def hammingWeight(n):
    n = str(bin(n))
    suma = 0
    for i in range(len(n)):
        if n[i] == "1":
            suma += 1
    return suma


"""
        n = str(bin(n)).count('1')
        return n
"""


n = 0b1011

print(hammingWeight(n))




