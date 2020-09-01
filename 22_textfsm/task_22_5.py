# -*- coding: utf-8 -*-
"""
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
"""
from task_22_4 import send_and_parse_show_command
import yaml
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
def send_and_parse_command_parallel(device_dicts, command):
    with ThreadPoolExecutor(max_workers=3) as executor:
        cmd_execute=executor.map(send_and_parse_show_command, device_dicts, repeat(command))
        result = []
        for device, output in zip(device_dicts, cmd_execute):
            result.append({device["host"]:output})
    return result
if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices=yaml.safe_load(f)
    pprint(send_and_parse_command_parallel(devices, "show ip int br"))
