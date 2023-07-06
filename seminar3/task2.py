numbers = list((int(i) for i in input().split()))
k = int(input())
i = 0

while i < k:
    poped = numbers.pop()
    numbers.insert(0, poped)
    i += 1


print(numbers)