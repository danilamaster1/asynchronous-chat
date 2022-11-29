"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""
import os
import re
import csv
from chardet import detect


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def collect_data():
    data_dir = os.path.join(CURRENT_DIR, 'info_files')
    info_files = [i for i in os.listdir(data_dir) if i.split('.')[1] == 'txt']
    result = []

    for filename in info_files:
        filepath = os.path.join(data_dir, filename)

        with open(filepath, 'rb') as file:
            content = file.read()
            ENCODING = detect(content)['encoding']

        with open(filepath, 'r', encoding=ENCODING) as fl:
            for line in fl.readlines():
                result += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)

    return result


def get_data():
    data = collect_data()

    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for item in data:
        os_prod_list.append(item[1]) if item[0] == main_data[0][0] else None
        os_name_list.append(item[1]) if item[0] == main_data[0][1] else None
        os_code_list.append(item[1]) if item[0] == main_data[0][2] else None
        os_type_list.append(item[1]) if item[0] == main_data[0][3] else None

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv(filepath):
    data = get_data()

    dir_, filename = os.path.split(filepath)

    os.makedirs(dir_, exist_ok=True)

    filepath = os.path.join(CURRENT_DIR, dir_, filename)

    with open(filepath, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        for line in data:
            writer.writerow(line)


write_to_csv('info_files/data_report.csv')







