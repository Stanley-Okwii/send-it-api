from tests.base import BaseTestCase
import json
import pytest

class TestParcelDeliveryOrder(BaseTestCase):
    def test_user_can_create_a_parcel_delivery_order(self):
        """
        Test that a user can create a delivery parcel order
        :return:
        """
        with self.client:
            self.register_new_user("user","user2@gmail.com", "00000", "user")
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
                'api/v1/users/admin@gmail.com/parcels'
            )

            self.assertEqual(response.status_code, 200)

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_user_can_get_all_parcels_belonging_to_them(self):
        """
        Test that user can get parcels that belong to them
        :return:
        """
        with self.client:
            self.register_new_user("new_user","new_user@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
                "new_user@gmail.com",
                "045",
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni"
                )
            response = self.client.get(
                'api/v1/users/stanley@gmail.com/parcels'
            )

            self.assertEqual(response.status_code, 200)

    def test_user_can_get_specific_parcel(self):
        """
        Test that user can get a specific parcel
        :return:
        """
        with self.client:
            response = self.client.get(
                'api/v1/parcels/009'
            )

            self.assertEqual(response.status_code, 200)

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_user_can_not_get_a_parcel_for_user_without_parcel_orders(self):
        """
        Test that a user can not get a specific parcel when they have not created one
        :return:
        """
        with self.client:
            self.register_new_user("no_parcel","no_parcel@gmail.com","234012", "user")
            response = self.client.get(
                'api/v1/users/no_parcel@gmail.com/parcels'
            )

            self.assertEqual(response.status_code, 404)

    def test_get_a_parcel_that_does_not_exist(self):
        """
        Test that a user can not get parcel when it does not exist or wrong id is provided
        :return:
        """
        with self.client:
            self.register_new_user("new_user","new_user@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
                "new_user@gmail.com",
                "045",
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni"
                )
            response = self.client.get(
                'api/v1/parcels/564'
            )

            self.assertEqual(response.status_code, 404)

    def test_user_can_change_destination_of_a_parcel_delivery_order(self):
        """
        Test that a user can change destination of a delivery parcel order
        :return:
        """
        with self.client:
            self.register_new_user("julie","julie@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
                "julie@gmail.com",
                "025",
                "veg pizza",
                '3',
                "95210",
                "Oryx",
                "Wandegeya",
                "Kikoni"
                )
            response = self.client.put(
                'api/v1/parcels',
                content_type= "application/json",
                data = json.dumps(dict(email="julie@gmail.com",id="025", destinaton="new location"))
                )

            self.assertEqual(response.status_code, 201)

    def test_admin_can_change_current_location_and_status_of_a_parcel_delivery_order(self):
        """
        Test that a admin can change current location and status of a delivery parcel order
        :return:
        """
        with self.client:
            self.register_new_user("julie","julie@gmail.com", "00000", "admin")
            self.create_new_parcel_delivery_order(
                "julie@gmail.com",
                "025",
                "veg pizza",
                '3',
                "95210",
                "Oryx",
                "Wandegeya",
                "Kikoni"
                )
            response = self.client.put(
                'api/v1/parcels',
                content_type= "application/json",
                data = json.dumps(dict(email="julie@gmail.com",id="025", current_location="new location", status="delivered"))
                )

            self.assertEqual(response.status_code, 201)
