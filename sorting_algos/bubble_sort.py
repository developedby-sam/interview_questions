# TIME COMPLEXITY O(N) --> SPACE COMPLEXITY O(1)
def bubble_sort(num_list):
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - 1):
            if num_list[j + 1] < num_list[j]:
                num_list[j + 1], num_list[j] = num_list[j], num_list[j + 1]

    return num_list

print(bubble_sort([3, 5, 2, 1, 13, 9, 15, 8]))
print(bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))