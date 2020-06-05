# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from sys import argv
def get_int_vlan_map(config_filename=argv[1]):
	""" обрабатывает конфигурационный файл коммутатора
	и возвращает кортеж из двух словарей:
	* словарь портов в режиме access, где ключи номера портов, а значения access VLAN
	* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN
	"""
	f = open(config_filename)
	accessports={}
	trunkports={}
	for line in f:
		mode=""
		if line.startswith("interface FastEthernet"):
			intf = line.split()[-1]
		elif "trunk allowed vlan " in line:
			vlans = line.split()[-1].split(",")
			for i in range(len(vlans)): vlans[i]=int(vlans[i])
			mode = "trunk"
		elif "switchport access vlan " in line:
			vlan = line.split()[-1]
			mode = "access"
		if mode == "access":
			accessports[intf] = int(vlan)
		elif mode == "trunk":
			trunkports[intf] = vlans
	return (accessports, trunkports)
print(get_int_vlan_map(argv[1]))
