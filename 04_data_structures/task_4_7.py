# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac = bin(int(mac.replace(":", ""), 16)).strip("0b")


# reverse convertation
 mac = list(hex(int(mac, 2)).strip("0x"))
 mac.insert(4,".")
 mac.insert(9,".")
 mac = "".join(mac).upper()
