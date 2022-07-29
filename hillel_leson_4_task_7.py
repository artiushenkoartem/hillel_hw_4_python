"""Задача 7. 10 баллов
Написать программу которая данный список кортежей переведет в список списков
Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]"""
# create a variable with a list of tuples
list_of_tuples: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# converting all elements of a list to lists
list_of_lists = [list(x) for x in list_of_tuples]
# output the result
print(list_of_lists)
