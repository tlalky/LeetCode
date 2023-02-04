def generate(numRows):
    res = [[1]]  # first layer of pascal triangle

    for i in range(numRows - 1):  # so we need n-1 rows now
        temp = [0] + res[-1] + [0]  # add zeros in front and at the end of row
        row = []
        for j in range(len(res[-1]) + 1):  # loop going through elems of previous row
            row.append(temp[j] + temp[j + 1])  # appending sum of elems to row array
        res.append(row)  # appending row to result
    return res


num = 5
print(generate(num))




