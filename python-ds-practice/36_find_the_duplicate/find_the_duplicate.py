def find_the_duplicate(nums):
    return [i for i in set(nums) if nums.count(i) > 1][0] if nums else None