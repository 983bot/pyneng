# -*- coding: utf-8 -*-
"""
Задание 21.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
"""

data = {
    "tun_num": None,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}
device1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
}
device2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.2',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
}

import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import re
from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import os
def chk_dev(dev1, dev2):
    ssh1=ConnectHandler(**dev1)
    ssh1.enable()
    result1=ssh1.send_command("sh ip int br | i Tunnel")
    ssh2=ConnectHandler(**dev2)
    ssh2.enable()
    result2=ssh2.send_command("sh ip int br | i Tunnel")
    return result1, result2
def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    regex=r"Tunnel(\d+)\s+"
    tunlist=[]
    for tunnels in chk_dev(src_device_params, dst_device_params):
        tunnels1=[match.group(1) for match in re.finditer(regex, tunnels)]
        tunlist+=tunnels1
    vpn_data_dict["tun_num"]="Tunnel"+ str(int(max(tunlist)) + 1)
    path1, fl1 = os.path.split(src_template)
    env1=Environment(loader=FileSystemLoader(path1))
    path2, fl2 = os.path.split(dst_template)
    env2=Environment(loader=FileSystemLoader(path2))
    template1 = env1.get_template(fl1)
    template2 = env2.get_template(fl2)
    config1 = template1.render(vpn_data_dict).split('\n')
    config2 = template2.render(vpn_data_dict).split('\n')
    return config1, config2
if __name__ == "__main__":
    pprint(configure_vpn(device1, device2, "templates/gre_ipsec_vpn_1.txt", "templates/gre_ipsec_vpn_2.txt", data))

