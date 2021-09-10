def find_duplicate(arr):
    """
    Given an array of size n+1 and items ranging from 1 to n, find the duplicate number present in the array.
    :param arr: array where duplicate has to be found.
    :return: duplicate item
    """
    if len(arr) <= 0:
        return -1

    # for i in range(len(arr)):
    #     arr[abs(arr[i])] = -arr[abs(arr[i])]
    #     print(arr[arr[i]])
    #     if arr[abs(arr[i])] > 0:
    #         return abs(arr[i])

    for i in range(len(arr)):
        j = abs(arr[i])
        if arr[j] >= 0:
            arr[j] = -arr[j]
        else:
            return j


if __name__ == "__main__":
    input_arr = [5, 2, 4, 2, 1, 3]
    print(f"Duplicate value is {find_duplicate(input_arr)}")
