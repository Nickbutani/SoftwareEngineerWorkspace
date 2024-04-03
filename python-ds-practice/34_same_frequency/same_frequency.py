def same_frequency(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) != len(num2):
        return False
    count1 = {}
    count2 = {}
    for val in num1:
        count1[val] = count1.get(val, 0) + 1
    for val in num2:
        count2[val] = count2.get(val, 0) + 1
    for key in count1:
        if count1[key] != count2.get(key, 0):
            return False
    return True