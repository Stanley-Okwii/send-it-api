import unittest
from tests.base import BaseTestCase
import json

class TestParcelDeliveryOrder(BaseTestCase):
    def test_user_can_create_a_parcel_delivery_order(self):
        """
        Test that a user can create a delivery parcel order
        :return:
        """
        with self.client:
            self.register_new_user("user","user2@gmail.com", "00000")
            response = self.create_new_parcel_delivery_order(
                "user2@gmail.com",
                "045",
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni"
                )

            self.assertEqual(response.status_code, 201)

    def test_admin_can_get_all_parcels(self):
        """
        Test that admin can get all delivery orders for all users
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/parcels'
            )

            self.assertEqual(response.status_code, 200)

    def test_user_can_get_all_parcels_belonging_to_them(self):
        """
        Test that user can get parcels that belong to them
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/parcels',
                data = json.dumps(dict(email="stanley@gmail.com"))
            )

            self.assertEqual(response.status_code, 200)
