import datetime

from database.core import Connection

class Accounts:
    
    ''' Object from db. Accounts.'''
    id: int
    number: str
    owner_id: int
    balance: float
    type: str

    @staticmethod 
    def create(
    conn: Connection,
    number: str,
    owner_id: int,
    balance: float,
    type: str
    ):
        with conn.cursor() as cur:
            cur.execute(f'''
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type)
                VALUES(
                    '{number}',
                    '{owner_id}',
                    '{balance}',
                    '{type}')
                '''
            )

    @staticmethod
    def all(
        conn:Connection
    ):
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM accounts
                """
            )
            print(cur.fetchall())
            return cur.fetchall()