"""
Given an array, find the subarray (containing at exact k numbers) which has the largest sum.
Examples:
Input : arr[] = {-4, -2, 1, -3}
            k = 2
Output : -1
The sub array is {-2, 1}

Input : arr[] = {1, 1, 1, 1, 1, 1}
            k = 2
Output : 6
The sub array is {1, 1, 1, 1, 1, 1}
"""


def get_largest_sum_sub_array(arr):
    curr_max = arr[0]
    output_sum = arr[0]
    n = len(arr)

    for i in range(1, n):
        curr_max = max(arr[i], curr_max+arr[i])
        output_sum = max(output_sum, curr_max)

    return output_sum


def get_k_largest_sum_sub_array(arr, k):
    output_sum = arr[0]
    output_defined = False
    n = len(arr)

    for i in range(0, n-k+1):
        temp_sum = arr[i]
        for j in range(i+1, i+k):
            temp_sum += arr[j]
        output_sum = max(output_sum, temp_sum) if output_defined else temp_sum
        output_defined = True
    return output_sum


if __name__ == "__main__":
    arr1 = [-4, -2, 1, -3]
    arr2 = [1, 1, 1, 1, 1, 1]
    arr3 = [-2, -3, 4, -1, -2, 1, 5, -3]
    arr4 = [5, -1, -2, -1, 4]
    arr5 = [5, 7, -9, 3, -4, 2, 1, -8, 9, 10]

    print("Largest Sum for {} is {}".format(arr1, get_largest_sum_sub_array(arr1)))
    print("Largest Sum for {} is {}".format(arr2, get_largest_sum_sub_array(arr2)))
    print("Largest Sum for {} is {}".format(arr3, get_largest_sum_sub_array(arr3)))
    print("Largest Sum for {} is {}".format(arr4, get_largest_sum_sub_array(arr4)))
    print("Largest Sum for {} is {}".format(arr5, get_largest_sum_sub_array(arr5)))

    print("Largest Sum for {}, limit to {} is {}".format(arr1, 2, get_k_largest_sum_sub_array(arr1, 2)))
    print("Largest Sum for {}, limit to {} is {}".format(arr2, 6, get_k_largest_sum_sub_array(arr2, 6)))
    print("Largest Sum for {}, limit to {} is {}".format(arr3, 2, get_k_largest_sum_sub_array(arr3, 2)))
    print("Largest Sum for {}, limit to {} is {}".format(arr4, 2, get_k_largest_sum_sub_array(arr4, 2)))
    print("Largest Sum for {}, limit to {} is {}".format(arr5, 5, get_k_largest_sum_sub_array(arr5, 5)))
