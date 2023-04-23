# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.

# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

# 7
# 3 1 3 4 2 4 12

# 6
# 4 15 43 1 15 1

list1 = [input(f'{i + 1}: ')
         for i in range(int(input("enter the size of first arrray: ")))]
list2 = [input(f'{i + 1}: ')
         for i in range(int(input("enter the size of first arrray: ")))]
list3 = [i for i in list1 if i not in list2]

print(*list1)
print(*list2)
print(*list3)
