# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        pass
        self.ignore_case = kwargs.get('ignore_case',False)
        self.uniq_items = list()
        self.items = iter(items)

    def __next__(self):
        # Нужно реализовать __next__    
        pass
        while self.items:
            value = next(self.items) #will Raise StopIteration
            if self.ignore_case and type(value) == str:
                value = str(value).lower()
            if value not in self.uniq_items:
                self.uniq_items.append(value)
                return value

    def __iter__(self):
        return self
