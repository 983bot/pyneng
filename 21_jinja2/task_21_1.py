# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""
import os
from jinja2 import Environment, FileSystemLoader
import yaml
def generate_config(template, data_dict):
    path, fl = os.path.split(template)
    env=Environment(loader=FileSystemLoader(path), trim_blocks=True, lstrip_blocks=True)
    templ=env.get_template(fl)
    return templ.render(data_dict)
if __name__=="__main__":
    with open("data_files/for.yml") as f:
        data=yaml.safe_load(f)
    print(generate_config("templates/for.txt", data))

