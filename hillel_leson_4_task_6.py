"""Задача 6. 5 баллов
Тема Кортеж и работа сним.
Удaлить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)"""
# create immutable tuple
first = (1, 2, 3)
# transfer it to the list for further changes
second = list(first)
# remove the last component using the "pop" function
second.pop()
# convert list back to tuple
first = tuple(second)
# output a tuple
print(first)
