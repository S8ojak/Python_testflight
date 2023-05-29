# Алгоритм получения цифр n-значного числа
# Несложно понять, по какому алгоритму можно найти каждую цифру
# n-значного числа num:
# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.
num = int(input())
last_digit = num % 10
first_digit = (num // 10) % 10
second_digit = num // 100
print('число десятков', first_digit)
print('число единиц', last_digit)
print('сумма чисел двузначного числа', last_digit + first_digit) 
print('перестановка числе двузначного числа', last_digit * 10 +first_digit)
print(second_digit, first_digit, last_digit, sep=' , ')