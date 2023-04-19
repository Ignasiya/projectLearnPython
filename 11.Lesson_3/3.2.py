def sum_str(*args): # * - неограниченное колл-во элементов
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('s', 't', 'o', 'p'))

print(sum_str(1, 8, 9)) # Ошибка