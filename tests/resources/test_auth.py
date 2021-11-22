from .view_test import ViewTest
from faker import Faker


class TestAuth(ViewTest):

    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestAuth, cls).setUpClass()

    def test_login(self):
        # login for a customer
        message = self.login_test_message()

        # login with a wrong email
        data = {
            'email': message.email,
            'password': TestAuth.faker.password()
        }

        response = self.client.post('/authenticate', json=data)
        json_response = response.json

        assert response.status_code == 401
        assert json_response["authentication"] == 'failure'
        assert json_response['message'] is None




    
    


