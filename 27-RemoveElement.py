def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return nums

"""    i = 0
    for elem in nums:
        if elem != val:
            nums[i] = elem
            i += 1
    return i"""


"""    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = "_"
    nums = str(nums)
    returning = []
    for i in range(len(nums)):
        if nums[i].isdigit():
            returning.append(int(nums[i]))

    return returning"""



nums = [0,1,2,2,3,0,4,2]
val = 2



print(removeElement(nums, val))


