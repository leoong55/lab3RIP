#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data_str = ['a', 'A', 'b', 'B']

def one_liner(arg):
    print(', '.join(str(x) for x in arg))

# Реализация задания 2
if __name__ == '__main__':
    test = Unique(data1)  # pre-generated list
    one_liner(test)
    test = Unique(data2)  # our generator test
    one_liner(test)
    test = Unique(data_str)  # cased string
    one_liner(test)
    test = Unique(data_str, ignore_case=True)  # caseless string
    one_liner(test)


