"""Задача 1. 10 баллов
тема Срезы и условие if.
написать программку которая будет состоять из первых двух и последних символов предоставленной строки.
Если длинна строки меньше двух символов напечатать строку типа.
'Ваша строка слишком короткая - СТРОКА ' . Через метод форматирования строк с %.
Входная строка : 'Hillel school'
Результат1 : 'Hiol' или
Результат2 : 'Ваша строка слишком короткая - и ваша строка'"""
# create variable from user input
user_string: str = input("Введите вашу строку: ")
# set length conditions for user variable
if len(user_string) < 2:
    print("Ваша строка слишком короткая - %s" % user_string)
# if the variable is not subject to length conditions
else:
    # output the first two and last two letters of a variable using string formatting
    print(f"{user_string[:2]}{user_string[-2:]}")
