# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import ipaddress
import argparse
import subprocess
def ping_ip_addresses(ips):
    reach, unreach = [], []
    for ip in ips:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            unreach.append(ip)
            continue
        png = subprocess.run(['ping', '-c', '2', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if png.returncode:
            unreach.append(ip)
        else:
            reach.append(ip)
    return reach, unreach
parser=argparse.ArgumentParser(description='Ping script')
parser.add_argument('ips', nargs='*', action='store', help='list of ip addresses')
args=parser.parse_args()
if  __name__ == '__main__':
	print(ping_ip_addresses(args.ips))

