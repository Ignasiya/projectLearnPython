import string

filename = r'C:\Users\Василий\Documents\practicecode\ProectPython\00.MGU\orwell_1984.txt'

# не эффективный метод
with open(filename, "r", encoding='utf8') as file:
    text = file.read()

letters_frequencies = [text.count(letter) for letter in string.ascii_lowercase]

sorted_letters_and_frequencies = sorted(zip(string.ascii_lowercase, letters_frequencies),
                                        key=lambda pair: pair[1], reverse=True)
for letter, frequency in sorted_letters_and_frequencies:
    print(letter, frequency)

def letter_index(letter: str):
    """ Возвращает индекс буквы в английском алфавите (считая от нуля)
        работает с буквами в ВЕРХНЕМ и нижнем регистрах.
        
        >>> letter_index('a')
        0
        >>> letter_index('z')
        25
    """
    letter = letter.lower()
    assert len(letter) == 1, "Функцию можно вызывать только для символов (строк длины 1)."
    assert 'a' <= letter <= 'z', "Допускаются только английские символы (классическая латиница)."
    return ord(letter) - ord('a')

with open('animals.txt', encoding='utf8') as file:
    animals = set(line.strip() for line in file)  # немного "магии" с файлом, как с итерируемым объектом
    print(animals, len(animals))

print(*map(lambda animal: animal.title(), filter(lambda animal: animal[-1] == 'а', animals))) # фильтр последняя буква а

animals = {"корова", "собака", "кошка", "гусь", "курица", "тигр", "пчела", "оса", "щука"}
domestic_animals = {"корова", "собака", "кошка", "гусь", "курица", "пчела"}
mammals = {"корова", "собака", "кошка", "тигр"}

if mammals <= animals:
    print("Все млекопитающие являются животными.")
if animals >= domestic_animals:
    print("Все домашние животные являются животными.")

inverted_animals_names = {name[::-1] for name in animals}
print(inverted_animals_names)

states = "Россия", "Казахстан", "Китай"
capitals = "Москва", "Астана", "Пекин"
the_dict = dict(zip(states, capitals))
print(the_dict)

the_dict = {"корова": 2, "коза":2, "собака": 3, "кошка": 3,
            "рыба": 0, "петух": 8, "Гагарин": 7}
print("Угадайте, что значат числа в этой задаче-шутке?")
for key in the_dict:
    print(key, the_dict[key], sep=' - ')

key = input()
print("Число для ключа:", the_dict.get(key, "не знаю."))

animals_names = ["корова", "коза", "собака", "кошка", "рыба", "петух", "осёл"]
animals_sounds = ["му", "ме", "гав", "мяу", "", "кукареку", "иа"]
the_dict = {animal: len(sound) for animal, sound in zip(animals_names, animals_sounds)}
print("Разгадка задачи-шутки в исходном тексте:")
print(the_dict)

from collections import Counter 

with open("students.txt", encoding="utf8") as file:
    students_set = {line.strip() for line in file}
with open("elections.txt", encoding="utf8") as file:
    candidates_votes = Counter(line.strip() for line in file
                               if line.strip() in students_set)

rating = candidates_votes.most_common()
elected_delegate = rating[0][0]
print("Избранный представитель факультета:", elected_delegate)
print()  # представление результатов табличкой:
print("Фамилия кандидата".ljust(30), "Голосов".ljust(10), sep='| ')
print('-'*30 + '+' + '-'*10)
for candidate, votes in rating:
    print(candidate[:30].ljust(30), str(votes).ljust(10), sep='| ')