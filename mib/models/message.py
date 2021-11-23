from werkzeug.security import generate_password_hash, check_password_hash

from mib import db


class Message(db.Model):
    """Representation of Message model."""

    # The name of the table that we explicitly set
    __tablename__ = 'Message'

    # A list of fields to be serialized
    SERIALIZE_LIST = ['id', 'sender', 'receiver', 'body', 'draft', 'scheduled']

    # All fields of message
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sender = db.Column(db.Integer, default=0)
    receiver = db.Column(db.Integer, default=0)

    body = db.Column(db.Unicode(8196), nullable = False, unique = False)
    photo = db.Column(db.Unicode(8196), default = 'profile_pics/profile_pic.svg')
    timestamp = db.Column(db.DateTime())
    draft = db.Column(db.Boolean, default = True)
    scheduled = db.Column(db.Boolean, default = False)
    sent = db.Column(db.Integer, default =0)
    read = db.Column(db.Boolean, default = False)
    bold = db.Column(db.Boolean, default = False)
    italic = db.Column(db.Boolean, default = False)
    underline = db.Column(db.Boolean, default = False)
    hidden_for_sender = db.Column(db.Boolean, default = False)
    hidden_for_receiver = db.Column(db.Boolean, default = False)

    def __init__(self, *args, **kw):
        super(Message, self).__init__(*args, **kw)

    def set_sender(self, sender):
        self.sender = sender

    def set_receiver(self, receiver):
        self.receiver = receiver

    def set_body(self, body):
        self.body = body

    def set_photo(self, photo):
        self.photo = photo
    
    def set_draft(self, draft):
        self.draft = draft
    
    def set_scheduled(self, scheduled):
        self.scheduled = scheduled
    
    def set_sent(self, sent):
        self.sent = sent

    def set_read(self, read):
        self.read = read

    def set_bold(self, bold):
        self.bold = bold

    def set_italic(self, italic):
        self.italic = italic

    def set_underline(self, underline):
        self.underline = underline

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def serialize(self):
        return dict([(k, self.__getattribute__(k)) for k in self.SERIALIZE_LIST])
