from flask import request, jsonify
from mib.dao.message_manager import MessageManager
from mib.models.message import Message
from mib import db
import datetime
import json

def create_message():
    """This method allows the creation of a new user.
    """
    post_data = request.get_json()
    mail_sender = post_data.get('sender')
    mail_receiver = post_data.get('receiver')

    message = Message()
    
    message.set_sender(mail_sender)
    message.set_receiver(mail_receiver)
    message.set_body(post_data.get('body'))
    message.set_photo(post_data.get('photo'))
    message.set_timestamp(post_data.get('timestamp'))
    message.set_draft(post_data.get('draft'))
    message.set_bold(post_data.get('scheduled'))
    message.set_bold(post_data.get('bold'))
    message.set_italic(post_data.get('italic'))
    message.set_underline(post_data.get('underline'))
    message.set_sent(True)
    MessageManager.create_message(message)

    response_object = {
        'message': message.serialize(),
        'status': 'success',
        'message': 'Successfully registered',
    }

    return jsonify(response_object), 201


def search_message():
    #gets from the request the id of the user and the desidered list
    post_data=request.get_json()
    id_user = post_data.get('id')
    body = post_data.get('body')
    email = post_data.get('email')
    date = post_data.get('date')

    #search
    res_received, res_sent, res_to_be_sent = search_messages(id_user,body, email, date)


    response_object = {
        'res_received': res_received,
        'res_sent': res_sent,
        'res_to_be_sent': res_to_be_sent,
        'status': 'success',
        'message': 'Successfully searched',
    }
    return jsonify(response_object)

#this function returns the requested list of messages
def get_messages():
    #gets from the request the id of the user and the desidered list
    post_data=request.get_json()
    id_user = post_data.get('email')
    type_of_list = post_data.get('op')
    messages=''

    #cases for each function
    if type_of_list == "inbox":
        messages=db.session.query(Message).filter(Message.receiver==id_user,Message.sent==True, Message.hidden_for_receiver==False)
    if type_of_list == "scheduled":
        messages=db.session.query(Message).filter(Message.sender==id_user,Message.scheduled==True)
    if type_of_list == "sent":
        messages=db.session.query(Message).filter(Message.sender==id_user,Message.sent==True, Message.hidden_for_sender==False)
    if type_of_list == "draft":
        messages=db.session.query(Message).filter(Message.sender==id_user,Message.draft==True)
        
    #assembling the json
    msgs=[]
    for m in messages:
        msgs.append(m.to_string())

    #assembling the response
    response_object={
        'list':msgs,
        'status':'success',
        'message':'successfully delivered list'
    }
    return jsonify(response_object)


# Given the body, the sender and the date, returns the filtered messages
def search_messages(id,msg_field, msg_user, msg_date):
    res_to_be_sent=[]
    res_received=[]
    res_sent=[]
    
    to_be_sent_messages = db.session.query(Message).filter(Message.sender==id, Message.scheduled==True)
    received_messages = db.session.query(Message).filter(Message.receiver==id, Message.sent==True)
    sent_messages = db.session.query(Message).filter(Message.sender==id, Message.sent==True)    
    
    if msg_date is None:
        msg_date=""
    if msg_field is None:
        msg_field=""
    if msg_user is None:
        msg_user=""

    #assembling the lists
    to_be_sent_msgs=[]
    for m in to_be_sent_messages:
        to_be_sent_msgs.append(m.to_string())
    sent_msgs=[]
    for m in sent_messages:
        sent_msgs.append(m.to_string())
    received_msgs=[]
    for m in received_messages:
        received_msgs.append(m.to_string())

    #checks for three none args
    if not msg_field and not msg_user and not msg_date:
        return 0,0,0

    #checks for date format 
    """     if msg_date:
        try:
            msg_date=datetime.strptime(msg_date, '%Y-%m-%d').strftime('%d/%m/%Y')
            print(msg_date)
        except:
            return "error","error","error" """

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