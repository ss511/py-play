def search(arr, key):
    n = len(arr)
    if n < 1:
        return False

    low, high = 0, n-1

    mid = n//2
    if arr[mid] == key:
        return True
    if arr[low] <= arr[mid]:
        if arr[low] <= key <= arr[mid]:
            return search(arr[low:mid], key)
        else:
            return search(arr[mid+1:high+1], key)
    else:
        if arr[mid] <= key < arr[high]:
            return search(arr[mid+1:high+1], key)
        else:
            return search(arr[low:mid], key)


if __name__ == "__main__":
    """
    Algo to perform binary search in circularly sorted array.
    """
    input_arr = [5, 7, 8, 9, 1, 2, 3]
    x = int(input())
    print("Is X present in array: ", search(input_arr, x))
