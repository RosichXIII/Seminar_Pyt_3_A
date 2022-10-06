# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import math
list_n = []
list_len = random.randint(3,9)
for i in range(list_len):
    list_n.append(random.randint(0,9))
print('Список:', list_n)
print('Ответ: ', end = ' ')
for i in range(math.ceil(len(list_n)/2)):
    print(list_n[i]*list_n[len(list_n)-1-i], end = ' ')