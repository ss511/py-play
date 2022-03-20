def get_triplet_sum(arr):
    triplet_sum = list()

    arr.sort()
    print(arr)

    arr_len = len(arr)
    for i in range(arr_len):
        left = i + 1
        right = arr_len - 1

        while left < right:
            if arr[i] + arr[left] + arr[right] == 0:
                triplet_sum.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif arr[i] + arr[left] + arr[right] > 0:
                right -= 1
            else:
                left += 1

    return triplet_sum


if __name__ == "__main__":
    arr1 = [0, -1, 2, -3, 1]
    arr2 = [1, -2, 1, 0, 5]
    arr3 = [1, 3, 4, 0, 5]
    arr4 = [-5, 2, 3, 1, 4]

    print("Triplet Zero Sum for arr1 is ", get_triplet_sum(arr1))
    print("Triplet Zero Sum for arr2 is ", get_triplet_sum(arr2))
    print("Triplet Zero Sum for arr3 is ", get_triplet_sum(arr3))
    print("Triplet Zero Sum for arr4 is ", get_triplet_sum(arr4))
