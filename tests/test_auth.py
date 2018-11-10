import unittest
from tests.base import BaseTestCase
import json

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

    def test_update_of_user_information(self):
        """
        Test a user can update their account name and password
        :return:
        """
        with self.client:
            self.register_new_user("joyce","joyce@gmail.com","000000")
            response = self.client.put(
                'api/v1/user/joyce@gmail.com',
                data=json.dumps(dict(name="superstar", password="007007"))
            )

            self.assertEqual(response.status_code, 201)

    def test_delete_user(self):
        """
        Test a user is successfully deleted
        :return:
        """
        with self.client:
            response = self.client.delete(
                'api/v1/user/stanley@gmail.com'
            )

            self.assertEqual(response.status_code, 204)

    def test_fetch_specific_user(self):
        """
        Test to get details of a given user
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/user/okwii@gmail.com'
            )

            self.assertEqual(response.status_code, 200)

    def test_fetch_user_with_incorrect_email_format(self):
        """
        Test to get details of a given user with a wrong email format
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/user/owiigmail.com'
            )

            self.assertEqual(response.status_code, 400)

    def test_fetch_user_who_is_not_registered(self):
        """
        Test to get details of a given user with a wrong email format
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/user/andries@gmail.com'
            )

            self.assertEqual(response.status_code, 404)

    def test_register_new_user_with_password_less_than_4_characters(self):
        """
        Test to create user with a password of less than 4 characters
        :return:
        """
        with self.client:
            response = self.register_new_user("wrong_user", "wrong_user@gmail.com", "123")

            self.assertEqual(response.status_code, 400)
