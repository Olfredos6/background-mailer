
from pickle import TRUE
from rest_framework.test import APITestCase
from rest_framework import status


class EmailTests(APITestCase):

    def setUp(self):
        self.valid_payload = {
            'subject': 'A Test',
            'recipient': ['me@nehemie.dev'],
            'content': '<H6>Welcome</H6><br><p>We are testing new features</p>',
            'html': True,
            'port': 456,
            'host': 'mail.test.com',
            'username': 'test@test.com',
            'password': 'somepassowrd',
            'template': 'welcome'
            # templates folder, name of the template file
        }
    

    def test_sends_email(self):
        '''
            Tests that we can send email
            provided a correct payload
        '''
        pass

    def test_can_send_to_many_recipients(self):
        pass

    def test_incorrect_payload_returns_descriptive_message(self):
        '''
            We want to include the name of the fields
            causing a problem when posting
        '''
        pass