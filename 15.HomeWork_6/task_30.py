# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

parametrs = list(map(int, input('Enter parametrs: ').split()))
num_a, num_b, num_c = parametrs[0], parametrs[1], parametrs[2]

result = [num_a + i * num_b for i in range(num_c)]

print(*result)