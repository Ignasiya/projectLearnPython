# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

numbers = list(map(int, input('Enter a value A and B: ').split()))
num_a = numbers[0]
num_b = numbers[1]

def sum(a, b):
    if a == 0:
        return b
    return sum(a - 1, b + 1)

print(f"The sum of the numbers A = {num_a} and B = {num_b}"
      f" -> {sum(num_a, num_b)}")