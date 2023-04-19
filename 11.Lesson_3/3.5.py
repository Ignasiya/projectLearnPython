def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([14,5,9,6,3,58,7,5,2,7]))