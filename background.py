from mib import create_app
from celery import Celery
from datetime import datetime, timedelta
from celery.signals import worker_ready

APP = None

BACKEND = BROKER = 'redis://messages_ms_redis-server:6379'
celery = Celery(__name__, backend = BACKEND, broker = BROKER)
celery.conf.beat_schedule = {
    "send_messages": {
        "task": "send_messages",
        "schedule": timedelta(seconds = 10)
    },   
}

@celery.task(name = 'send_messages')
def send_messages():
    with APP.app_context():
        from mib.models.message import Message, db
        # retrieve all scheduled messages from message table
        # filtering by expired time of delivery
        messages = db.session.query(Message).filter(\
            Message.scheduled == True, 
            Message.timestamp <= datetime.now()).all()
        for message in messages:
            print(message.serialize())
            message.sent = 1
            message.scheduled = False
        db.session.commit()
    return 'all messages has been sent'

@worker_ready.connect
def start(sender, **k):
    with sender.app.connection() as conn:
        sender.app.send_task('background.initialize',
            connection = conn)

@celery.task
def initialize():
    global APP
    # lazy init
    if APP is None:
        app = create_app()
        APP = app
    else:
        app = APP
    return []