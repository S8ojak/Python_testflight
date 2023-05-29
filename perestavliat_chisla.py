num = int(input())
digit1 = num // 10000 # вычисляем первую цифру
digit2 = (num // 1000) % 10 # вторую и т.д.
digit3 = (num // 100) % 10
digit4 = (num // 10) % 10
digit5 = num % 10
print(digit1, digit2, digit3, digit4, digit5)
print(num, num // 10000, sep='\n')
print(num, num // 1000, (num // 1000) % 10)
print('hello world!')
print(num // 100, (num // 100) % 10)
print(num % 10000 // 1000)