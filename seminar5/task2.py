length = int(input())
list1 = [int(input()) for i in range(length)]
min = float('inf')
max = 0

for i in list1:
    if i < min:
        min = i
    if i > max:
        max = i



for i in range(len(list1)):
    if list1[i] == max:
        list1[i] = min


print(list1)