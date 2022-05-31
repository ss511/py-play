"""
Largest Rectangular Area in a Histogram

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of
contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.
For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}.
The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)

 6           6
|-|  5   5  |-|
| | |-|4|-| | |
| | | |-| | | |
| |2| | | | | |
| |-| | | |1| |
|_|_|_|_|_|_|_|

"""


def get_largest_area_v1(histogram):
    n = len(histogram)
    stack = list()

    max_area = 0
    index = 0

    while index < n:
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()

            area = (histogram[top_of_stack] * (index - stack[-1] - 1) if stack else index)

            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        max_area = max(max_area, area)
    return max_area


def get_largest_area_v2(histogram):
    n = len(histogram)
    left_smaller = [-1]*n
    right_smaller = [n]*n
    stack = [-1]
    index = 0
    max_area = 0
    while index < n:
        while stack and stack[-1] != -1 and histogram[stack[-1]] >= histogram[index]:
            right_smaller[stack[-1]] = index
            stack.pop()
        if index > 0 and histogram[index] == histogram[index - 1]:
            left_smaller[index] = left_smaller[index - 1]
        else:
            left_smaller[index] = stack[-1]
        stack.append(index)
        index += 1
    for i in range(0, n):
        max_area = max(max_area, histogram[i] * (right_smaller[i] - left_smaller[i] - 1))
    return max_area


if __name__ == "__main__":
    histogram1 = [6, 2, 5, 4, 5, 1, 6]
    histogram2 = [6, 2, 5, 5, 6]
    histogram3 = [6, 2, 5, 2, 5, 2, 2]

    print("Largest area for histogram1 using v1: {}".format(get_largest_area_v1(histogram1)))
    print("Largest area for histogram2 using v1: {}".format(get_largest_area_v1(histogram2)))
    print("Largest area for histogram3 using v1: {}".format(get_largest_area_v1(histogram3)))

    print("Largest area for histogram1 using v2: {}".format(get_largest_area_v2(histogram1)))
    print("Largest area for histogram2 using v2: {}".format(get_largest_area_v2(histogram2)))
    print("Largest area for histogram3 using v2: {}".format(get_largest_area_v2(histogram3)))







