# -*- coding: utf-8 -*-
"""
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
"""
from netmiko import ConnectHandler
from task_22_3 import parse_command_dynamic
import yaml
from pprint import pprint
def connect_to_device(device_param, cmd):
    with ConnectHandler(**device_param) as ssh:
        ssh.enable()
        result = ssh.send_command(cmd)
    return result
def send_and_parse_show_command(device_dict, command, templates_path="templates", index="index"):
    cmd_output = connect_to_device(device_dict, command)
    att_dict={"Command":command}
    result = parse_command_dynamic(cmd_output, att_dict, index, templates_path)
    return result
if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices=yaml.safe_load(f)
    pprint(send_and_parse_show_command(devices[0], "show ip int br", "templates"))
