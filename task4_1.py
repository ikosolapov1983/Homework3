a = int(input("Введите первое число списка: "))
b = int(input("Введите конечное число списка: "))
l = list(range(a, b+1))
c = len(l)
while c > 0:
    print(l)
    del l[0]
    c -= 1
