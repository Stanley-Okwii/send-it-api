import os
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# load dot env in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__))
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
API_ENVIRONMENT = os.getenv('API_ENV')


class DataModel(object):
    def __init__(self):
        """create instance of a connection instance to sendit database"""
        if API_ENVIRONMENT == 'TESTING':
            self.connection = connect(os.getenv('TESTING'))
        elif API_ENVIRONMENT == 'DEVELOPMENT':
            self.connection = connect(os.getenv('DEVELOPMENT'))
        elif os.getenv('TRAVIS'):
            self.connection = connect(database=os.getenv('TRAVIS_DB'))
        else:
            self.connection = connect(os.getenv('DATABASE_URL'))

        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(
            cursor_factory=RealDictCursor
            )

    def create_user_table(self):
        """create table to store user information"""
        user_table_query = "CREATE TABLE IF NOT EXISTS users (email varchar(100) PRIMARY KEY, \
                            username varchar(50), password varchar(256), \
                            role varchar(15) NOT NULL DEFAULT 'user')"

        self.cursor.execute(user_table_query)

    def create_parcel_order_table(self):
        """creates table to store parcel orders"""

        parcel_order_table_query = "CREATE TABLE IF NOT EXISTS parcel_order(\
        order_id serial PRIMARY KEY, parcel varchar(100), weight integer,\
        price integer, receiver varchar(80), destination varchar(100), \
        current_location varchar(100), pickup_location varchar(100), \
        status varchar(100) NOT NULL DEFAULT 'pending', \
        email varchar(100), \
        FOREIGN KEY (email) REFERENCES users (email) ON DELETE CASCADE)"

        self.cursor.execute(parcel_order_table_query)

    def drop_tables(self):
        """drops/deletes tables"""

        drop_user_table = "DROP TABLE users cascade;"
        drop_parcel_order_table = "DROP TABLE parcel_order cascade;"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_parcel_order_table)
