length = int(input())
numbers = [int(input()) for i in range(length)]


length = len(numbers) // 2
i = 0
j = len(numbers) - 1


while i < length:
    numbers[i], numbers[j] = numbers[j], numbers[i]
    i += 1
    j -= 1


print(numbers)