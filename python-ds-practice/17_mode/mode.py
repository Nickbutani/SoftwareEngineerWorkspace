def mode(nums):
    return max(set(nums), key=nums.count) if nums else None