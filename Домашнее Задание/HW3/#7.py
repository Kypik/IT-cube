num = int(input())
if num >= 1000 and num <= 9999:
    if num % 7 == 0 or num % 17 == 0:
        print("Да")
    else:
        print("Нет")
else:
    print("Нет")