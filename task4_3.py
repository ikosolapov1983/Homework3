a = list(input("Введите данные: "))
c = len(a)
while c > 0:
    print(a)
    a.remove(min(a))
    c -= 1

