# -*- coding: utf-8 -*-import sqlite3
import sqlite3
import yaml
from create_db import connect_db
from create_db import write_to_db
from create_db import writescriptto_db
import os
import re
from datetime import timedelta, datetime
def add_switches_info(source):
    with open(source) as f:
        switch_dict=yaml.safe_load(f)
        query = "INSERT into switches values (?, ?)"
        result=[]
        for key in switch_dict:
            for items in switch_dict[key].items():
                result.append(items)
    conn = connect_db("dhcp_snooping.db")
    for line in result:
        if not write_to_db(conn, query, line):
            print(f'line added to switches table "{line[0]}     {line[1]}"')
        else:
            print(f"{line[0]} info already present in the table")
    conn.commit()
dhcplist=['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
def add_dhcp_info(filelist):
    regexp = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result =[]
    conn = connect_db("dhcp_snooping.db")
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
        if not write_to_db(conn, insert, line):
            print(f"string added to the dhcp table: {line}")
        else:
            tmp = list(line)[1::]
            tmp.append(line[0])
            line = tuple(tmp)
            print(f"updating values for mac {line[-1]}. New values: {line[0:-1:]}")
            write_to_db(conn, update, line)
    conn.commit()
def remove_old_records():
    now = datetime.today().replace(microsecond=0)
    week_ago = now - timedelta(days=7)
    conn = connect_db("dhcp_snooping.db")
    print (f"removing old records (before {week_ago})")
    query = f"delete from dhcp where datetime(last_active) <= datetime('{week_ago}') and active == 0"
    writescriptto_db(conn, query)
    conn.commit()
if __name__ == "__main__":
    add_switches_info('switches.yml')
    add_dhcp_info(dhcplist)
    remove_old_records()
