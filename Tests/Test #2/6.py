x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
a = x2 - x1
b = y2 - y1

if a ** 2 == b ** 2:
    print("Да")
else:
    print("Нет")