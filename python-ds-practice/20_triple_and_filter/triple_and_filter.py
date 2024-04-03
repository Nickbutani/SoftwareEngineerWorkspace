def triple_and_filter(nums):
    result = [num * 3 for num in nums if num % 4 == 0]
    
    return result