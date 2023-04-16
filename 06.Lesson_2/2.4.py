t = () # КОРТЕЖ НЕ МЕНЯЕТСЯ
print(type(t))

t = (1, 2, 3,) # запятая нужна
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b = 1, 2
a = b = 1

a, b, c = v
print(a, b, c)