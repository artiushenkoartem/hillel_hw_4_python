"""Задача 3. 15 баллов
Тема list и его методы. Строки и срезы.
Программа принимает список продуктов и принтит самое длинное слово и его длинну.
Ипользовать ''.format() для вывода строки и аргументов.
Входные данные: ['bread', 'milk', 'kolbasa']
Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'"""
# create a variable containing a list of products
shopping_list: list = ['bread', 'milk', 'kolbasa']
# create an empty string variable
longest_word = ""
# assign to variable "i" all values of "shopping_list"
for i in shopping_list:
    # set the condition for the length of the variables
    if len(i) > len(longest_word):
        # equate two variables
        longest_word = i
# output the final string by formatting it
print("Самое длинное название продукта {0} длинна {1} символов.".format(longest_word, len(longest_word)))
