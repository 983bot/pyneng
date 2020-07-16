# -*- coding: utf-8 -*-import sqlite3
import sqlite3
import yaml
from create_db import connect_db
from create_db import write_to_db
import os
import re
def add_switches_info(source):
    with open(source) as f:
        switch_dict=yaml.safe_load(f)
        query = "INSERT into switches values (?, ?)"
        result=[]
        for key in switch_dict:
            for items in switch_dict[key].items():
                result.append(items)
    print(result)
    print('adding data to switches table')
    write_to_db('dhcp_snooping.db', query, result)
dhcplist=['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
def add_dhcp_info(filelist):
    regexp = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result =[]
    for files in filelist:
        device=re.search('(\S+?)_\S+',files).group(1)
        with open(files) as f:
            for line in f:
                match=regexp.search(line)
                if match:
                    resstring = list(match.group(1, 2, 3, 4))
                    resstring.append(device)
                    result.append(tuple(resstring))
    query='insert into dhcp values (?, ?, ?, ?, ?)'
    print('adding data to dhcp table')
    write_to_db('dhcp_snooping.db', query, result)

if __name__ == "__main__":
    add_switches_info('switches.yml')
    add_dhcp_info(dhcplist)
