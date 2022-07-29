"""Задача 5. 15 баллов.
Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.
Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white"""
# create variable from user input
a = input()
# split a string into its contents using the "split" function
a = a.split(", ")
# all values are transferred to a collection to remove duplicate values
a = set(a)
# we translate the collection into a list so that we can work with it
a = list(a)
# sort the list alphabetically and add delimiters to it
print(*sorted(a), sep=", ")
