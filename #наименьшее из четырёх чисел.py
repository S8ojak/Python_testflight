# наименьшее из четырёх чисел
a, b, c, d = int(input()), int(input()), int(input()), int(input())
ab = a < b or b < a
if a < b:
    ab = a
else:
    ab = b
cd = c < d or d < c
if c < d:
    cd = c
else:
    cd = d
if ab < cd:
    print(ab)
else:
    print(cd)
