# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list_n = []
list_len = random.randint(1,9)
for i in range(list_len+1):
    list_n.append(random.randint(0,9))
print('Список:', list_n)
print('Сумма чисел на нечётных позициях =', sum(list_n[i] for i in range(len(list_n)) if i%2 !=0))