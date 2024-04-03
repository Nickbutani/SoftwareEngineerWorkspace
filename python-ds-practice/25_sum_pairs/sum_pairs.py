def sum_pairs(nums, goal):
    seen = set()
    for num in nums:
        diff = goal - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
    return []