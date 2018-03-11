#!/usr/bin/python
import psycopg2

class Database():
    def __init__(self):
        self.conn = None

        # read connection parameters
        params = {
            "host": "localhost",
            "database": "COMMANDER",
            "user": "GRUBEMAN",
            'password': "Noelle1983",
            "port": "2708"
        }

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        self.conn = psycopg2.connect(**params)

        # create a cursor
        self.cur = self.conn.cursor()

    def get_version(self):
        # execute a statement
        print('PostgreSQL database version:')
        self.cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = self.cur.fetchone()
        print(db_version)

    def __del__(self):
        self.close()

    def close(self):
        # close the communication with the PostgreSQL
        self.cur.close()

        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    def query(self,stmt):
        self.cur.execute(stmt)
        self.conn.commit()

if __name__ == '__main__':
    db = Database()
    db.get_version()
    stmt = "INSERT INTO play_planet(name, starsystem_id) VALUES ('Terre',1);"
    db.query(stmt)
    db.close()