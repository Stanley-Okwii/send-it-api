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

    def test_user_can_get_specific_parcel_that_belongs_to_them(self):
        """
        Test that user can get a specific parcel that belong to them
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/parcels',
                data = json.dumps(dict(email="stanley@gmail.com", id="001"))
            )

            self.assertEqual(response.status_code, 200)

    def test_get_a_parcel_for_user_without_parcel_orders(self):
        """
        Test that a user can not get a specific parcel when they have not created one
        :return:
        """
        with self.client:
            self.register_new_user("noparcel","noparcel@gmail.com","234012")
            response = self.client.get(
                'api/v1/parcels?email=noparcel@gmail.com'
            )

            self.assertEqual(response.status_code, 404)

    def test_get_a_parcel_that_does_not_exist(self):
        """
        Test that a user can not get parcel when it does not exist or wrong id is provided
        :return:
        """
        with self.client:
            self.register_new_user("me","me@me.you","90")
            response = self.client.get(
                'api/v1/parcels?email=stanley@gmail.com&id=07'
            )

            self.assertEqual(response.status_code, 404)

