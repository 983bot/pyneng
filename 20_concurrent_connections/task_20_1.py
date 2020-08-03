# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor
from sys import argv
from pprint import pprint
def ping(ip):
    result=subprocess.run(['ping', '-c', '3', '-n', ip])
    if result.returncode == 0:
        return True
    else:
        return False
def ping_ip_addresses(ip_list, limit=3):
    pprint(ip_list)
    with ThreadPoolExecutor(max_workers=limit) as executor:
        ping_test = executor.map(ping, ip_list)
    result=zip(ip_list, ping_test)
    reachable=[]
    unreachable=[]
    for ip, test in result:
        if test:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable
if __name__ == "__main__":
    pprint(ping_ip_addresses(argv[1::], 5))

