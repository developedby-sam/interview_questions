def merge_two_sorted_array(array1, array2):

    if not array1:
        return array2
    if not array2:
        return array1

    merged_array = []
    array1_length = len(array1)
    array2_length = len(array2)
    i = 0
    j = 0

    while (i < array1_length) and (j < array2_length):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    while i < array1_length:
        merged_array.append(array1[i])
        i += 1

    while j < array2_length:
        merged_array.append(array2[j])
        j += 1

    return merged_array


print(merge_two_sorted_array([1, 3, 7, 9], [2, 7, 8]))
