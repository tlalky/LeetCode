def addBinary(a, b):
    sum = bin(int(a, 2) + int(b, 2))
    return str(sum)[2:]


a = "11"
b = "1"

print(addBinary(a, b))
