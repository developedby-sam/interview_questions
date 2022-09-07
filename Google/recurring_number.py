# Given an array, find the first recurring number
# Example: array => [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array [2, 3, 4, 5]
# It should return undefined

def find_recurring_number(arr):
    hash_array = []
    for num in arr:
        if num in hash_array:
            return num
        hash_array.append(num)
    return None


print(find_recurring_number([2, 3, 4, 5]))
