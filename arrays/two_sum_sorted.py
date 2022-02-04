"""
Given a sorted array and a target sum, find two numbers in the array which equals the target sum.
One solution uses map, another traverses the array from front and back simultaneously.
"""


def find_two_sum(arr, n):
    temp_dict = dict()
    for x in range(len(arr)):
        temp = arr[x]
        if temp_dict.get(n-temp) is None:
            temp_dict[temp] = x
        else:
            return x, temp_dict[n-temp]
    return -1, -1


def find_two_sum_no_extra_space(arr, n):
    size = len(arr)
    j = size-1
    x = 0
    while x in range(size):
        if arr[x] + arr[j] == n:
            return x, j
        elif arr[x] + arr[j] > n:
            j -= 1
        else:
            x += 1
    return -1, -1


if __name__ == "__main__":
    sorted_arr = [2, 3, 4, 5, 7, 10, 11]
    target_sum = 17
    i, j = find_two_sum(sorted_arr, target_sum)
    print("Index Are: ", i, j)
    print("Index Are: ", find_two_sum_no_extra_space(sorted_arr, target_sum))
