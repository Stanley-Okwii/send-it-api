import unittest
import json
from tests.base import BaseTestCase

class TestAuth(BaseTestCase):
    def test_user_registration(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1',
                content_type='application/json'
            )
            print(response)
            self.assertEqual(response.status_code, 200)
