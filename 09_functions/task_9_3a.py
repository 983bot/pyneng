# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
	mode = ""
	for line in f:
		if line.startswith("interface FastEthernet"):
			intf = line.split()[-1]
		elif "trunk allowed vlan " in line:
			vlans = line.split()[-1].split(",")
			for i in range(len(vlans)): vlans[i]=int(vlans[i])
			trunkports[intf] = vlans
		elif "switchport mode access" in line:
			mode ="access"
		elif "switchport access vlan " in line:
			vlan = line.split()[-1]
		elif line.startswith("!"): 
			if mode == "access" and vlan:
				accessports[intf]=int(vlan)
				vlan=""
			elif mode == "access":
				accessports[intf]=1
			mode=""
	return (accessports, trunkports)
print(get_int_vlan_map(argv[1]))
