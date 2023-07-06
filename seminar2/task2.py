a = 1
b = 1
fib = int(input())
i = 1
while a < fib or b < fib:
    if a > b:
        b = b + a
    else:
        a = a + b
    i += 1

if a == fib or b == fib:
    print(i)
else:
    print(-1)