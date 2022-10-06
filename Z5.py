# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

import random
number = random.randint(1, 15)
print('k =', number)
list_n = [0,1]
for i in range(2, number+1):
    list_n.append(list_n[i-1] + list_n[i-2])
number = -number
for i in range(0, number, -1):
    list_n.insert(0, (list_n[1] - list_n[0]))
print('Ответ:', list_n)