# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и 
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# print_operation_table(lambda x, y: x * y)
# print_operation_table(operation, num_rows=6, num_columns=6)

rows, columns = int(input()), int(input())

def print_operation_table(f, rows, columns):
    for column in range(1, columns + 1):
        for row in range(1, rows + 1):
            print(f(column, row), end=' ')
        print()

print_operation_table(lambda x, y: x * y, rows, columns)