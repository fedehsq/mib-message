from flask import request, jsonify
from mib.dao.message_manager import MessageManager
from mib.models.message import Message
from mib import db
from sqlalchemy import cast, Date
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

def create_message(user_email):
    """
    This method allows the creation of a new message
    for the user with email == user_email.
    """
    post_data = request.get_json()
    #mail_sender = post_data.get('sender')
    email_receiver = post_data.get('receiver')
    message = Message()
    message.set_sender(user_email)
    message.set_receiver(email_receiver)
    message.set_body(post_data.get('body'))
    message.set_photo(post_data.get('photo'))
    message.set_timestamp(post_data.get('timestamp'))
    message.set_draft(post_data.get('draft'))
    message.set_scheduled(post_data.get('scheduled'))
    message.set_bold(post_data.get('bold'))
    message.set_italic(post_data.get('italic'))
    message.set_underline(post_data.get('underline'))
    #just for test purposes set sent=1
    #message.set_sent(1)
    ###################
    MessageManager.create_message(message)
    response_object = {
        'status': 'success',
        'message': 'Operation done',
        'body': message.serialize(),
    }
    return jsonify(response_object), 201

def update_message(user_email):
    """
    This method allows the edit of an existing message 
    for the user with email == user_email.
    """
    post_data = request.get_json()
    #mail_sender = post_data.get('sender')
    email_receiver = post_data.get('receiver')
    message = MessageManager.retrieve_by_id(post_data.get('id'))
    if message is None:
        response_object = {
            'status': 'failure',
            'message': 'Message not found',
        }
        return jsonify(response_object), 404
    message.set_sender(user_email)
    message.set_receiver(email_receiver)
    message.set_body(post_data.get('body'))
    message.set_photo(post_data.get('photo'))
    message.set_timestamp(post_data.get('timestamp'))
    message.set_draft(post_data.get('draft'))
    message.set_scheduled(post_data.get('scheduled'))
    message.set_bold(post_data.get('bold'))
    message.set_italic(post_data.get('italic'))
    message.set_underline(post_data.get('underline'))
    #just for test purposes set sent=1
    #message.set_sent(1)
    ###################
    MessageManager.update_message(message)
    response_object = {
        'status': 'success',
        'message': 'Operation done',
        'body': message.serialize(),
    }
    return jsonify(response_object), 200


def search_message(user_email):
    # gets from the request the id of the user and the desidered list
    post_data = request.get_json()
    #id_user = post_data.get('id')
    body = post_data.get('body')
    email = post_data.get('sender')
    date = post_data.get('date')

    # search
    filtered_inbox, filtered_sent, filtered_scheduled = \
        search_messages(user_email, body, email, date)

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

"""#this function returns the requested list of messages
def get_messages(email):
    #gets from the request the id of the user and the desidered list
    post_data=request.get_json()
    #id_user = post_data.get('email')
    type_of_list = post_data.get('op')
    #messages=''

    #cases for each function
    if type_of_list == "inbox":
        messages = db.session.query(Message).filter(Message.receiver == email,Message.sent==1, Message.hidden_for_receiver==False)
    if type_of_list == "scheduled":
        messages = db.session.query(Message).filter(Message.sender == email,Message.scheduled==True)
    if type_of_list == "sent":
        messages = db.session.query(Message).filter(Message.sender == email,Message.sent==1, Message.hidden_for_sender==False)
    if type_of_list == "draft":
        messages = db.session.query(Message).filter(Message.sender == email,Message.draft==True)
        
    #assembling the json
    msgs=[]
    for m in messages:
        msgs.append(m.to_string())
    #assembling the response
    response_object={
        'list': [message.serialize() for message in messages],
        'status':'success',
        'message':'successfully delivered list'
    }
    return jsonify(response_object), 200"""


def get_inbox_messages(user_email):
    """    
    this function returns the inbox messages
    for the user with email == user_email.
    """
    messages = db.session.query(Message).filter( \
        Message.receiver == user_email, 
        Message.sent == 1, 
        Message.hidden_for_receiver == False)
    response_object = {
        'status':'success',
        'message':'successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200

def get_scheduled_messages(user_email):
    """    
    this function returns the scheduled messages
    for the user with email == user_email.
    """
    messages = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.scheduled == True).all() 
    response_object = {
        'status':'success',
        'message': 'Successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200


def get_sent_messages(user_email):
    """    
    this function returns the sent messages
    for the user with email == user_email.
    """
    messages = db.session.query(Message).filter(\
        Message.sender == user_email, Message.sent == 1,
        Message.hidden_for_sender == False)
    response_object = {
        'status':'success',
        'message':'Successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200

def get_draft_messages(user_email):
    """    
    this function returns the draft messages
    for the user with email == user_email.
    """
    messages = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.draft == True)
    response_object = {
        'status':'success',
        'message':'Successfully delivered list',
        'body': [message.serialize() for message in messages],
    }
    return jsonify(response_object), 200


def get_notifications(user_email):
    """
    This function returns the notification numbers
    for the user with email == user_email.
    """

    inbox = db.session.query(Message).filter(\
        Message.receiver == user_email,
        Message.sent == 1, 
        Message.read == False).count()
    sent = db.session.query(Message).filter(\
        Message.sender == user_email,
        Message.sent == 1, 
        Message.read == True).count()
       
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

def search_messages(user_email, body, sender, date):
    """
    Given the body (and/or) the sender (and/or) the date, 
    returns the filtered messages
    """
    """ if not body and not sender and not date:
        return 0, 0, 0
    try:
        msg_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    except:
        msg_date = ''"""

    if date:
        #  2022-06-05 12:12:00
        date = datetime.strptime(date, '%Y-%m-%d')
    inbox = db.session.query(Message).filter(\
        Message.receiver == user_email, 
        Message.sent != 0,
        Message.body.contains(body),
        Message.timestamp.cast(Date) == date if date else True
        ).all()
    sent = db.session.query(Message).filter(\
        Message.sender == user_email, 
        Message.sent != 0,
        Message.body.contains(body),
        Message.timestamp.cast(Date) == date if date else True
        ).all()
    scheduled = db.session.query(Message).filter(\
        Message.sender == user_email, 
        Message.scheduled == True,
        Message.body.contains(body),
        Message.sender.contains(sender),
        Message.timestamp.cast(Date) == date if date else True     
        ).all()
    print('schedulati!!!!!!')
    for s in scheduled:
        print(s.serialize())
    return inbox, sent, scheduled

"""def filter_list(messages, body, sender, date):
    Returns a filtered list 
    for m in messages:
        if body in m.body and sender in m.sender and date in m.timestamp:
            messages.append(m)"""


"""# Given the body, the sender and the date, returns the filtered messages
def search_messages(id,msg_field, msg_user, msg_date):
    res_to_be_sent=[]
    res_received=[]
    res_sent=[]
    
    scheduled = db.session.query(Message).filter(Message.sender==id, Message.scheduled==True)
    inbox = db.session.query(Message).filter(Message.receiver==id, Message.sent==True)
    sent = db.session.query(Message).filter(Message.sender==id, Message.sent==True)    
    
    if msg_date is None:
        msg_date=""
    if msg_field is None:
        msg_field=""
    if msg_user is None:
        msg_user=""

    #assembling the lists
    to_be_sent_msgs=[]
    for m in scheduled:
        to_be_sent_msgs.append(m.to_string())
    sent_msgs=[]
    for m in sent:
        sent_msgs.append(m.to_string())
    received_msgs=[]
    for m in inbox:
        received_msgs.append(m.to_string())

    #checks for three none args
    if not msg_field and not msg_user and not msg_date:
        return 0,0,0

    #checks for date format 
        if msg_date:
        try:
            msg_date=datetime.strptime(msg_date, '%Y-%m-%d').strftime('%d/%m/%Y')
            print(msg_date)
        except:
            return "error","error","error" 

    for cm in to_be_sent_msgs:
        curr=json.loads(cm)
        body=curr["body"]
        timestamp=curr["timestamp"]
        if msg_field in body and msg_date in timestamp:
            if msg_field or msg_user or msg_date: 
                res_to_be_sent.append(json.dumps(cm))

    for cm in sent_msgs:
        curr=json.loads(cm)
        body=curr["body"]
        timestamp=curr["timestamp"]
        if msg_field in body and msg_date in timestamp:
            res_sent.append(json.dumps(cm))
    
    for cm in received_messages:
        curr=json.loads(cm)
        body=curr["body"]
        sender=curr["sender"]
        timestamp=curr["timestamp"]
        if msg_field in body and msg_user in sender and msg_date in timestamp:
            res_received.append(json.dumps(cm))
    
    return res_received,res_sent,res_to_be_sent
    """