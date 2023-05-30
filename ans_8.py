def findErrorNums(nums):
    numSet = set()
    duplicate = 0
    missing = 0
    
    for num in nums:
        if num in numSet:
            duplicate = num
        numSet.add(num)
    
    for i in range(1, len(nums) + 1):
        if i not in numSet:
            missing = i
            break
    
    return [duplicate, missing]

nums = [1,2,2,4]
result = findErrorNums(nums)
print(result)