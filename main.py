#Local
from database.core import Connection

import datetime

#Python
from decouple import config 

from database.models.users import User
from database.models.accounts import Accounts
from database.models.cards import Card


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)


if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     first_name='pob',
    #     last_name='friday',
    #     date_of_birth=datetime.datetime(
    #     year=1998,
    #     month=5,
    #     day=15),
    #     iin='980115123234',
    #     phone_number= '7719411034'
    # )
    # Card.create(
    #     conn=my_connection.conn,
    #     number='1243985645231264',
    #     account_id=3,
    #     cvv=482,
    #     date_end=datetime.datetime(year=2005,month=1,day=11),
    #     is_active=True,
    #     pin=1090
    # )
    # Accounts.create(
    #     conn=my_connection.conn,
    #     number='12533254895712834912',
    #     owner_id=19,
    #     balance=100000.0,
    #     type='USD'
    # )
    # User.all(
    #     conn=my_connection.conn
    # )
    # Card.all(
    #     conn=my_connection.conn
    # )
    # Accounts.all(
    #     conn=my_connection.conn
    # )
    # User.filtr(
    #     conn=my_connection.conn
    # )
    Card.filtr(
        conn=my_connection.conn
    )