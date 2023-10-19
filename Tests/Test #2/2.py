x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 % 2 == x2 % 2 and y1 % 2 == y2 % 2:
    print("Да")
elif x1 % 2 != x2 % 2 and y1 % 2 != y2 % 2:
    print("Да")
else:
    print("Нет")
