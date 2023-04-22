# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

numbers = list(map(int, input('Enter a value A and B: ').split()))
num_a = numbers[0]
num_b = numbers[1]

def PowNumber(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (PowNumber(a, -b - 1) * a)
    else:
        return PowNumber(a, b - 1) * a

print(f"The number A = {num_a} "
      f"to the integer power B = {num_b} "
      f"-> {PowNumber(num_a, num_b)}")