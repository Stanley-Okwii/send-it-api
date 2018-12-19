from tests.base import BaseTestCase
import json
import pytest


class TestArchiveParcels(BaseTestCase):

    def test_admin_can_view_archived_orders(self):
        """
        Test that admin can get parcels that belong to all deleted users
        :return:
        """
        with self.client:
            admin_token = self.get_token("admin", "admin@gmail.com",
                                         "000000", "admin")
            user_token = self.get_token("user", "user@gmail.com",
                                        "000000", "user")
            self.create_new_parcel_delivery_order(
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni",
                user_token
                )
            self.create_new_parcel_delivery_order(
                "Big Pig",
                '3',
                "650",
                "Diana",
                "Wandegeya",
                "Kampala",
                user_token
                )
            response = self.client.delete(
                'api/v1/user',
                content_type='application/json',
                headers=dict(Authorization='Bearer ' + admin_token),
                data=json.dumps(dict(
                    email="user@gmail.com"
                    ))
            )
            response = self.client.get(
                'api/v1/archive',
                headers=dict(Authorization='Bearer ' + admin_token),
            )

            self.assertEqual(response.status_code, 200)

    def test_user_can_not_view_archived_orders(self):
        """
        Test that user can not get parcels that belong to all deleted users
        :return:
        """
        with self.client:
            admin_token = self.get_token("admin", "admin@gmail.com",
                                         "000000", "admin")
            user_token = self.get_token("user", "user@gmail.com",
                                        "000000", "user")
            self.create_new_parcel_delivery_order(
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni",
                user_token
                )
            self.create_new_parcel_delivery_order(
                "Big Pig",
                '3',
                "650",
                "Diana",
                "Wandegeya",
                "Kampala",
                user_token
                )
            response = self.client.delete(
                'api/v1/user',
                content_type='application/json',
                headers=dict(Authorization='Bearer ' + admin_token),
                data=json.dumps(dict(
                    email="user@gmail.com"
                    ))
            )
            response = self.client.get(
                'api/v1/archive',
                headers=dict(Authorization='Bearer ' + user_token),
            )

            self.assertEqual(response.status_code, 404)
