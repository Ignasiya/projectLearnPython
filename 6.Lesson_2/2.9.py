# Операции со множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy() # копирует
print(c)

u = a.union(b) # объедияет уникальные значения
print(u)

i = a.intersection(b) # пересечение - 8, 2, 5
print(i)

dl = a.difference(b) # вычитает - 1, 3
print(dl)

dr = b.difference(a) # вычитает - 13, 21
print(dr)

q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
print(q)

a = {1, 8, 6}

b = frozenset(a) # не мождем менять