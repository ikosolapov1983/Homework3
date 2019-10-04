x = int(input("Введите число: "))
count = 0
while x % 2 == 0:
    x = x / 2
    count += 1
print("Количество делений: ", count)
