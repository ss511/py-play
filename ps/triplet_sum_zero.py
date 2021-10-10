def triplet_sum_zero(arr):
    """
    This function returns the all triplets in an arr whose sum is 0.
    The list must not have duplicate triplets pair, if though the item index for those could be different.
    Example:
    For input - [-1, 0, 1, 2, -1, -4]
    Result without removing duplicate will be - [[-1, 0, 1], [-1, -1, 2], [-1, 0, 1]]
    But the result should be [[-1, 0, 1], [-1, -1, 2]]
    This program uses sorting technique and O(n^2) time complexity without using extra space for computation.
    Extra space is only used to store results obviously.

    :param arr: the arr where triplets needs to be find.
    :return: triplets as a lists of list.
    """
    triplets = list()
    arr_len = len(arr)
    arr.sort()

    for i in range(0, arr_len):
        triplet = list()
        j = i+1
        k = arr_len-1
        while j < k:
            if arr[i] + arr[j] + arr[k] == 0:
                triplet.extend([arr[i], arr[j], arr[k]])
                triplets.append(triplet)
                triplet = list()
                j += 1
                k -= 1
            elif arr[i] + arr[j] + arr[k] < 0:
                j += 1
            else:
                k -= 1

    return list(map(list, set(map(tuple, triplets))))


if __name__ == "__main__":
    print(triplet_sum_zero([-1, 0, 1, 2, -1, -4]))
    print(triplet_sum_zero([]))
    print(triplet_sum_zero([0]))
