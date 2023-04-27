def grandfather():
    print('Дедка зовёт бабку.')
    grandmother()
    print('Дедка за репку!')

def grandmother():
    print('Бабка зовёт внучку.')
    granddaughter()
    print('Бабка за дедку.')

def granddaughter():
    print('Внучка зовёт жучку.')
    dog()
    print('Внучка за бабку!')

def dog():
    print('Жучка зовёт кошку.')
    cat()
    print('Жучка за внучку!')

def cat():
    print('Кошка зовёт мышку.')
    mouse()
    print('Кошка за жучку!')

def mouse():
    print('Мышка никого не зовёт. Мышка просто тянет за кошку.')

grandfather()
print("Ура! И вытянули репку!")