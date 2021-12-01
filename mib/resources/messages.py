from re import M
from flask import request, jsonify
from sqlalchemy.sql.expression import or_
from sqlalchemy.sql.functions import user
from mib.dao.message_manager import MessageManager
from mib.models.message import Message
from mib import db
from sqlalchemy import cast, Date, or_
from datetime import datetime, timedelta
import json

def delete_message_by_id(message_id):
    """
    Delete the message with id = message_id.
    :param message_id the id of message to be deleted
    :return json response
    """
    message: Message = MessageManager.retrieve_by_id(message_id)
    if message is None:
        response_object = {
            'status': 'failure',
            'message': 'Message not found',
        }
        return jsonify(response_object), 404
    MessageManager.delete_message_by_id(message_id)
    response_object = {
        'status': 'success',
        'message': 'Successfully deleted',
    }
    return jsonify(response_object), 202

def get_message_by_id(message_id):
    """
    Get the message with id = message_id.
    :param message_id the id of message to retrieve
    :return json response
    """
    message: Message = MessageManager.retrieve_by_id(message_id)
    if message is None:
        response_object = {
            'status': 'failure',
            'message': 'Message not found',
        }
        return jsonify(response_object), 404
    response_object = {
        'status': 'success',
        'message': 'Operation done',
        'body': message.serialize(),
    }
    return jsonify(response_object), 200

def create_message():
    """
    This method allows the creation of a new message
    for the user with email == user_email.
    """
    post_data = request.get_json()
    message = Message()
    message.set_sender_id(post_data.get('sender_id'))
    message.set_sender(post_data.get('sender'))
    message.set_receiver_id(post_data.get('receiver_id'))
    message.set_receiver(post_data.get('receiver'))
    message.set_body(post_data.get('body'))
    message.set_photo(post_data.get('photo'))
    message.set_timestamp(post_data.get('timestamp'))
    message.set_draft(post_data.get('draft'))
    message.set_scheduled(post_data.get('scheduled'))
    message.set_bold(post_data.get('bold'))
    message.set_italic(post_data.get('italic'))
    message.set_underline(post_data.get('underline'))
    MessageManager.create_message(message)
    response_object = {
        'status': 'success',
        'message': 'Operation done',
        'body': message.serialize(),
    }
    print(message.serialize())
    return jsonify(response_object), 201

def update_message(message_id):
    """
    This method allows the edit of an existing message 
    for the user with id == user_id.
    """
    post_data = request.get_json()
    message = MessageManager.retrieve_by_id(message_id)
    if message is None:
        response_object = {
            'status': 'failure',
            'message': 'Message not found',
        }
        return jsonify(response_object), 404
    message.set_sender_id(post_data.get('sender_id'))
    message.set_sender(post_data.get('sender'))
    message.set_receiver_id(post_data.get('receiver_id'))
    message.set_receiver(post_data.get('receiver'))
    message.set_body(post_data.get('body'))
    message.set_photo(post_data.get('photo'))
    message.set_timestamp(post_data.get('timestamp'))
    message.set_draft(post_data.get('draft'))
    message.set_read(post_data.get('read'))
    message.set_sent(post_data.get('sent'))
    message.set_scheduled(post_data.get('scheduled'))
    message.set_bold(post_data.get('bold'))
    message.set_italic(post_data.get('italic'))
    message.set_underline(post_data.get('underline'))
    MessageManager.update_message(message)
    response_object = {
        'status': 'success',
        'message': 'Operation done',
        'body': message.serialize(),
    }
    return jsonify(response_object), 200

def search_message():
    # gets from the request the id of the user and the desidered list
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    user_email = post_data.get('user_email')
    body = post_data.get('body')
    email = post_data.get('sender')
    date = post_data.get('date')

    # search
    filtered_inbox, filtered_sent, filtered_scheduled = \
        search_messages(user_id, user_email, body, email, date)

    response_object = {
        'status': 'success',
        'message': 'Successfully searched',
        'body': {    
            'filtered_inbox': [message.serialize() for message in filtered_inbox],
            'filtered_sent': [message.serialize() for message in filtered_sent],
            'filtered_scheduled': [message.serialize() for message in filtered_scheduled]
        }
    }
    return jsonify(response_object), 200

def get_inbox_messages():
    """    
    this function returns the inbox messages
    for a given user.
    """
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    user_email = post_data.get('user_email')
    messages = db.session.query(Message).filter(\
        # in this way the messages read don't deseappear in the mailbox
        Message.receiver == user_email,
        Message.receiver_id == user_id,
        or_(Message.sent == 1,  Message.sent == 2))
    response_object = {
        'status':'success',
        'message':'successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200

def get_scheduled_messages():
    """    
    this function returns the scheduled messages
    for the user with email == user_email.
    """
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    user_email = post_data.get('user_email')
    messages = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.sender_id == user_id,
        Message.scheduled == True).all() 
    response_object = {
        'status':'success',
        'message': 'Successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200


def get_sent_messages():
    """    
    this function returns the sent messages
    for the user with email == user_email.
    """
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    user_email = post_data.get('user_email')
    messages = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.sender_id == user_id,
        # in this way the messages read don't deseappear in the mailbox
        or_(Message.sent == 1, Message.sent == 2),
        )
    response_object = {
        'status':'success',
        'message':'Successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200

def get_draft_messages():
    """    
    this function returns the draft messages
    for the user with email == user_email.
    """
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    user_email = post_data.get('user_email')
    messages = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.sender_id == user_id,
        Message.draft == True)
    response_object = {
        'status':'success',
        'message':'Successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200


def get_notifications():
    """
    This function returns the notification numbers
    for the user with email == user_email.
    """
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    user_email = post_data.get('user_email')
    print(user_id)
    print(user_email)
    inbox = db.session.query(Message).filter(\
        Message.receiver == user_email,
        Message.receiver_id == user_id,
        Message.sent == 1, 
        Message.read == 0).count()
    sent = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.sender_id == user_id,
        Message.sent == 1, 
        or_(Message.read == 1, Message.read == 2)).count()
    
    response_object = {
        'status':'success',
        'message':'Successfully delivered notifications',
        'body': {
            'inbox': inbox,
            'sent': sent,
        }
    }
    return jsonify(response_object), 200

##################################################################
###############-------Auxiliary Functions-------##################
##################################################################

def search_messages(user_id, user_email, body, sender, date):
    """
    Given the body (and/or) the sender (and/or) the date, 
    returns the filtered messages
    """
    if date:
        #  2022-06-05 12:12:00
        date = datetime.strptime(date, '%Y-%m-%d')
    inbox = db.session.query(Message).filter(\
        Message.receiver_id == user_id, 
        Message.receiver == user_email, 
        Message.sent != 0,
        Message.body.contains(body),
        Message.timestamp.cast(Date) == date if date else True
        ).all()
    sent = db.session.query(Message).filter(\
        Message.sender_id == user_id, 
        Message.sender == user_email, 
        Message.sent != 0,
        Message.body.contains(body),
        Message.timestamp.cast(Date) == date if date else True
        ).all()
    scheduled = db.session.query(Message).filter(\
        Message.sender_id == user_id, 
        Message.sender == user_email, 
        Message.scheduled == True,
        Message.body.contains(body),
        Message.sender.contains(sender),
        Message.timestamp.cast(Date) == date if date else True     
        ).all()
    return inbox, sent, scheduled