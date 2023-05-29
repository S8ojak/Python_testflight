n = int(input())
nn = str(n) + str(n) # переводим в строчный формат чтобы сложить 9 и 9 и чтоб получилось не 18 а 99
nnn = str(n) + str(n) + str(n)
print(int(n) + int(nn) + int(nnn))
print(nn)
print(nnn)