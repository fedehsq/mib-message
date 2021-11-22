import unittest


class ViewTest(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests resources
    """
    client = None

    @classmethod
    def setUpClass(cls):
        from mib import create_app
        app = create_app()
        cls.client = app.test_client()

        from tests.models.test_message import TestMessage
        cls.test_message = TestMessage

        from mib.dao.message_manager import MessageManager
        cls.message_manager = MessageManager()

    def login_test_message(self):
        """
        Simulate the message login for testing the resources
        :return: message
        """
        message = self.test_message.generate_random_message()
        psw = message.password
        message.set_password(message.password)

        self.message_manager.create_message(message=message)
        data = {
            'email': message.email,
            'password': psw,
        }

        response = self.client.post('/authenticate', json=data)
        json_response = response.json

        assert response.status_code == 200
        assert json_response["authentication"] == 'success'
        assert json_response['message'] is not None

        return message
