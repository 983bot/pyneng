# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""
import re
import argparse
def get_ip_from_cfg(fname):
    result={}
    fltr=('interface (?P<interface>\S+)|ip address (?P<ip>[\d.]+\d+) (?P<mask>[\d.]+\d+)')
    with open(fname) as f:
        for line in f:
            res=re.search(fltr, line)
            if res:
                if res.lastgroup == 'interface':
                    interface=res.group('interface')
                elif res.lastgroup == 'mask':
                    result[interface]=res.group('ip', 'mask')
    return result

if __name__ == "__main__":
    print(get_ip_from_cfg('config_r1.txt'))
