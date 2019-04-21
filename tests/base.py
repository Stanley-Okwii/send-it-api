from app import api
from app.models import DataModel
from flask_testing import TestCase
import json

db = DataModel()


class BaseTestCase(TestCase):
    def create_app(self):
        """
        Create an instance of the app
        :return:
        """
        return api

    def setUp(self):
        db.create_user_table()
        db.create_parcel_order_table()

    def tearDown(self):
        db.drop_tables()

    def register_new_user(self, name, email, password, role):
        """
        Helper method for creating a user with test data
        :return:
        """
        return self.client.post(
            'api/v1/user',
            content_type='application/json',
            data=json.dumps(dict(
                name=name,
                email=email,
                password=password,
                role=role))
            )

    def create_new_parcel_delivery_order(self, parcel, weight, price, receiver,
                                         pickup_location, destination, token):
        """
        Helper method for creating a parcel
        :return:
        """
        return self.client.post(
            'api/v1/parcels',
            content_type='application/json',
            headers=dict(Authorization='Bearer ' + token),
            data=json.dumps(dict(
                parcel=parcel,
                weight=weight,
                price=price,
                receiver=receiver,
                pickup_location=pickup_location,
                destination=destination
                ))
            )

    def get_token(self, name, email, password, role):
        """
        Get a user token
        :return:
        """
        self.client.post(
            'api/v1/user',
            content_type='application/json',
            data=json.dumps(dict(
                name=name,
                email=email,
                password=password,
                role=role))
            )
        response = self.client.post(
            'api/v1/auth/signin',
            content_type='application/json',
            data=json.dumps(dict(
                email=email,
                password=password
            )))
        return json.loads(response.data.decode())['user_token']
