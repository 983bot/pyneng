# -*- coding: utf-8 -*-
import sqlite3
import re
import os
from tabulate import tabulate
import yaml
from datetime import timedelta, datetime
def create_db(dbname, schema):
    db_exists = os.path.exists(dbname)
    if db_exists:
        print(f"Database {dbname} already exists")
        return 1
    else:
        conn=sqlite3.connect(dbname)
        with open(schema) as f:
            schema=f.read()
            conn.executescript(schema)
def connect_db(dbname):
    db_exists = os.path.exists(dbname)
    if db_exists:
        conn=sqlite3.connect(dbname)
        return conn
    else:
        print(f"Database {dbname} does not exist")
        return 1
def write_to_db(cnt, command, data=None):
    cursor=cnt.cursor()
    try:
        if data:
            cursor.execute(command, data)
        else:
            cursor.execute(command)
        return cursor
    except sqlite3.IntegrityError:
        return 1
def add_data_switches(dbfile, filelist):
    for files in filelist:
        switchinfo_exists=os.path.exists(files)
        if not switchinfo_exists:
            print(f"file {files} not found")
            return
        conn=connect_db(dbfile)
        if conn != 1:
            with open(files) as f:
                switch_dict=yaml.safe_load(f)
                query = "INSERT into switches values (?, ?)"
                result=[]
                for key in switch_dict:
                    for items in switch_dict[key].items():
                        result.append(items)
                for line in result:
                    if write_to_db(conn, query, line) !=1:
                        print(f'line added to switches table "{line[0]}     {line[1]}"')
                    else:
                        print(f"{line[0]} info already present in the table")
            conn.commit()
        else:
            print(f"file {dbfile} not found")
def add_data(dbfile, filelist):
    regexp = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result =[]
    conn = connect_db(dbfile)
    for files in filelist:
        device=re.search('(\S+?)_\S+',os.path.basename(files)).group(1)
        with open(files) as f:
            for line in f:
                match=regexp.search(line)
                if match:
                    resstring = list(match.group(1, 2, 3, 4))
                    resstring.append(device)
                    result.append(tuple(resstring))
            query = f"update dhcp set active = ? where switch like '{device}'"
            write_to_db(conn, query, '0')
    insert='insert into dhcp values (?, ?, ?, ?, ?, 1, datetime("now"))'
    update = "update dhcp set ip = ?, vlan = ?, interface = ?, switch = ?, active = 1, last_active = datetime('now') where mac = ?"
    for line in result:
        if write_to_db(conn, insert, line) != 1:
            print(f"string added to the dhcp table: {line}")
        else:
            tmp = list(line)[1::]
            tmp.append(line[0])
            line = tuple(tmp)
            print(f"updating values for mac {line[-1]}. New values: {line[0:-1:]}")
            write_to_db(conn, update, line)
###################Remove old Records##################################
    now = datetime.today().replace(microsecond=0)
    week_ago = now - timedelta(days=7)
    print (f"removing old records (before {week_ago})")
    query = f"delete from dhcp where datetime(last_active) <= datetime('{week_ago}') and active == 0"
    write_to_db(conn, query)
    conn.commit()
def get_data(dbfile, key=None, value=None):
    conn = connect_db(dbfile)
    cursor=conn.cursor()
    nameslist=[ 'mac', 'ip', 'vlan', 'interface', 'switch', 'active']
    if key and value:
        if any(item in key for item in nameslist):
            query = f'select * from dhcp where {key} like "{value}" and active == 1'
            active = cursor.execute(query).fetchall()
            query = f'select * from dhcp where {key} like "{value}" and active == 0'
            pasive = cursor.execute(query).fetchall()
            print(f"entries from DB where {key} equals {value}")
            print("Active entries")
            print(tabulate(active))
            if pasive:
                    print("Inactive entries")
                    print(tabulate(pasive))
        else:
            print(f'available parameter list is:\n{nameslist}')
            return
    else:
        print('need 0 or 2 parameters')
def get_all_data(dbfile):
    conn = connect_db(dbfile)
    cursor=conn.cursor()
    qact = f'select * from dhcp where active == 1'
    active = cursor.execute(qact).fetchall()
    qpas = f'select * from dhcp where active == 0'
    pasive = cursor.execute(qpas).fetchall()
    print("dhcp table entries")
    print("Active entries in the DB")
    print(tabulate(active))
    if pasive:
        print("Inactive entries in the DB")
        print(tabulate(pasive))
