# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)

array = [0, -1, 5, 2, 3]

result = [array[i] > array[i - 1] for i in range(1, len(array))]
    
print(sum(result))