import json
import sys

"""
Не очень много работала с json в Python, так что, видимо, в этой программе
много костылей, но не было времени разобраться во всех нюансах работы
json.loads, .dump  и как это аккуратно парсить при разной вложенности.
Добавила себе в список для изучения))
"""


values_json = sys.argv[1]
tests_json = sys.argv[2]
report_json = sys.argv[3]

with open(values_json,"r") as f:
    s = f.readlines()
data1 = json.loads(''.join(s))

# создаем словарь, в котором, для удобства, только уникальные id в качестве
# ключа и результат в качестве значения.
new_dict = dict()
for item in data1['values']:
    new_dict[item['id']] = item['value']

value = ''
report_base = ''  # основа для будущего отчета
with open(tests_json,"r") as f:
    for s in f: 
        if '"id":' in s:
            # Для некоторых "id" нет значений, по-этому через try
            try:
                value = new_dict[int(s.split()[1][:-1])]
                #здесь из строки s вычленяем "id" и по нему берем значение из
                #вспомогательного словаря
            except KeyError:
                pass
        if '"value"' in s:
            s = s.replace('""', '"'+value+'"')
            
        report_base =report_base + s

with open(report_json,"w") as f:
    f.write(report_base)





