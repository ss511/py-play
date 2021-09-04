"""
Radix sort works for arrays with huge min and max value. It uses count_sort as a subroutine, but acts on digit.
"""


def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        arr = count_sort(arr, exp)
        exp *= 10
    return arr


def count_sort(arr, exp):
    count_arr = [0 for _ in range(0, 10)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        index = arr[i] // exp
        count_arr[index % 10] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] // exp
        output_arr[count_arr[index % 10] - 1] = arr[i]
        count_arr[index % 10] -= 1

    return output_arr


if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
