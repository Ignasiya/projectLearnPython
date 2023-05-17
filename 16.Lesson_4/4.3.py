list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1)) # 2 параметра - функция которая применяется к каждому объекту, и объект
print(list_1)