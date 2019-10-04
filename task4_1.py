a = input("Введите значение: ")
c = len(a)
while c > 0:
    print(a)
    a = a[1:]
    c -= 1
