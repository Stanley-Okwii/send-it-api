from app.models import DataModel
from werkzeug.security import generate_password_hash, check_password_hash

db_connect = DataModel()
cursor = db_connect.cursor
dictcur = db_connect.dict_cursor


def register_new_user(self, data):
    """registers a new user"""
    query = "INSERT INTO users(username, email, password, role) \
        VALUES('{0}', '{1}', '{2}', '{3}')".format(
            data['username'],
            data['email'],
            generate_password_hash(data['password']),
            "user"
        )
    cursor.execute(query)
    return data


# def check_password(self, data, db_data):
#     return check_password_hash(data, db_data)

register_new_user(data = {
    "name": "stanley",
    "email": "stanley@gmail.com",
    "password": "123456"
})
