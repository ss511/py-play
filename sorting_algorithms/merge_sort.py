def merge_sort(arr):
    """
    Performs the partition of list and also acts as the main core method.
    """
    n = len(arr)
    if n <= 1:
        return arr

    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Performs the merging of two arrays in sorted order.
    :param left: the left side of the list to merged
    :param right: the right side of the list to merged
    :return: sorted merged array
    """
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    i, j = 0, 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if i < len(left):
        sorted_list.extend(left[i: len(left)])
    elif j < len(right):
        sorted_list.extend(right[j: len(right)])

    return sorted_list


if __name__ == "__main__":
    """
    Merge Sort Algorithm written in PYTHON...
    """
    input_arr = list(map(int, input().split()))
    print(input_arr)
    input_arr = merge_sort(input_arr)
    print(input_arr)
