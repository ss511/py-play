"""
Divide and Conquer. Pick a pivot and partition the array along that pivot.
Pivot element could be first, last, random, or median.
Better than merge sort for arrays since it is in-place.
"""


def quick_sort(start, end, a):
    if start < end:
        p = partition(start, end, a)

        quick_sort(start, p - 1, a)
        quick_sort(p + 1, end, a)


def partition(start, end, a):
    pi = end
    pivot = a[pi]

    while start < end:
        while start < len(a) and a[start] < pivot:
            start += 1
        while a[end] > pivot:
            end -= 1

        if start < end:
            a[start], a[end] = a[end], a[start]

    a[start+1], a[pi] = a[pi], a[start+1]
    return start


# def partition(start, end, a):
#     pi = end
#     pivot = a[pi]
#     i, j = start-1, start
#     while j < pi:
#         if a[j] < pivot:
#             i += 1
#             a[i], a[j] = a[j], a[i]
#         j += 1
#     a[i+1], a[pi] = a[pi], a[i+1]
#     return i+1


a = [5, 12, 1, 8, 7, 4, 6]
quick_sort(0, len(a) - 1, a)
print(a)
