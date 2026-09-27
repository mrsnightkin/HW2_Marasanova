def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def main_func(a, b, op):
    if op == '+':
        result = add(a,b)
    elif op == '-':
        result = subtract(a,b)
    elif op == '*' or op == 'x':
        result = mul(a,b)
    elif op == '/' or op == ':':
        result = divide(a,b)
    else:
        return 'Математическая операция не распознана. Пожалуйста, введите другое выражение!'
    return f"{a} {op} {b} = {result}"

a, op, b = input("Введите выражение:").split(sep = ' ')
a = float(a)
b = float(b)
print(main_func(a, b, op))
