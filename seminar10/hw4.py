n = input()
try:
    n = int(n)
except ValueError:
    print('That\'s not an int!')

summa = 0
for i in range(n+1):
    if i % 5 == 0 and i % 3 != 0:
        summa += i

print(summa)