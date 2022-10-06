# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import math
list_n = []
list_len = random.randrange(2, 9)
for i in range(list_len):
    list_n.append(round(random.random()*100, 2))
print('Список:', list_n)
max = list_n[0]%1
min = list_n[0]%1
for i in range(list_len):
    if list_n[i]%1 > max:
        max = list_n[i]%1
    elif list_n[i]%1 < min:
        min = list_n[i]%1
print('Ответ:', round(max-min, 2))