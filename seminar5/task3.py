def simple_number(n):
    k = 2
    while n >= k * k:
        if n % k == 0:
            return 'no'
        k += 1
    return 'yes'

print(simple_number(int(input())))