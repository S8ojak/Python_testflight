num = int(input())
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
sum = digit1 + digit2 + digit3
proizvedenie = digit1 * digit2 * digit3
print('Сумма цифр =', sum)
print('Произведение цифр =', proizvedenie)
