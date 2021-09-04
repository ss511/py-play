"""
Counting Sort.
"""


def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    elements_range = max_element-min_element+1

    count_arr = [0 for _ in range(elements_range)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        count_arr[arr[i]-min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i]-min_element] - 1] = arr[i]
        count_arr[arr[i]-min_element] -= 1

    return output_arr


if __name__ == "__main__":
    print(count_sort([1, 0, 1, 3, 1, 3]))
    print(count_sort([1, 4, 1, 2, 7, 5, 2]))
