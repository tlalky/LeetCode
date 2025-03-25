def romanToInt(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for a, b in zip(s, s[1:]):
        if values[a] < values[b]:
            result -= values[a]
        else:
            result += values[a]
    return result + values[s[-1]]


print(romanToInt("MCMXCIV"))


# def romanToInt(s: str) -> int:
#     values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').
#                                                           replace('CD', 'CCCC').replace('CM', 'DCCCC')
#     for char in s:
#         result += values[char]
#     return result
