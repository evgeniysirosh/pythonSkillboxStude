#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_code = goods['Стол']
tables_item = store[table_code][0]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price

table_code_1 = goods['Стол']
tables_item_1 = store[table_code_1][1]
tables_quantity_1 = tables_item_1['quantity']
tables_price_1 = tables_item_1['price']
tables_cost_1 = tables_quantity_1 * tables_price_1
print('Стол -', tables_quantity+tables_quantity_1, 'шт, стоимость', tables_cost+tables_cost_1, 'руб')

sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost = sofa_quantity*sofa_price

sofa_code_1 = goods['Диван']
sofa_item_1 = store[sofa_code_1][1]
sofa_quantity_1 = sofa_item_1['quantity']
sofa_price_1 = sofa_item_1['price']
sofa_cost_1 = sofa_quantity_1*sofa_price_1
print('Диван -', sofa_quantity+sofa_quantity_1, 'шт, стоимость', sofa_cost+sofa_cost_1, 'руб')


chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_cost = chair_price * chair_quantity

chair_code_1 = goods['Стул']
chair_item_1 = store[chair_code_1][1]
chair_quantity_1 = chair_item_1['quantity']
chair_price_1 = chair_item_1['price']
chair_cost_1 = chair_price_1 * chair_quantity_1

chair_code_2 = goods['Стул']
chair_item_2 = store[chair_code_1][2]
chair_quantity_2 = chair_item_2['quantity']
chair_price_2 = chair_item_2['price']
chair_cost_2 = chair_price_2 * chair_quantity_2

print('Стул -', chair_quantity+chair_quantity_1+chair_quantity_2, 'шт, стоимость', chair_cost+chair_cost_1+chair_cost_2, 'руб')
# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.



##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






