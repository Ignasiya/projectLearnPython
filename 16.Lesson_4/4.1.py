def calc_1(a, b):
    return a + b

def calc_2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(lambda a, b: a + b, 5, 45)