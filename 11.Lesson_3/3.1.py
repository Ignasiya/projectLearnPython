def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(sum_numbers(5, 'Hi'))