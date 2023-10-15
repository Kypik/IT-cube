num = int(input())
print ("Сумма цифр числа", num, "=", num // 100000+ num // 10000 % 10 + num // 1000 % 10 + num // 100 % 10 + num // 10 % 10 + num % 10)