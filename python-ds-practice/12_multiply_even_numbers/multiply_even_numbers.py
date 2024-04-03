def multiply_even_numbers(nums):
    result = 1  
    
    for num in nums:
        if num % 2 == 0:  
            result *= num
    
    return result if result != 1 else 1 