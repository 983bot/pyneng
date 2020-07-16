# -*- coding: utf-8 -*-import sqlite3
import sqlite3
import argparse
from tabulate import tabulate
from sys import argv
def read_data_from_db(parameter= None, value=None):
    connect=sqlite3.connect('/home/vlaz01/tools/pyneng/18_db/task_18_1/dhcp_snooping.db')
    cursor=connect.cursor()
    nameslist=[ 'mac', 'ip', 'vlan', 'interface', 'switch']
    if parameter==None and value == None:
        query = f'select * from dhcp'
        print("There are such entries in the DB")
    elif parameter!=None and value != None:
        if any(item in parameter for item in nameslist):
            query = f'select * from dhcp where {parameter} like "{value}"'
            print(f"entries from DB where {argv[1]} equals {argv[2]}")
        else:
            print('available parameter list is:\nmac, ip, vlan, interface, switch')
            return
    else:
        return 'need 0 or 2 parameters'
    cursor.execute(query)
    return cursor.fetchall()
#parser = argparse.ArgumentParser(description='Getting data from dhcp_snooping DB')
#parser.add_argument('-cn', action='store', dest='columnname', default=None, choices=['mac', 'ip', 'vlan', 'interface', 'switch' ], help='table column name')
#parser.add_argument('-cv', action='store', dest='columnvalue', default=None, help='parameter value')
#args = parser.parse_args()
if __name__ =='__main__':
    if len(argv) == 1:
        print(tabulate(read_data_from_db()))
    elif len(argv) == 3:
        print(tabulate(read_data_from_db(argv[1], argv[2])))
    else:
        print('need 0 or 2 parameters')
