# -*- coding: utf-8 -*-import sqlite3
import sqlite3
import os
dbfilename = 'dhcp_snooping.db'
def connect_db(dbname):
    db_exists = os.path.exists(dbname)
    conn=sqlite3.connect(dbname)
    if db_exists:
        print(f'connecting to database {dbname}')
        print('-'*60)
        return conn
    else:
        with open('dhcp_snooping_schema.sql') as f:
            schema=f.read()
            print('creating database')
            print('-'*60)
            conn.executescript(schema)
        return conn
def write_to_db(dbname, command, data):
    print(f'adding data to {dbname}')
    connect = connect_db(dbname)
    cursor=connect.cursor()
    for line in data:
        try:
            print(f'adding data "{line}" to database')
            cursor.execute(command, line)
        except sqlite3.IntegrityError:
            print(f"data '{line}' already present in the database")
    connect.commit()

if __name__ == "__main__":
    connect_db('dhcp_snooping.db')
