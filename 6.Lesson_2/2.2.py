list_1 = [] # СПИСОК
print(list_1)

for i in range(5):
    list_1.append(i)
    print(list_1)

a = list_1.pop() # удаляет последнее значение
b = list_1.pop(0) # удаляет значение индекса

c = list_1.insert(2, 11) # на второй индекс вставляется значение 11
print(list_1) 