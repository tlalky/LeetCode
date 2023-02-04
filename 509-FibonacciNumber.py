def fib(n):
    if n <= 1:
        return n
    one, two = 0, 1
    for i in range(n):
        one, two = one + two, one
    return one




n = 3
print(fib(n))
