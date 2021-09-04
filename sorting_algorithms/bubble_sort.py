"""
Simplest sorting algo. Compares the neighbours and interchange them if i+1 is smaller than i.
"""


def bubble_sort(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        for j in range(1, arr_size):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 2, 1, 8, 7, 4, 6]))
