from app.models import DataModel
from datetime import datetime
from pytz import timezone

db_connect = DataModel()
cursor = db_connect.cursor
dictcur = db_connect.dict_cursor


def register_new_user(data):
    """registers a new user"""
    query = "INSERT INTO users(username, email, password, role) \
        VALUES('{0}', '{1}', '{2}', '{3}')".format(
            data['username'],
            data['email'],
            data['password'],
            data['role']
        )
    cursor.execute(query)


def update_user_account(data, email):
    """update user information"""
    query = "UPDATE users SET username='{0}', password='{1}' WHERE email='{2}'".format(
            data['username'],
            data['password'],
            email
        )
    cursor.execute(query)


def update_user_role_to_admin(data):
    """update user information"""
    query = "UPDATE users SET role='{0}' WHERE email='{1}'".format(
            data['role'],
            data['email']
        )
    cursor.execute(query)


def delete_user_account(email):
    """delete a user account"""
    backup_parcels = "INSERT INTO parcel_order_archive(order_id, parcel, weight, \
     price, receiver, destination, current_location, pickup_location, \
    email, created_at, status) \
    SELECT order_id, parcel, weight, price, receiver, destination, \
    current_location, pickup_location, email, created_at, status \
    FROM parcel_order WHERE email='%s'; \
    DELETE FROM users WHERE email='%s';" % (email, email)
    cursor.execute(backup_parcels)


def get_all_users():
    """get all user accounts"""
    query = "SELECT * FROM users"
    dictcur.execute(query)
    users = dictcur.fetchall()

    return users


def create_parcel_order(data):
    """creates a new parcel delivery order"""
    uganda_time = timezone('Africa/Kampala')
    created_at = datetime.now(uganda_time).strftime("%Y-%m-%d %I:%M:%S %p")
    query = "INSERT INTO parcel_order(parcel, weight, \
     price, receiver, destination, current_location, \
      pickup_location, email, created_at, status) \
        VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s')" % (
            data['parcel'],
            data['weight'],
            data['price'],
            data['receiver'],
            data['destination'],
            data['pickup_location'],
            data['current_location'],
            data['email'],
            created_at,
            'pending'
        )
    cursor.execute(query)


def update_parcel_order(data):
    """updates an existing parcel delivery order"""
    query = "UPDATE parcel_order SET current_location='%s', pickup_location='%s', \
        status='%s', destination='%s' WHERE order_id='%i'" % (
            data['current_location'],
            data['pickup_location'],
            data['status'],
            data['destination'],
            data['order_id']
        )
    cursor.execute(query)


def get_all_parcel_orders(database_table):
    query = "SELECT * FROM %s" % (database_table)
    dictcur.execute(query)
    parcel_orders = dictcur.fetchall()

    return parcel_orders
