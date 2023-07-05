number = int(input())

n1 = number // 100000
n2 = number // 10000 % 10
n3 = number // 1000 % 10
n4 = number // 100 % 10
n5 = number // 10 % 10
n6 = number % 10


if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')

