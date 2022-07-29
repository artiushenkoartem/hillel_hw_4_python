"""Задача 9. 10 баллов
Тема Листы
Даны два списка элементов если хоть один елемент совпадает отпринтить True.
print(Тrue) не слово! а объект подставить."""
# create two lists of elements
first_list = [10, 16, 'ar', 8, 'ee', 'ks']
second_list = [8, 'we', 'ar', 4]
# create two interpreted variables for each of the lists
for i in first_list:
    for q in second_list:
        # create a condition for the equality of interpreted variables
        if i == q:
            print(True)
            exit(0)
