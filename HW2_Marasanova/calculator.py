def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def main_func(a, b, op):
    if op == '+':
        add(a,b)
    elif op == '-':
        subtract(a,b)
    elif op == '*' or op == 'x':
        mul(a,b)
    elif op == '/' or op == ':':
        divide(a,b)
    else:
        print('Математическая операция не распознана. Пожалуйста, введите другое выражение!')

a, op, b = input("Введите выражение:").split(sep = ' ')
a = float(a)
b = float(b)
main_func(a, b, op)

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b
