from tests.base import BaseTestCase
import json
import pytest

class TestParcelDeliveryOrder(BaseTestCase):
    # @pytest.mark.skip(reason="test later")
    def test_user_can_create_a_parcel_delivery_order(self):
        """
        Test that a user can create a delivery parcel order
        :return:
        """
        with self.client:
            token = self.get_token("arnold","arnold@gmail.com","000000", "user")
            response = self.create_new_parcel_delivery_order(
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni",
                token
                )
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'parcel delivery order successfully created')
            self.assertEqual(response.status_code, 201)

    # @pytest.mark.skip(reason="test later")
    def test_admin_can_not_create_a_parcel_delivery_order(self):
        """
        Test that an admin can not create a delivery parcel order
        :return:
        """
        with self.client:
            token = self.get_token("admin","admin@gmail.com","000000", "admin")
            response = self.create_new_parcel_delivery_order(
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni",
                token
                )
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'only users are allowed to create parcels')
            self.assertEqual(response.status_code, 401)

    # @pytest.mark.skip(reason="test later")
    def test_user_can_not_create_a_parcel_delivery_order_with_in_valid_parameter(self):
        """
        Test that a user can not create a delivery parcel order with in valid parameter
        :return:
        """
        with self.client:
            token = self.get_token("user","user@gmail.com","123456", "user")
            response = self.client.post(
            'api/v1/parcels',
            content_type = 'application/json',
            headers=dict(Authorization='Bearer ' + token),
            data = json.dumps(dict(
                parcel="parcel",
                weight="",
                price="020",
                receiver="receiver",
                pickup_location="pickup_location",
                destination="destination"
                ))
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'value of weight is not valid')
            self.assertEqual(response.status_code, 400)

    # @pytest.mark.skip(reason="test later")
    def test_admin_can_get_all_parcels(self):
        """
        Test that admin can get all delivery orders for all users
        :return:
        """
        with self.client:
            token = self.get_token("admin","admin@gmail.com","000000", "admin")
            response = self.client.get(
                'api/v1/parcels',
                 headers=dict(Authorization='Bearer ' + token),
            )

            self.assertEqual(response.status_code, 200)

    # @pytest.mark.skip(reason="test later")
    def test_user_can_get_all_parcels_belonging_to_them(self):
        """
        Test that user can get parcels that belong to them
        :return:
        """
        with self.client:
            token = self.get_token("new_user","new_user@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
                "Big money",
                '3',
                "950",
                "Diana",
                "Wandegeya",
                "Kikoni",
                token
                )
            response = self.client.get(
                'api/v1/parcels',
                headers=dict(Authorization='Bearer ' + token),
            )

            self.assertEqual(response.status_code, 200)

    # @pytest.mark.skip(reason="test later")
    def test_user_can_get_specific_parcel(self):
        """
        Test that user can get a specific parcel
        :return:
        """
        token = self.get_token("new_user","new_user@gmail.com", "00000", "user")
        self.create_new_parcel_delivery_order(
            "Big money",
            '3',
            "950",
            "Diana",
            "Wandegeya",
            "Kikoni",
            token,
            )
        response = self.client.get(
            'api/v1/parcels/1',
            headers=dict(Authorization='Bearer ' + token),
        )

        self.assertEqual(response.status_code, 200)


    @pytest.mark.skip(reason="test later")
    def test_user_can_not_get_a_parcel_when_none_is_created_parcel_orders(self):
        """
        Test that a user can not get a specific parcel when they have not created one
        :return:
        """
        with self.client:
            token = self.get_token("new_user","new_user@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
            "Big money",
            '3',
            "950",
            "Diana",
            "Wandegeya",
            "Kikoni",
            token,
            )
            response = self.client.get(
                'api/v1/parcels/cancel',
                headers=dict(Authorization='Bearer ' + token),
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['message'] == 'user does not have any orders')
            self.assertEqual(response.status_code, 400)

    # @pytest.mark.skip(reason="test later")
    def test_get_a_parcel_that_does_not_exist(self):
        """
        Test that a user can not get parcel when it does not exist or wrong id is provided
        :return:
        """
        with self.client:
            token = self.get_token("new_user","new_user@gmail.com", "00000", "user")
            response = self.client.get(
                'api/v1/parcels/7',
                headers=dict(Authorization='Bearer ' + token),
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'parcel order does not exist')
            self.assertEqual(response.status_code, 400)

    # @pytest.mark.skip(reason="test later")
    def test_user_can_cancel_a_parcel_delivery_order(self):
        """
        Test that a user can cancel a delivery parcel order
        :return:
        """
        with self.client:
            token = self.get_token("new_user","new_user@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
            "Big money",
            '3',
            "950",
            "Diana",
            "Wandegeya",
            "Kikoni",
            token,
            )
            response = self.client.put(
                'api/v1/parcels/cancel',
                data = json.dumps(dict(
                id=1
                )),
                content_type='application/json',
                headers=dict(Authorization='Bearer ' + token)
            )
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'parcel delivery has been cancelled')
            self.assertEqual(response.status_code, 201)

    @pytest.mark.skip(reason="test later")
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
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'parcel has been successfully updated')
            self.assertEqual(response.status_code, 201)

    @pytest.mark.skip(reason="test later")
    def test_user_can_change_destination_of_a_parcel_delivery_order_that_does_not_exist(self):
        """
        Test that a user can change destination of a delivery parcel order which does not exist
        :return:
        """
        with self.client:
            self.register_new_user("julie","julie2@gmail.com", "00000", "user")
            self.create_new_parcel_delivery_order(
                "julie2@gmail.com",
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
                data = json.dumps(dict(email="julie2@gmail.com",id="225", destinaton="new location"))
                )
            data = json.loads(response.data.decode())

            self.assertTrue(data['message'] == 'parcel order with id 225 does not exist')
            self.assertEqual(response.status_code, 404)
