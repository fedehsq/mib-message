from mib import create_app
from celery import Celery
from datetime import datetime, timedelta
from celery.signals import worker_ready
from flask_mail import Mail, Message as Email

APP = None
mail = None

SENT_NOTIFICATION_OBJECT = 'Incoming message'
SENT_NOTIFICATION_BODY = 'A new message has been sent to you by '
READ_NOTIFICATION_OBJECT = 'Read message'
READ_NOTIFICATION_BODY = 'A message has been read by '
SENDER_EMAIL_ADDRESS = 'mymessageinabottle9@gmail.com'
# this is really safe
SENDER_EMAIL_PSW = 'elliotalderson'

BACKEND = BROKER = 'redis://messages_ms_redis-server:6379'
celery = Celery(__name__, backend = BACKEND, broker = BROKER)
celery.conf.beat_schedule = {
    "send_messages": {
        "task": "send_messages",
        "schedule": timedelta(seconds = 10)
    },  
    "send_read_notifications": {
        "task": "send_read_notifications",
        "schedule": timedelta(seconds = 10)
    },  
}

@celery.task(name = 'send_messages')
def send_messages():
    global APP
    if not APP:
        return
    with APP.app_context():
        from mib.models.message import Message, db
        # retrieve all scheduled messages from message table
        # filtering by expired time of delivery
        messages = db.session.query(Message).filter(\
            Message.scheduled == True, 
            Message.timestamp <= datetime.now()).all()
        for message in messages:
            
            message.sent = 1
            message.scheduled = False
            send_sent_notifications(message)
        db.session.commit()
    return 'all messages has been sent'

def send_email(object, sender, receiver, body):
    global mail
    email = Email(
            object,
            sender = SENDER_EMAIL_ADDRESS,
            recipients = [receiver]
        )
    email.body = body + sender
    mail.send(email)

def send_sent_notifications(message):
    send_email(
        SENT_NOTIFICATION_OBJECT, 
        message.sender, 
        message.receiver,
        SENT_NOTIFICATION_BODY)
"""    global mail
    email = Email(
            SENT_NOTIFICATION_OBJECT,
            sender = SENDER_EMAIL_ADDRESS,
            recipients = [message.receiver]
        )
    email.body = SENT_NOTIFICATION_BODY + message.sender
    mail.send(email)"""

@celery.task(name = 'send_read_notifications')
def send_read_notifications():
    global APP
    global mail
    if not APP:
        return
    with APP.app_context():
        from mib.models.message import Message, db
        # retrieve all read messages that has not yet notified to the sender
        messages = db.session.query(Message).filter(
            Message.read == 1,
            Message.sent == 1).all()
        for message in messages:
            # receiver read the message, notifies to the sender
            message.read = 2
            send_email(
                READ_NOTIFICATION_OBJECT,
                message.receiver,
                message.sender,
                READ_NOTIFICATION_BODY
            )
            """email = Email(
                    READ_NOTIFICATION_OBJECT,
                    sender = SENDER_EMAIL_ADDRESS,
                    recipients = [message.sender]
                )
            email.body = READ_NOTIFICATION_BODY + message.sender
            mail.send(email)"""
        db.session.commit()
        
    return 'all messages has been notified'

@worker_ready.connect
def start(sender, **k):
    with sender.app.connection() as conn:
        sender.app.send_task('background.initialize',
            connection = conn)

@celery.task
def initialize():
    global APP
    global mail
    # lazy init
    if APP is None:
        app = create_app()
        # configuration of mail
        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = SENDER_EMAIL_ADDRESS
        app.config['MAIL_PASSWORD'] = SENDER_EMAIL_PSW
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)
        APP = app
    else:
        app = APP
    return []