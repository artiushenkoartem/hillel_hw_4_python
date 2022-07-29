"""Задача 2. 15 баллов
Тема Dict
Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}"""
# ask the user to enter text and create a list based on this
user_text: list = list(input("Print you sting"))
# create an empty dictionary
our_dictionary: dict = {}
# create an iterable variable based on input
for i in user_text:
    # loop through the interpreted variables and the number of occurrences in them
    our_dictionary[i] = int(user_text.count(i))
# output the final dictionary
print(our_dictionary)
