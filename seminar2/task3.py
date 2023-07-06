count_watermelon = int(input())
max = 1
min = float('inf')
for i in range(count_watermelon):
    mass = int(input())
    if mass > max:
        max = mass
    if mass < min:
        min = mass

print(max, min)