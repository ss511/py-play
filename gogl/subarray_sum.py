"""
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33
or
Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Output: Sum found between indexes 1 and 4
Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7
or
Input: arr[] = {1, 4}, sum = 0
Output: No sub-array found
There is no sub-array with 0 sum
"""


def find_sub_array_sum(arr, sum):
    arr_len = len(arr)
    i = 0
    while i < arr_len:
        j = i+1
        temp_sum = arr[i]
        while temp_sum <= sum and j < arr_len:
            temp_sum += arr[j]
            j += 1
            if temp_sum == sum:
                return arr[i:j]
        i += 1
    return "Sub Array not Found."


if __name__ == "__main__":
    arr1 = [1, 3, 20, 3, 10, 5]
    sum1 = 33
    arr2 = [1, 4, 0, 0, 3, 10, 5]
    sum2 = 7
    arr3 = [1, 4]
    sum3 = 0

    print("Sub Array for Arr1: ", find_sub_array_sum(arr1, sum1))
    print("Sub Array for Arr2: ", find_sub_array_sum(arr2, sum2))
    print("Sub Array for Arr3: ", find_sub_array_sum(arr3, sum3))