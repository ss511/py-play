"""
Given an array of size N+1, where the max element in array can be N and min can be 1.
Find out which which all numbers are duplicate
"""


def find_duplicate(arr):
    duplicates = set()

    i = 0
    while i in range(len(arr)):
        j = abs(arr[i])
        if arr[j] < 0:
            duplicates.add(j)
        else:
            arr[j] = -arr[j]
        i += 1

    return duplicates


if __name__ == "__main__":
    duplicates_array = [1, 2, 3, 1, 2, 5, 5]
    print("Duplicate set: ", find_duplicate(duplicates_array))