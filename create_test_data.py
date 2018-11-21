from app.models import DataModel
from werkzeug.security import generate_password_hash
from app.db_methods import register_new_user, create_parcel_order

db_connect = DataModel()
cursor = db_connect.cursor
dictcur = db_connect.dict_cursor


def create_test_users():
    query = "INSERT INTO users(username, email, password, role) \
        VALUES('{0}', '{1}', '{2}', '{3}'), ('{4}', '{5}', '{6}', '{7}')".format(
            'admin',
            'admin@gmail.com',
            generate_password_hash('123456'),
            "admin",
            'stanley',
            'stanley@gmail.com',
            generate_password_hash('123456'),
            "user"
        )
    cursor.execute(query)

def create_test_parcels():
    parcel= {
            'parcel': 'Oranges',
            'weight': 34,
            'price': 8000,
            'receiver':'Maria',
            'destination':'kireka',
            'pickup_location': 'kampala',
            'current_location': 'Kampala',
            'email': 'stanley@gmail.com'
        }
    create_parcel_order(data=parcel)

create_test_users()
create_test_parcels()
