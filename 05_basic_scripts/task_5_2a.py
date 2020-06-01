# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
subnet = input("enter subnet:  ")
network = subnet[:subnet.find("/"):]
ml = subnet[:subnet.find("/"):-1]
ml = int(ml[::-1])
m="1"*ml
m=m+"0"*(32-ml)
net = network.split(".")
n=f"{bin(int(net[0]))[2:]:>08}"
n=n+f"{bin(int(net[1]))[2:]:>08}"
n=n+f"{bin(int(net[1]))[2:]:>08}"
n=n+f"{bin(int(net[3]))[2:]:>08}"
n=n[:ml]
n=n+"0"*(32-ml)

print (f"""

network: {n}
{int(n[0:8], 2):<10} {int(n[8:16], 2):<10} {int(n[16:24], 2):<10} {int(n[24:32], 2):<10}
{n[0:8]:<10} {n[8:16]:<10} {n[16:24]:<10} {n[24:32]:<10}
Mask:
/{ml}
{int(m[0:8], 2):<10} {int(m[8:16], 2):<10} {int(m[16:24], 2):<10} {int(m[24:], 2):<10}
{int(m[0:8]):<10} {int(m[8:15]):<10} {int(m[16:23]):<10} {int(m[24:32]):<10}
""")
