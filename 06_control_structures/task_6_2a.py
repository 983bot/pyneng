# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input("enter IP address:   ")
ipcheck = ip.split(".")
check = True
for digit in ipcheck:
    if ( 0 <= int(digit) <= 255 ):
        pass
    else:
        check = False
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

