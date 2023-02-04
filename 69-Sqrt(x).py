
def mySqrt(x):
    k = x / 2  # initial value

    while abs(k * k - x) >= 0.1:
        k = k - (k * k - x) / (2 * k)  # update
    return int(k)


x = 16
print(mySqrt(x))

