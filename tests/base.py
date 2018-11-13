from app import api
from flask_testing import TestCase
import json


class BaseTestCase(TestCase):
    def create_app(self):
        """
        Create an instance of the app
        :return:
        """
        return api

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def register_new_user(self, name, email, password):
        """
        Helper method for creating a user with test data
        :return:
        """
        return self.client.post(
            'api/v1/user',
            content_type='application/json',
            data=json.dumps(dict(name=name, email=email, password=password))
            )

    def create_new_parcel_delivery_order(self, email,_id,parcel,weight,price,receiver,pickup_location,destination):
        """
        Helper method for registering a user with test data
        :return:
        """
        return self.client.post(
            'api/v1/parcels',
            content_type = 'application/json',
            data = json.dumps(dict(
                email=email,
                id=_id,
                parcel=parcel,
                weight=weight,
                price=price,
                receiver=receiver,
                pickup_location=pickup_location,
                destination=destination
                ))
            )
