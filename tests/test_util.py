from tests.base import BaseTestCase
import json
import pytest

class TestUtil(BaseTestCase):
    def test_abort_sign_in_if_user_does_not_exist(self):
        """
        Test a user can create an account
        :return:
        """
        with self.client:
            self.register_new_user("ajori","ajori@gmail.com","000000", "user")
            response = self.client.post(
                'api/v1/auth/signin',
                content_type='application/json',
                data=json.dumps(dict(email="user2@gmail.com", password="00000"))
            )
            data = response.get_json()

            self.assertTrue(data['message'] == "user doesn't exist")
            self.assertEqual(response.status_code, 400)
