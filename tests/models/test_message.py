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
        t.assertEqual(value.email, expected.email)
        t.assertEqual(value.password, expected.password)
        t.assertEqual(value.is_active, expected.is_active)
        t.assertEqual(value.authenticated, False)
        t.assertEqual(value.is_anonymous, expected.is_anonymous)

    @staticmethod
    def generate_random_message():
        email = TestMessage.faker.email()
        password = TestMessage.faker.password()
        is_active = TestMessage.faker.boolean()
        is_admin = TestMessage.faker.boolean()
        authenticated = TestMessage.faker.boolean()
        is_anonymous = TestMessage.faker.boolean()
        first_name = TestMessage.faker.first_name()
        last_name = TestMessage.faker.last_name()
        phone = TestMessage.faker.phone_number()

        from mib.models import Message

        message = Message(
            email=email,
            password=password,
            is_active=is_active,
            is_admin=is_admin,
            authenticated=authenticated,
            is_anonymous=is_anonymous,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )

        return message

    def test_set_password(self):
        message = TestMessage.generate_random_message()
        password = self.faker.password(length=10, special_chars=False, upper_case=False)
        message.set_password(password)

        self.assertEqual(
            message.authenticate(password),
            True
        )
    
    def test_set_email(self):
        message = TestMessage.generate_random_message()
        email = self.faker.email()
        message.set_email(email)
        self.assertEqual(email, message.email)

    def test_is_authenticated(self):
        message = TestMessage.generate_random_message()
        self.assertFalse(message.is_authenticated())
