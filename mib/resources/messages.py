from flask import request, jsonify
from mib.dao.message_manager import MessageManager
from mib.models.message import Message
import datetime


def create_message():
    """This method allows the creation of a new user.
    """
    post_data = request.get_json()
    id_sender = post_data.get('sender')
    id_receiver = post_data.get('receiver')

    message = Message()
    
    message.set_sender(id_sender)
    message.set_receiver(id_receiver)
    message.set_body(post_data.get('body'))
    message.set_photo(post_data.get('photo'))
    message.set_timestamp(post_data.get('timestamp'))
    message.set_draft(post_data.get('draft'))
    message.set_bold(post_data.get('scheduled'))
    message.set_bold(post_data.get('bold'))
    message.set_bold(post_data.get('italic'))
    message.set_bold(post_data.get('underline'))


    MessageManager.create_message(message)

    response_object = {
        'message': message.serialize(),
        'status': 'success',
        'message': 'Successfully registered',
    }

    return jsonify(response_object), 201
