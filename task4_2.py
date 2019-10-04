a = input("Введите данные: ")
c = len(a)
while c > 0:
    print(a)
    a = a.replace(a[0], "")
    c -= 1

