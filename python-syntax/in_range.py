def in_range(nums, lowest, highest):
  for num in nums:
    if lowest <= num <= highest:
      print(f"{num} fits")

    # YOUR CODE HERE


in_range([10, 20, 30, 40, 50], 15, 30)            
