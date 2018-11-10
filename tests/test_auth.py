import unittest
from tests.base import BaseTestCase

class TestAuth(BaseTestCase):
    def test_show_welcome_message(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1',
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)

    def test_show_all_registered_users(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/users',
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        """
        Test a user can create an account
        :return:
        """
        with self.client:
            response = self.register_new_user("ajori","ajori@gmail.com","000000")
            data = response.get_json()

            self.assertTrue(data['message'] == 'successfully created new user account')
            self.assertEqual(response.status_code, 201)

    def test_delete_user(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        with self.client:
            response = self.client.delete(
                'api/v1/user/stanley@gmail.com',
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 204)


