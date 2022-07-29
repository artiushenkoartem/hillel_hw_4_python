"""Задача 4. 5 баллов
Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo"""
# create variable from user input
user_name = input('Fill up you name')
# using string formatting, display text with converted variables
print("{0} {1}".format(user_name.upper(), user_name.lower()))
