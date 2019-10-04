x = input("Введите значение: ")
if len(x) % 2 == 0:
    x1 = x[len(x)//2:] + x[:len(x)//2]
else:
    x1 = x[len(x)//2+1:] + x[:len(x)//2+1]
print(x1)

