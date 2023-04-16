'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
1 2 3 4 5
6
-> 5
'''

import random

size = int(input('Enter the size of the list: '))

array = [random.randint(0, 99) for i in range(size)]
print(*array)

findNum = int(input('Enter a number to search for: '))

result = 0
Diff = 100
for item in array:
    tempDiff = findNum - item
    if tempDiff >= 0 and tempDiff < Diff:
        Diff = tempDiff
        result = item

print(f"The element closest in size to a given number {findNum} -> {result}")