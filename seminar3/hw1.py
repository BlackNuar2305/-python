n = [int(i) for i in input().split()]
x = int(input())
count = 0

for i in range(len(n)):
    if n[i] == x:
        count += 1
print(count)