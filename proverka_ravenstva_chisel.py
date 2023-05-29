num = int(input())
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
if digit1 == digit2 == digit3:
    print("в трехзначном числе все цифры одинаковы")
else:
    print("Короче есть разные цифры")
print(digit1)
print(digit2)
print(digit3)