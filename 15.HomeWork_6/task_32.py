# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. 
# неменьше заданного минимума и не больше заданного максимума)

# Ввод: 
# 5, 15
# [-5, 9, 0, 3, -1, -2, 1,4, -2, 10, 2, 0, -9, 8, 10, -9,0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

import random

parametrs = list(map(int, input('Enter parametrs (size), (min), (max): ').split()))
size, min, max = parametrs[0], parametrs[1], parametrs[2]

list_1 = [random.randint(- 50, 50) for _ in range(size)]
print(*list_1)

for i in range(size):
    if min <= list_1[i] <= max:
        print(i, end = ' ')

# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])