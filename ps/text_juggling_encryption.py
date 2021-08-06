"""
An English text needs to be encrypted using the following encryption scheme.
floor(sqr(len(s))) <= row <= col <= ceil(sqr(len(s)))
i/p - haveaniceday
o/p - hae and via ecy
"""

import math
import os


def encryption(s):
    s = "".join(s.split())
    sqr_n = math.sqrt(len(s))
    col = math.ceil(sqr_n)
    print(s)
    res = ""
    for i in range(0, col):
        print(i)
        print(s[i::col])
        res += s[i::col] + " "
    return res


if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result + '\n')
