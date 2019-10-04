a = input("Введите данные a: ")
b = input("Введите данные b: ")
try:
    c = int(a) + int(b)
    print(c)
except:
    c = a + b
    print(c)

