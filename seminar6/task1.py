n = int(input())
array1 = [int(input()) for i in range(n)]
m = int(input())
array2 = [int(input()) for i in range(m)]

i = 0
while i < len(array1):
    if array1[i] in array2:
        array1.pop(i)
    else:
        i += 1


print(array1)
