def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

print(majority_element([1, 2, 3, 2, 2, 2, 5])) 
