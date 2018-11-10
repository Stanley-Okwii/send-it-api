from app import app
from flask_testing import TestCase
import json


class BaseTestCase(TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        :return:
        """
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def register_user(self, name, email, password):
        """
        Helper method for registering a user with dummy data
        :return:
        """
        return self.client.post(
            'v1/user',
            content_type='application/json',
            data=json.dumps(dict(name=name, email=email, password=password)))
