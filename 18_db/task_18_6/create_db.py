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
def write_to_db(cnt, command, data):
    conn = cnt
    cursor=conn.cursor()
    try:
        cursor.execute(command, data)
        return cursor
    except sqlite3.IntegrityError:
        return 1
def writescriptto_db(cnt, command):
    conn = cnt
    cursor=conn.cursor()
    try:
        cursor.executescript(command)
    except sqlite3.IntegrityError:
        return 1
if __name__ == "__main__":
    connect_db('dhcp_snooping.db')
