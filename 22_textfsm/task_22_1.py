# -*- coding: utf-8 -*-
"""
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

"""
import sys
import textfsm
from tabulate import tabulate
from pprint import pprint
ip_int='''
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   unassigned      YES NVRAM  up                    up      
GigabitEthernet0/0/1   unassigned      YES NVRAM  up                    up      
GigabitEthernet0/0/2   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0       unassigned      YES NVRAM  administratively down down    
Loopback0              10.20.12.251    YES NVRAM  up                    up      
Port-channel1          unassigned      YES unset  up                    up      
Port-channel1.501      10.20.255.10    YES NVRAM  up                    up      
Port-channel1.511      128.0.173.201   YES NVRAM  up                    up      
Tunnel1                10.255.20.20    YES NVRAM  up                    up      
Tunnel2                10.255.11.20    YES NVRAM  up                    up 
'''
def parse_command_output(template, command_output):
    result=[0]
    with open(template) as templ:
        table = textfsm.TextFSM(templ)
        header=table.header
        pars_table=table.ParseText(command_output)
    result[0]=header
    result.extend(pars_table)
    return result
if __name__ == "__main__":
    pprint(parse_command_output("templates/sh_ip_int_br.template", ip_int))
 
