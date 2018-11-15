from tests.base import BaseTestCase
import json

class TestAuth(BaseTestCase):
    def test_show_welcome_message(self):
        """
        Test that api displays welcome message
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
                'api/v1/users/admin@gmail.com',
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        """
        Test a user can create an account
        :return:
        """
        with self.client:
            response = self.register_new_user("ajori","ajori@gmail.com","000000", "user")
            data = response.get_json()

            self.assertTrue(data['message'] == 'successfully created new user account')
            self.assertEqual(response.status_code, 201)

    def test_user_who_is_not_admin_can_not_view_users_list(self):
        """
        Test a user who is not admin can not view users list
        :return:
        """
        with self.client:
            self.register_new_user("arnold","arnold@gmail.com","000000", "user")
            response = self.client.get(
                'api/v1/users/arnold@gmail.com',
                content_type='application/json'
            )
            data = response.get_json()

            self.assertTrue(data['message'] == 'you do not have permission to access this endpoint')
            self.assertEqual(response.status_code, 404)

    def test_update_of_user_information(self):
        """
        Test a user can update their account name and password
        :return:
        """
        with self.client:
            self.register_new_user("joyce","joyce@gmail.com","000000", "user")
            response = self.client.put(
                'api/v1/user/joyce@gmail.com',
                content_type= "application/json",
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
            response = self.register_new_user("wrong_user", "wrong_user@gmail.com", "123", "user")

            self.assertEqual(response.status_code, 400)

    def test_custom_error_url_found(self):
        """
        Test requested endpoint was not found
        :return:
        """
        with self.client:
            response = self.client.put(
                '/api/v1/users/stanley@gmail.com/forget'
            )

            self.assertEqual(response.status_code, 404)

    def test_custom_error_method_not_allowed_for_the_requested_URL(self):
        """
        Test method is not allowed for the requested URL
        :return:
        """
        with self.client:
            response = self.client.patch(
                'api/v1/user'
            )

            self.assertEqual(response.status_code, 405)

    def test_sign_in_request_is_json(self):
        """
        Test that the content type is application/json
        :return:
        """
        with self.client:
            response = self.client.post(
                '/api/v1/auth/signin',
                content_type='application/javascript',
                data=json.dumps(dict(email='example@gmail.com', password='123456')))
            data = json.loads(response.data.decode())
            self.assertTrue(response.status, 400)
            self.assertTrue(data['message'] == 'content type must be application/json', msg='Check the returned message')

    def test_sign_up_with_empty_string(self):
        """
        Test user can not sign up with empty strings
        :return:
        """
        with self.client:
            response = self.client.post(
                '/api/v1/user',
                content_type='application/json',
                data=json.dumps(dict(email='new@gmail.com', password='123456', role="user", name="")))
            self.assertTrue(response.status_code, 400)

    def test_sign_up_with_missing_property(self):
        """
        Test user can not sign up with property
        :return:
        """
        with self.client:
            response = self.client.post(
                '/api/v1/user',
                content_type='application/json',
                data=json.dumps(dict(email='new@gmail.com', password='123456', name="")))
            self.assertTrue(response.status_code, 400)

