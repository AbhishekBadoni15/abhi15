def move_zeros(nums):
    non_zero = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zero))
    return non_zero + zeros

print(move_zeros([0, 1, 0, 3, 12])) 
