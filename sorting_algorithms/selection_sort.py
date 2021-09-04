"""
Finds the min element in each pass and
exchange it with ith value which is conceived to be the min in starting of each pass.
"""


def selection_sort(arr):
    arr_size = len(arr)
    for i in range(arr_size-1):
        min_id = i
        for j in range(i, arr_size):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i], arr[min_id] = arr[min_id], arr[i]

    return arr


if __name__ == "__main__":
    print(selection_sort([5, 2, 1, 8, 7, 4, 6]))
