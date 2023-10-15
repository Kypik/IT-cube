num = int(input())
if num == 0:
    print("Зеленый")
elif num >= 1 and num <= 10 or num >= 19 and num <= 28:
    if num % 2 != 0:
        print("Красный")
    else:
        print("Черный")
elif num >= 11 and num <= 18 or num >= 29 and num <= 36:
    if num % 2 != 0:
        print("Черный")
    else:
        print("Красный")
else:
    print("Ошибка ввода")