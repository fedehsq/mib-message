from .view_test import ViewTest
from faker import Faker

class TestMessages(ViewTest):
    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestMessages, cls).setUpClass()

    def test_message(self):
        #test add message
        data = {
            'id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'sender':TestMessages.faker.email(),
            'sender_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver': TestMessages.faker.email(),
            'body': TestMessages.faker.paragraph(nb_sentences= 2),
            'timestamp':TestMessages.faker.date_time().strftime("%d/%m/%Y %H:%M"),
            'draft': False,
            'scheduled': True,
            'sent': 0,
            'read': 0,
            'bold': False,
            'italic': False,
            'underline': False
        }
        rv = self.client.post('/message', json=data)
        
        assert rv.status_code == 201
        
    
    def test_delete(self):
        data = {
            'id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'sender':TestMessages.faker.email(),
            'sender_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver': TestMessages.faker.email(),
            'body': TestMessages.faker.paragraph(nb_sentences= 2),
            'timestamp':TestMessages.faker.date_time().strftime("%d/%m/%Y %H:%M"),
            'draft': False,
            'scheduled': True,
            'sent': 0,
            'read': 0,
            'bold': False,
            'italic': False,
            'underline': False
        }
        rv = self.client.post('/message', json=data)
        body=rv.json["body"]
        id=body["id"]
        #test delete of existing message
        rv = self.client.delete('/message/%d' % id)
        assert rv.status_code == 202

        #test delete of not existing message
        rv = self.client.delete('/message/0')
        assert rv.status_code == 404


    def test_get_message(self):
        data = {
            'id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'sender':TestMessages.faker.email(),
            'sender_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver': TestMessages.faker.email(),
            'body': TestMessages.faker.paragraph(nb_sentences= 2),
            'timestamp':TestMessages.faker.date_time().strftime("%d/%m/%Y %H:%M"),
            'draft': False,
            'scheduled': True,
            'sent': 0,
            'read': 0,
            'bold': False,
            'italic': False,
            'underline': False
        }
        rv = self.client.post('/message', json=data)
        body=rv.json["body"]
        id=body["id"]
        #test get of existing message
        rv = self.client.get('/message/%d' % id)
        assert rv.status_code==200

        #test get of not existing message
        rv = self.client.get('/message/0')
        assert rv.status_code==404

    def test_update_message(self):
        data = {
            'id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'sender':TestMessages.faker.email(),
            'sender_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'receiver': TestMessages.faker.email(),
            'body': TestMessages.faker.paragraph(nb_sentences= 2),
            'timestamp':TestMessages.faker.date_time().strftime("%d/%m/%Y %H:%M"),
            'draft': False,
            'scheduled': True,
            'sent': 0,
            'read': 0,
            'bold': False,
            'italic': False,
            'underline': False
        }
        rv = self.client.post('/message', json=data)
        body=rv.json["body"]
        id=body["id"]
        
        #test update of existing message
        data["body"]=TestMessages.faker.paragraph(nb_sentences= 4)
        rv = self.client.put('/message/%d' % id, json=data)
        assert rv.status_code==200

        #test update of not existing message
        rv = self.client.put('/message/0', json=data)
        assert rv.status_code==404

    def test_search(self):
        data = {
            'user_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'user_email':TestMessages.faker.email(),
            'body': TestMessages.faker.paragraph(nb_sentences= 2)
        }
        rv = self.client.post('/search', json=data)
        
        print(rv)
        if(rv == None):
            print("ciao")
        assert rv.status_code == 200
     
    
    def test_inbox(self):
        data = {
            'user_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'user_email':TestMessages.faker.email(),
        }
        rv = self.client.get('/inbox', json = data)
        assert rv.status_code == 200
    
    def test_sent(self):
        data = {
            'user_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'user_email':TestMessages.faker.email(),
        }
        rv = self.client.get('/sent', json = data)
        assert rv.status_code == 200
        
    def test_draft(self):
        data = {
            'user_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'user_email':TestMessages.faker.email(),
        }
        rv = self.client.get('/draft', json = data)
        assert rv.status_code == 200

    def test_scheduled(self):
        data = {
            'user_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'user_email':TestMessages.faker.email(),
        }
        rv = self.client.get('/scheduled', json = data)
        assert rv.status_code == 200

    def test_notifications(self):
        data = {
            'user_id': TestMessages.faker.pyint(min_value=1, max_value=999),
            'user_email':TestMessages.faker.email(),
        }
        rv = self.client.get('/notifications', json = data)
        assert rv.status_code == 200
