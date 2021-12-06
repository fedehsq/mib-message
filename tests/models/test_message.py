import unittest

from faker import Faker

from .model_test import ModelTest


class TestMessage(ModelTest):

    faker = Faker()

    @classmethod
    def setUpClass(cls):
        super(TestMessage, cls).setUpClass()

        from mib.models import message
        cls.message = message

    @staticmethod
    def assertMessageEquals(value, expected):
        t = unittest.FunctionTestCase(TestMessage)
        t.assertEqual(value.id, expected.id)


    @staticmethod
    def generate_random_message():
        sender_id = TestMessage.faker.pyint(min_value=1, max_value=999)
        receiver_id = TestMessage.faker.pyint(min_value=1, max_value= 999)
        sender = TestMessage.faker.email()
        receiver = TestMessage.faker.email()
        body = TestMessage.faker.paragraph(nb_sentences= 2)
        photo = TestMessage.faker.file_extension(category='image')
        timestamp = TestMessage.faker.date_time()
        draft = False
        scheduled = True
        bold = False
        italic = False
        underline = False
        deleted = 0


        from mib.models import Message

        message = Message(
            sender_id = sender_id,
            receiver_id = receiver_id,
            sender = sender,
            receiver = receiver,
            body = body,
            photo = photo,
            timestamp = timestamp,
            draft = draft,
            scheduled = scheduled,
            bold = bold,
            italic = italic,
            underline = underline,
            deleted = deleted
        )

        return message

    def test_set_sender_id(self):
        message = TestMessage.generate_random_message()
        sender_id = TestMessage.faker.pyint(min_value=1, max_value=999)
        message.set_sender_id(sender_id)
        self.assertEqual(sender_id,message.sender_id)
        
    def test_set_receiver_id(self):
        message = TestMessage.generate_random_message()
        receiver_id = TestMessage.faker.pyint(min_value=1, max_value=999)
        message.set_receiver_id(receiver_id)
        self.assertEqual(receiver_id,message.receiver_id)
    
    def test_set_sender(self):
        message = TestMessage.generate_random_message()
        sender = TestMessage.faker.email()
        message.set_sender(sender)
        self.assertEqual(sender,message.sender)
    
    def test_set_receiver(self):
        message = TestMessage.generate_random_message()
        receiver = TestMessage.faker.email()
        message.set_receiver(receiver)
        self.assertEqual(receiver,message.receiver)
    
    def test_set_body(self):
        message = TestMessage.generate_random_message()
        body = TestMessage.faker.paragraph(nb_sentences= 2)
        message.set_body(body)
        self.assertEqual(body, message.body)
    
    def test_set_photo(self):
        message = TestMessage.generate_random_message()
        photo = TestMessage.faker.file_extension(category='image')
        message.set_photo(photo)
        self.assertEqual(photo, message.photo)

    def test_timestamp(self):
        message = TestMessage.generate_random_message()
        timestamp = TestMessage.faker.date_time()
        message.set_timestamp(timestamp.strftime("%d/%m/%Y %H:%M"))
        self.assertEqual(timestamp.strftime("%d/%m/%Y %H:%M"), message.timestamp.strftime("%d/%m/%Y %H:%M"))
    
    def test_draft(self):
        message = TestMessage.generate_random_message()
        draft = TestMessage.faker.boolean()
        message.set_draft(draft)
        self.assertEqual(draft, message.draft)

    def test_scheduled(self):
        message = TestMessage.generate_random_message()
        scheduled = TestMessage.faker.boolean()
        message.set_scheduled(scheduled)
        self.assertEqual(scheduled, message.scheduled)
    
    def test_bold(self):
        message = TestMessage.generate_random_message()
        bold = TestMessage.faker.boolean()
        message.set_bold(bold)
        self.assertEqual(bold, message.bold)
    
    def test_italic(self):
        message = TestMessage.generate_random_message()
        italic = TestMessage.faker.boolean()
        message.set_italic(italic)
        self.assertEqual(italic, message.italic)
    
    def test_underline(self):
        message = TestMessage.generate_random_message()
        underline = TestMessage.faker.boolean()
        message.set_underline(underline)
        self.assertEqual(underline, message.underline)
