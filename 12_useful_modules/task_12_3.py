# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""
import argparse
from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list
from task_12_2 import parser
from tabulate import tabulate

def print_ip_table(reachable, unreachable):
    if len(reachable) == len(unreachable):
        pass
    elif len(reachable) < len(unreachable):
        for i in range(len(unreachable)-len(reachable)): reachable.append("")
    else:
        for i in range(len(reachable)-len(unreachable)): unreachable.append("")
    print(tabulate(zip(reachable,unreachable), headers=['Reachable','unreachable']))

arg = parser.parse_args()
print(arg)
pingres = ping_ip_addresses(convert_ranges_to_ip_list(arg.IP_list))
rchbl, unrchbl = pingres
print_ip_table(rchbl, unrchbl)
