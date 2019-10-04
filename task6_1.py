# Заставляем вводить число
def s(a):
    a = input("Введите число: ")
    while True:
        try:
            a = float(a)
        except:
            print("Это не число!!!!")
        else:
            break
    return a

# Проверка на пробелы
def x(b):
    b = input("Введите строку БЕЗ пробелов: ")
    while True:
        if ' ' in b:
            print("Тут пробелы!!!")
        else:
            break
    return b

# Проверка високосного года
def is_year_leap(a):
    a = int(a)
    if a % 100 != 0 and a % 4 == 0:
        return True
    elif a % 400 == 0:
        return True
    else:
        return False

# Существование треугольника
def treug(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Определяем тип треугольника
def triangle(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Равносторонний треугольник")
        if a == b or a == c or b == c:
            print("Равнобедренный треугольник")
        if a != b and a != c and b != c:
            print("Разносторонний треугольник")
    else:
        print("Такого треугольника нет!")

# Расчет дистанции
def distance(x1, y1, x2, y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    d = ((x2 - x1) ** 2 + (y2-y1) ** 2) ** 0.5
    return d
