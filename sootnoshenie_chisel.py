# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.
num = int(input())
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
print(digit1, digit2, digit3,digit4)
a = digit1 + digit4
b = digit2 - digit3
if a == b:
    print('ДА')
else:
    print('НЕТ')
