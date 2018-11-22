import os
from app.config import app_config
from psycopg2 import connect
from psycopg2.extras import RealDictCursor


class DataModel(object):
    def __init__(self):
        """create instance of a connection instance to sendit database"""
        # if app_config['testing']:
        #     self.connection = connect(app_config['testing'].DATABASE_URL)
        if app_config['development']:
            self.connection = connect(app_config['development'].DATABASE_URL)
        # if app_config['production']:
        #     self.connection = connect(app_config['production'].DATABASE_URL)
        # self.connection = connect(database="sendit_test")

        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(
            cursor_factory=RealDictCursor
            )

    def create_user_table(self):
        """create table to store user information"""
        user_table_query = "CREATE TABLE IF NOT EXISTS users (email varchar(100) PRIMARY KEY, \
        username varchar(50), password varchar(256), role varchar(15) NOT NULL DEFAULT 'user')"

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
