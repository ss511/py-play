"""
Smallest subarray with sum greater than a given value

Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
"""


def get_min_sum_sub_array(arr, x):
    start = -1
    end = -1
    i = 0
    j = 0
    while i < len(arr):
        temp_start = -1
        temp_end = -1
        temp_sum = 0
        while temp_sum <= x and i < len(arr):
            temp_sum += arr[i]
            temp_end = i
            i += 1
        if i == len(arr) and temp_sum <= x and start == -1 and end == -1:
            return "Sub Array Doesn't Exist."
        while temp_sum > x and j < len(arr):
            temp_start = j
            temp_sum -= arr[j]
            j += 1
        if start == -1 and end == -1 and temp_start != -1 and temp_end != -1:
            start = temp_start
            end = temp_end
        if temp_end - temp_start < end - start:
            start = temp_start
            end = temp_end
    return arr[start:end+1]


if __name__ == "__main__":
    arr1 = [1, 4, 45, 6, 0, 19]
    x1 = 51
    arr2 = [1, 10, 5, 2, 7]
    x2 = 9
    arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
    x3 = 280
    arr4 = [1, 2, 4]
    x4 = 8

    print(get_min_sum_sub_array(arr1, x1))
    print(get_min_sum_sub_array(arr2, x2))
    print(get_min_sum_sub_array(arr3, x3))
    print(get_min_sum_sub_array(arr4, x4))
