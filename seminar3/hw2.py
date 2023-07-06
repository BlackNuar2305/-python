n = [int(i) for i in input().split()]
x = int(input())
min = float('inf')
k = 0
number = 0
for i in range(len(n)):
    k = abs(x - n[i])
    if k < min:
        min = k
        number = n[i]

print(number)