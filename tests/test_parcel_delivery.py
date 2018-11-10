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

