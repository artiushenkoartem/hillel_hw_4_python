"""Задача 8. 15 баллов
Тема range
Есть последовательность от -99 до 99. Ее шаг 3. т.е. [-99, -96]
напечатать все элементы последовательности которые делятся на 3 без остатка.
напечатать в формате 'это <<ЧИСЛО>> делится без остатка на 3'
использовать метод редактирования строки f' строки'"""
# create sequence with step 3
for n in range(-99, 99, 3):
    # set a condition for the resulting sequence
    if n % 3 == 0:
        # output a string with substituted values that match the condition
        print(f'это <<{n}>> делится без остатка на 3')
