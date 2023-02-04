def plusOne(digits):
    returning = ""
    digits = str(digits)
    for i in range(len(digits)):
        if digits[i].isdigit():
            returning += digits[i]

    returning = int(returning)
    returning += 1
    returning = str(returning)
    lista = []
    for i in range(len(returning)):
        lista.append(int(returning[i]))
    return lista


digits = [9, 9]
print(plusOne(digits))

"""returning = ""
digits = str(digits)
for i in range(len(digits)):
    if digits[i].isdigit():
        returning += digits[i]

returning = int(returning)
returning += 1
return returning

digits[-1] = digits[-1] + 1
returning = ""
digits = str(digits)
for i in range(len(digits)):
    if digits[i].isdigit():
        returning += digits[i]

return returning

"""