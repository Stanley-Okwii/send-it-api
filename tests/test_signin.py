from tests.base import BaseTestCase
import json

class TestSignIn(BaseTestCase):
    def test_user_can_login_successfully(self):
        """
        Test that a user can login with correct password and email
        :return:
        """
        with self.client:
            self.register_new_user("user","user@gmail.com", "00000")
            response = self.client.post(
                'api/v1/auth/signin',
                content_type='application/json',
                data=json.dumps(dict(email="user@gmail.com", password="00000"))
            )

            self.assertEqual(response.status_code, 200)

    def test_user_login_with_incorrect_password(self):
        """
        Test that user can not log in with wrong password
        :return:
        """
        with self.client:
            self.register_new_user("newuser","new_user@gmail.com", "00000")
            response = self.client.post(
                'api/v1/auth/signin',
                content_type='application/json',
                data=json.dumps(dict(email="new_user@gmail.com", password="000123"))
            )

            self.assertEqual(response.status_code, 401)
