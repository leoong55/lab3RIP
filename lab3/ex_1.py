#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'color': 'white'}
]

def one_liner(arg):
    print(', '.join(str(x) for x in arg))

# Реализация задания 1
if __name__ == '__main__':
    test = field(goods, 'title')
    print(', '.join(str(x) for x in test))
    #print(', '.join(str(x) for x in field(goods, 'title', 'price')))
    #print(', '.join(str(x) for x in gen_random(1, 5, 5)))
    one_liner(field(goods, 'title', 'price'))
    one_liner(gen_random(1, 5, 5))
