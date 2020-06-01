# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

mode = input("enter interface mode (access/trunk):  ")
question = {"access":"enter VLAN number:  ","trunk":"enter the list of alloved VLANs:  "}
interface = input("enter interface name/number: ")
vlans = input(question.get(mode, "press any key"))

modevar = {"access":access_template, "trunk":trunk_template}

print(f"interface {interface}\n"+"\n".join(modevar.get(mode, ["\n"])).format(vlans))

