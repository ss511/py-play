"""
A python program to derive the square of already sorted array and maintaining the resulting sorted order.
Example: -4 -2 3 5 -> 4 9 16 25
"""


def array_square_sorted(sorted_arr):

    square_sorted = list()

    x = 0
    for x in range(len(sorted_arr)):
        if sorted_arr[x] >= 0:
            break

    i = x-1
    j = x

    while i >= 0 and j < len(sorted_arr):
        if sorted_arr[i]*sorted_arr[i] < sorted_arr[j]*sorted_arr[j]:
            square_sorted.append(sorted_arr[i]*sorted_arr[i])
            i -= 1
        else:
            square_sorted.append(sorted_arr[j] * sorted_arr[j])
            j += 1

    while i >= 0:
        square_sorted.append(sorted_arr[i]*sorted_arr[i])
        i -= 1
    while j < len(sorted_arr):
        square_sorted.append(sorted_arr[j] * sorted_arr[j])
        j += 1

    return square_sorted


if __name__ == "__main__":
    print("Input Sorted Array, space separated:")
    arr = list(map(int, input().split(" ")))
    print("Input Array is: ", arr)
    print(arr)
    print("Sorted Array after squaring is: ", array_square_sorted(arr))
