"""
Merge Sort Algorithm.
Input - A list with space separated value
Output - Sorted List
"""


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    mid = int(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    arr = merge(left, right)
    return arr


def merge(left, right):
    arr = []

    i = j = 0

    while i < len(left) and j < len(right):
        if int(left[i]) < int(right[j]):
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr


if __name__ == "__main__":
    n = input().split()
    print("List before sorting: ", n)
    print("List after sorting: ", merge_sort(n))
