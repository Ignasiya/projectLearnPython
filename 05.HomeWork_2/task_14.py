'''
Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
'''

num = int(input('Введите натуральное число: '))

while num <= 0: #Проверка на дурака
    print('Введено некорректное значение')
    num = int(input('Введите натуральное число: '))

print(f"Степени двойки ->", end = ' ')
i = 0
while 2 ** i <= num:
    print(2 ** i, end = ' ')
    i += 1