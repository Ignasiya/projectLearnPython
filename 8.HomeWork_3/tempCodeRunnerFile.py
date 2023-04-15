import random

size = int(input('Enter the size of the list: '))

array = [random.randint(0, 10) for i in range(size)]
print(*array)

findNum = int(input('Enter a number to search for: '))

result = 0
for i in array:
    if array[i] == findNum:
        result += 1
    
print(f"The number {findNum} occurs {result} times in the list")