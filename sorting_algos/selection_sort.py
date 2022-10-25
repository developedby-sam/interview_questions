# TIME COMPLEXITY O(N) --> SPACE COMPLEXITY O(1)
def selection_sort(num_list):
    length = len(num_list)

    for i in range(length):
        smallest = i

        # We do not have to check element before the i-th element
        # because it is tracked by the smallest varaible
        # Check from the element next to the i-th element
        for j in range(i + 1, length):
            if  num_list[j] < num_list[smallest]:
                smallest = j

        # swap smallest element with the i-the index since all the item before that has been sorted.
        num_list[i], num_list[smallest] = num_list[smallest], num_list[i]

    return num_list


print(selection_sort([10, 4, 18, 16, 3, 1, 6, 14, 9, 7, 11, 12, 20, 8, 13])) 