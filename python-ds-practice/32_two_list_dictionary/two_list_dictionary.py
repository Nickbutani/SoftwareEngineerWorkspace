def two_list_dictionary(keys, values):
    return {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}