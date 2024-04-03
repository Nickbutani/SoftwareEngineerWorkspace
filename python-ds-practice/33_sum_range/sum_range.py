def sum_range(nums, start=0, end=None):
    return sum(nums[start:end]) if end else sum(nums[start:])