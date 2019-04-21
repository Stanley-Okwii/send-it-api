from tests.base import BaseTestCase
import json


class TestUtil(BaseTestCase):
    def test_abort_if_user_does_not_exist(self):
        """
        Test admin change role of none existing user
        :return:
        """
        with self.client:
            token = self.get_token("admin", "admin@gmail.com",
                                   "000000", "admin")
            response = self.client.put(
                '/api/v1/role',
                data=json.dumps(dict(email="user3@gmail", role="admin")),
                headers=dict(Authorization='Bearer ' + token),
            )
            data = response.get_json()

            # self.assertTrue(data['message'] == "user doesn't exist")
            self.assertEqual(response.status_code, 400)
