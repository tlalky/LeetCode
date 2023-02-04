def fizzBuzz(n):
    array = []
    for i in range(1,n+1):
        if i % 15 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(i))
    return array


n = 15
print(fizzBuzz(n))

