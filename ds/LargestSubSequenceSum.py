"""
Finds the largest sum of subsequence in the given array.
Input space separated integer values.
"""


def largest_subsequence(n):

    max_sum = 0
    max_val = int(n[0])

    for x in n[1:len(n)]:
        if int(x) > 0:
            max_sum += int(x)
        elif max_val < int(x) <= 0:
            max_val = int(x)
    return max_sum if max_sum > 0 else max_val


if __name__ == "__main__":
    arr = input().split()
    res = largest_subsequence(arr)
    print(res)
