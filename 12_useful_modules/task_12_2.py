# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
import argparse
def convert_ranges_to_ip_list(iplist):
    result=[]
    for ip in iplist:
        if "-" in ip:
            try:
                firstip=ipaddress.ip_address(ip.split("-")[0])
                try:
                    lastip=ipaddress.ip_address(ip.split("-")[1])
                    while firstip <= lastip:
                        result.append(str(firstip))
                        firstip +=1
                except ValueError:
                    lastdigit=ip.split("-")[1]
                    firstdigits=[str(firstip).split(".")[i] for i in range(3)]
                    lastip=ipaddress.ip_address("{d1}.{d2}.{d3}.{d4}".format(d1=firstdigits[0], d2=firstdigits[1], d3 = firstdigits[2], d4=lastdigit))
                    while firstip <= lastip:
                        result.append(str(firstip))
                        firstip +=1
            except ValueError:
                continue
        else:
            try:
                firstip=ipaddress.ip_address(ip)
                result.append(ip)
            except ValueError:
                continue
    return result
parser = argparse.ArgumentParser(description='script for ip list creation')
parser.add_argument("IP_list", nargs='+', help="list of IP addresses in form: 8.8.4.4, 1.1.1.1-3', 172.21.41.128-172.21.41.132")
arg=parser.parse_args()
if __name__ == '__main__':
    print(convert_ranges_to_ip_list(arg.IP_list))
