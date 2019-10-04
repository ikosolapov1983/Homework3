a = list(input("Введите данные: "))
a.sort()
print(a)
i = 0
for el in range(len(a)):
    print(a[i])
    del a[i]
print(a)
