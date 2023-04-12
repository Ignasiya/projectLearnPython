dictionary = {}
dictionary[895] = 98998
print(dictionary)

del dictionary[895]
for item in dictionary:
    print(item) # Вывод ключей
    print('{}: {}'.format(item, dictionary[item]))

for (k, v) in dictionary.items(): # альтернатива
    print(k, v)