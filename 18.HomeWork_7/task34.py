# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм 
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

poem = list(map(str, input('Write a poem: ').split()))

def find_rhythm_verses(poem):
    quantity = []
    for verse in poem:
        count = 0
        for char in 'уеыаоёэяию':
            count += verse.count(char)
        if count == 0: 
            return False
        quantity.append(count)
    return len(set(quantity)) == 1

if find_rhythm_verses(poem): print('Парам пам-пам')
else: print('Пам парам')