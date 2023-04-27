a = ['1', '2', '3', '4', '5'] #перечисление объектов в квадратных скобках через запятую
b = list('12345') # через конструктор
print(a, b)
print(a == b)  # равные друг другу списки
print(a is b)  # могут быть разными объектами

text = """Любовь долготерпит, милосердствует, любовь не завидует,
          любовь не превозносится, не гордится, не бесчинствует, не ищет своего,
          не раздражается, не мыслит зла, не радуется неправде, а сорадуется истине;
          все покрывает, всему верит, всего надеется, все переносит."""
words = text.split()  #  разбиваем строку text по пробелам на отдельные слова


stripped_lines = [line.strip() for line in lines]
stripped_lines

filtered_lines = [line for line in stripped_lines if 'любовь' in line] # в новый список выбираем только те строки, в которых есть слово "любовь"
filtered_lines

changed_and_filtered1 = [line.lower() for line in stripped_lines if 'не' in line] 
# в новый список выбираем только те строки, в которых есть слово "не", 
# и применяем ко всем строкам метод lower, который "превращает" все буквы в строчные
changed_and_filtered1

filtered = filter(lambda s: 'не' in s, stripped_lines)
changed_and_filtered2 = map(lambda s: s.lower(), filtered)

for line in changed_and_filtered2:
    print(line)

a = "Moscow"
b = map(lambda char: chr(ord(char) + 1), a)
print('once:', *b)
print('again:', *b)

a = "Moscow"
c = [chr(ord(char) + 1) for char in a]
print('once:', *c)
print('again:', *c)

a = "Алексей Руслан Тимур".split()
b = "Алёна Рита Тая".split()
for x, y in zip(a, b):
    print(x, '+', y, '= \u2665')

for number, student in enumerate(["Маша", "Вася", "Петя", "Рома", "Макар"]):
    print(number, student)

for x, y, z in it.permutations("ABCDE", 3):
    print(x, y, z, sep='', end='\t')

for x, y in it.combinations("ABCDE", 2):
    print(x, y, sep='', end='\t')

for x, y in it.combinations_with_replacement("ABCDE", 2):
    print(x, y, sep='', end='\t')

for n, s in it.product([1, 2, 3, 4], "ABC"):
    print(n, s)