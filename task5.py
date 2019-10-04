a = input("Введите данные a: ")
b = input("Введите данные b: ")
try:
    c = int(a) + int(b)
    print(c)
except ValueError as e:
    c = a + b
    print(c)
    print(e)


