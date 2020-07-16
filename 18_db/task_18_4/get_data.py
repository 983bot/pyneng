# -*- coding: utf-8 -*-import sqlite3
import sqlite3
import argparse
from tabulate import tabulate
from sys import argv
def read_data_from_db(parameter= None, value=None):
    connect=sqlite3.connect('/home/vlaz01/tools/pyneng/18_db/task_18_3/dhcp_snooping.db')
    cursor=connect.cursor()
    nameslist=[ 'mac', 'ip', 'vlan', 'interface', 'switch', 'active']
    if parameter==None and value == None:
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
    elif parameter!=None and value != None:
        if any(item in parameter for item in nameslist):
            query = f'select * from dhcp where {parameter} like "{value}" and active == 1'
            active = cursor.execute(query).fetchall()
            query = f'select * from dhcp where {parameter} like "{value}" and active == 0'
            pasive = cursor.execute(query).fetchall()
            print(f"entries from DB where {argv[1]} equals {argv[2]}")
            print("Active entries")
            print(tabulate(active))
            if pasive:
                print("Inactive entries")
                print(tabulate(pasive))
        else:
            print('available parameter list is:\nmac, ip, vlan, interface, switch')
            return
    else:
        print('need 0 or 2 parameters')
#parser = argparse.ArgumentParser(description='Getting data from dhcp_snooping DB')
#parser.add_argument('-cn', action='store', dest='columnname', default=None, choices=['mac', 'ip', 'vlan', 'interface', 'switch' ], help='table column name')
#parser.add_argument('-cv', action='store', dest='columnvalue', default=None, help='parameter value')
#args = parser.parse_args()
if __name__ =='__main__':
    if len(argv) == 1:
        read_data_from_db()
    elif len(argv) == 3:
        read_data_from_db(argv[1], argv[2])
    else:
        print('need 0 or 2 parameters')
