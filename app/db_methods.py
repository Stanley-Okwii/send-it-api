from app.models import DataModel
# from werkzeug.security import generate_password_hash, check_password_hash

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
    query = "DELETE FROM users WHERE email='{0}'".format(email)
    cursor.execute(query)


def get_all_users():
    """get all user accounts"""
    query = "SELECT * FROM users"
    dictcur.execute(query)
    users = dictcur.fetchall()

    return users


def create_parcel_order(data):
    """creates a new parcel delivery order"""
    query = "INSERT INTO parcel_order(parcel, weight, \
     price, receiver, destination, current_location, pickup_location, email) \
        VALUES('{0}', '{1}', '{2}', '{3}','{4}', '{5}', '{6}', '{7}')".format(
            data['parcel'],
            data['weight'],
            data['price'],
            data['receiver'],
            data['destination'],
            data['pickup_location'],
            data['current_location'],
            data['email']
        )
    cursor.execute(query)


def update_parcel_order(data):
    """updates an existing parcel delivery order"""
    query = "UPDATE parcel_order SET current_location='{0}', pickup_location='{1}', \
        status='{2}', destination='{3}' WHERE order_id='{4}'".format(
            data['current_location'],
            data['pickup_location'],
            data['status'],
            data['destination'],
            data['order_id']
        )
    cursor.execute(query)


def get_all_parcel_orders():
    query = "SELECT * FROM parcel_order"
    dictcur.execute(query)
    parcel_orders = dictcur.fetchall()

    return parcel_orders
