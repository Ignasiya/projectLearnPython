a = [1, 2, 3]
print(a)
for i, x in enumerate(a):
    print(f"#{i}: x = {x}; a[i] = {a[i]};", "x is a[i]" if x is a[i] else "x is not a[i].")
    x = x + 1  # Казалось бы, в этой строке мы меняем элементы списка, но нет...
    print(f"#{i}: x = {x}; a[i] = {a[i]};", "x is a[i]" if x is a[i] else "x is not a[i].\n")
print(a)

a = ["Hello", 15, 1.23, 2 + 2 == 4, (7, 8), lambda x: x**2]
for x in a:
    print(x, type(x), sep='\t')

words = []
x = input("Введите слово: ")
while x != "":
    words.append(x)
    x = input("Введите слово: ")
print(words)

s = "Я набрал 294 балла, и хотел поступать в МГУ, ВШЭ или МФТИ.".replace(',', '').replace('.', '')
capital_words = []
numbers = []
other_words = []
for word in s.split():
    if word.isupper():
        capital_words.append(word)
    elif word.isnumeric():
        numbers.append(word)
    else:
        other_words.append(word)
print(f"capital_words ={capital_words}")
print(f"numbers ={numbers}")
print(f"other_words ={other_words}")

while words:  # Читайте этот заголовок цикла так: **пока список слов не пуст**.
    print(words.pop())  # Пользуемся тем, что метод pop() не только удаляет элемент, но и возвращает его значение.

print("старая длина списка:", len(a))
a[3:6] = (777,)  # Это кортеж tuple, содержащий только один элемент. Запятая перед скобкой тут нужна!
print("новая длина списка:", len(a))
a

print(a[1:1], len(a[1:1]))  # Ну он же реально пустой!
a[1:1] = range(10, 70, 10)
print(a)  # А вот и профит.

a = [1, 2, 3, 5, 2, 123, 3, 22, 93, 10]
print(a)
a.sort(reverse=True)
print(a)

s = "Клара у Карла украла кораллы, Карл у Клары украл кларнет.".replace(',', '').replace('.', '')
words = s.split()
print(words)
words.sort(key=len)
print(words)
words.sort(key=lambda word: word.casefold())
print(words)

a = list(range(10))
b = sorted(a, key=lambda x: abs(x-4.5), reverse=True)
print(b)

from copy import deepcopy
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(a)
c = [x for x in a]
d = a[:]
e = a.copy()
f = deepcopy(a)
for the_list in a, b, c, d, e, f:
    print(the_list, id(the_list))

the_list_of_lists = [[(i*6 + k + 1) for k in range(6)] for i in range(4)]
for the_list in the_list_of_lists:
    print(*the_list, sep='\t')

M = 6  # Ширина таблицы. Она же — длина строк таблицы или количество столбцов.
N = 4  # Высота таблицы. Количество строк таблицы.
a = [(x+1) for x in range(M * N)]
print(a)
for i in range(N):
    for k in range(M):
        print(a[i*M + k], end='\t')  # Расплата за простоту — **эмуляция двумерности**.
    print()