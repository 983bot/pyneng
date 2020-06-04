# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
f'''{"Prefix":<22} {ospf_route.split()[0]:<22} 
 {"AD/Metric":<22} {ospf_route.split()[1].strip("[]"):<22} 
 {"Next-Hop":<22} {ospf_route.split()[3].strip(","):<22} 
 {"Last update":<22} {ospf_route.split()[4].strip(","):<22}
 {"Outbound Interface":<22} {ospf_route.split()[5]:<22}''' 
