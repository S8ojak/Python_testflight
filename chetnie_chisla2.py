num, num1, num2 = int(input()), int(input()), int(input())
counter = 0  # переменная счетчик
if num % 2 == 0:
    counter = counter + 1
if num1 % 2 == 0:
    counter = counter + 1
if num2 % 2 == 0:
    counter = counter + 1
print(counter)