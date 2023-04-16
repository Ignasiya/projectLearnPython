'''
Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

num = int(input('Введите любое натуральное число: '))
tempNum = num
sum = 0
while tempNum: # Как выйдет в ноль или Empty станет false
    sum += tempNum % 10
    tempNum //= 10
print(f'Cумма цифр чила {num} -> {sum}')