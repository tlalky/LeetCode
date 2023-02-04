
def findMedianSortedArrays(nums1, nums2):
    nums = []
    for elem in nums1:
        nums.append(elem)
    for elem in nums2:
        nums.append(elem)
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return float(nums[int((len(nums)-1) / 2)])
    else:
        num1 = nums[int((len(nums)-1)/2)]
        num2 = nums[int((len(nums))/2)]
        suma = (num1 + num2) / 2
        return float(suma)



nums1 = [1,2,3, 4.5, 5]
nums2 = [3,4,5]
print(findMedianSortedArrays(nums1, nums2))

