from app.models import DataModel
from werkzeug.security import generate_password_hash, check_password_hash

db_connect = DataModel()
cursor = db_connect.cursor
dictcur = db_connect.dict_cursor


def register_new_user(data):
    """registers a new user"""
    query = "INSERT INTO users(username, email, password, role) \
        VALUES('{0}', '{1}', '{2}', '{3}')".format(
            data['username'],
            data['email'],
            generate_password_hash(data['password']),
            "user"
        )
    cursor.execute(query)


def update_user_account(data, email):
    """update user information"""
    query = "UPDATE users SET username='{0}', password='{1}', role='{2}' WHERE email='{3}'".format(
            data['username'],
            generate_password_hash(data['password']),
            data['role'],
            email
        )
    cursor.execute(query)


def delete_user_account(email):
    """delete a user account"""
    query = "DELETE FROM users WHERE email='{0}'".format(email)
    cursor.execute(query)

def get_all_users():
    query = "SELECT * FROM users"
    dictcur.execute(query)
    users = dictcur.fetchall()

    return users

