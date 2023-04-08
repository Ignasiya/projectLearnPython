'''
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вырасплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где суммапервых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
'''
import random

# ticket = int(input('Введите номер билета (шестизначное число): '))
ticket = random.randint(100000, 1000000)

firstPart = ticket % 1000
firstSum = 0

while firstPart > 0:
    firstSum += firstPart % 10
    firstPart //= 10

secondPart = ticket // 1000
secondSum = 0

while secondPart > 0:
    secondSum += secondPart % 10
    secondPart //= 10

if firstSum == secondSum:
    boolTicket = 'yes'
else:
    boolTicket = 'no'

print (f'Счастливый билет {ticket} -> {boolTicket}')