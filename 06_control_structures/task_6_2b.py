# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
check = False
while not check:
    ip = input("enter IP address:   ")
    ipcheck = ip.split(".")
    for digit in ipcheck:
        try:
            if ( 0 <= int(digit)) & ( int(digit) <= 255 ):
                check = True
            else: 
                check = False
                print("Wrong IP")
                break
        except ValueError:
            check = False
            print("IP should contain only digits and '.' character")
octet1=int(ip[:ip.find(".")])
if not check:
    print("wrong IP")
elif ( octet1 >= 1 ) & ( octet1 <= 223 ):
    print(f"IP {ip} is unicast")
elif ( octet1 >= 224 ) & ( octet1 <=239 ):
    print(f"IP {ip} is multicast")
elif ip == "255.255.255.255":
    print(f"IP {ip} is local broadcast")
elif ip == "0.0.0.0":
    print(f"IP {ip} is unassigned")
else :
    print(f"IP {ip} is unused")


