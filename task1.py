a = input("Введите строку: ")
if len(a) >= 5:
    print(a[2], a[-2], a[0:5], a[:-2], a[1::2], a[0::2], a[::-1], a[::-2], a[-2::-2], a[-2:0:-1], len(a), sep='\n')
else:
    print("Строка слишком короткая!!")