'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
1 2 3 4 5
3
-> 1
'''
import random

size = int(input('Enter the size of the list: '))

array = [random.randint(0, 9) for i in range(size)]
print(*array)

findNum = int(input('Enter a number to search for: '))

result = 0
for i in array:
    if array[i] == findNum:
        result += 1
    
print(f"The number {findNum} occurs {result} times in the list")