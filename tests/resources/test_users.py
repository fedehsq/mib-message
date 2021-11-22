from .view_test import ViewTest
from faker import Faker


class TestMessages(ViewTest):
    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestMessages, cls).setUpClass()

    def test_delete_message(self):
        message = self.login_test_message()
        rv = self.client.delete('/message/%d' % message.id)
        assert rv.status_code == 202

    def test_get_message_by_id(self):
        # get a non-existent message
        rv = self.client.get('/message/0')
        assert rv.status_code == 404
        # get an existent message
        message = self.login_test_message()
        rv = self.client.get('/message/%d' % message.id)
        assert rv.status_code == 200

    def test_get_message_by_email(self):
        # get a non-existent message with faked email
        rv = self.client.get('/message_email/%s' % TestMessages.faker.email())
        assert rv.status_code == 404
        # get an existent message
        message = self.login_test_message()
        rv = self.client.get('/message_email/%s' % message.email)
        assert rv.status_code == 200