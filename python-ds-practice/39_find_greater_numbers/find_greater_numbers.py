def find_greater_numbers(nums):
    return sum([1 for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[j] > nums[i]])