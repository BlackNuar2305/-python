a1 = int(input())
d = int(input())
n = int(input())
my_list = [a1]
res = None
i = 2
while i <= n:
    res = a1 + (i - 1) * d
    my_list.append(res)
    i += 1
print(my_list)