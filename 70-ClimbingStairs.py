def climbStairs(n):
    if n <= 2:
        return n
    one, two = 1, 1
    for i in range(n-1):
        one, two = one + two, one
    return one


n = 2

print(climbStairs(n))


