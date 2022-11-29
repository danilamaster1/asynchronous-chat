"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as f:
        data = json.loads(f.read())

    data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, separators=(',', ': '), ensure_ascii=False)


write_order_to_json('pc', 4, 12000, 'Lena', '12.05.2021')
write_order_to_json('tv', 1, 4450, 'Max', '01.02.2021')
