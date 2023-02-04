def searchInsert(nums, target):
    for i, e in enumerate(nums):
        if e >= target:
            return i

    return len(nums)


"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    nums.append(target)
    nums = sorted(nums)

    for i in range(len(nums)):
        if nums[i] == target:
            return i"""


nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))
