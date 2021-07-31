def twosum(nums, target):
    length = len(nums)
    j = 0
    for i in range(length):
        tmp = nums[i+1:]
        if target - nums[i] in tmp:
            j = tmp.index(target - nums[i])+i+1
            break
    return i, j

print(twosum([1,3,4,5,5],10))

