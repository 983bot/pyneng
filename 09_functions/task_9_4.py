# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
	"""
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
	"""
	return any(word in command for word in ignore)
from sys import argv

def convert_config_to_dict(config_filename=argv[1]):
	f = open(config_filename)
	result={}
	key=""
	value=[]
	for line in f:
		if line.strip() != "" and (not ignore_command(line,ignore)) and line.split()[0] != "!":
			if not line.startswith(" "):
				if key: result[key]=value
				key = line.rstrip()
				value=[]
			else:
				value.append(line.strip())
	result["end"]=[]
	return result
prt = convert_config_to_dict()
for key, value in convert_config_to_dict().items():
	print(f"{key}: {value}/n")

