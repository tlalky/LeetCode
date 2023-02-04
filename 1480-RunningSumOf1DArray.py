def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

"""
    output = [nums[0]]
    for i in range(1, len(nums)):
        output.append(nums[i] + output[i-1])
    return output"""




nums = [1,2,3,4]
print(runningSum(nums))
