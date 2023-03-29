import pprint
import re

import pandas as pd
from re import *
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
outputfile = '../new_phonebook.csv'
with open("phonebook", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # print(contacts_list)

pattern = r"(\+7|7|8)\s*\(*(\d{3})\)*[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d{2})\b\s*(\s*)(\w*\.*)\s*(\d*)"
repl = r"+7(\2)\3-\4-\5\6 \7\8"


lst_phone = []
dict_fio = {}
for i in contacts_list:
    page = ','.join(i)
    num_pattern = sub(pattern, repl, page)
    num_page = num_pattern.split(',')

    fio = ' '.join(num_page[:3]).split()
    num_page[:len(fio)] = fio
    dict_fio[''.join(num_page[:2])] = num_page
for key, val in dict_fio.items():
    lst_phone.append(val)

new_book = lst_phone
print(new_book)

out = [','.join(row)+'\n' for row in lst_phone]
with open(outputfile, "w", newline='', encoding='utf-8') as f2:
    f2.writelines(out)


