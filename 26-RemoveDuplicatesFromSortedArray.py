def removeDuplicates(nums):
    nums[:] = sorted(set(nums))
    return nums


"""
    nums = sorted(set(nums))
    nums = list(nums)
    return nums"""


"""   returning = []
    for elem in nums:
        if elem not in returning:
            returning.append(elem)

    return returning
"""



nums = [1,1,2,4,5,32,432,12,3,2,3,5]

print(removeDuplicates(nums))
