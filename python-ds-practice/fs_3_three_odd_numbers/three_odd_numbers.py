def three_odd_numbers(nums):
    for i in range(len(nums) - 2):
        if sum(nums[i:i + 3]) % 2 != 0:
            return True
    return False
