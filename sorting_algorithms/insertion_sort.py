"""
Insertion sort finds the items in the iteration smaller than its predecessor and
starts shifting it to its left until the predecessor itself is smaller than itself.

InPlace and Stable Sorting algorithm.
Works wonders if array is sorted and nearly sorted.
"""


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

    return a


if __name__ == "__main__":
    print(insertion_sort([5, 12, 1, 8, 7, 4, 6]))
