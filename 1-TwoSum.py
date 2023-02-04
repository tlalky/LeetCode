
def twosum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        seek = target - num
        if seek in seen:
            return [seen[seek], i]
        seen[num] = i
    return []


nums = [3, 3]
target = 6
print(twosum(nums, target))
