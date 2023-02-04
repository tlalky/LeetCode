def myAtoi(s):
    result = ""
    for char in s:
        if char == "-" and result == "":
            result += char

        if char == "-" and "-" in result:
            return 0

        if char.isdigit():
            result += char

    return result


# this code is wrong !!!!


s = "  -    4193 with words    "
print(myAtoi(s))

