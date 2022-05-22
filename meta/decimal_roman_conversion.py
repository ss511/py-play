"""
Given an integer, the task is to write a Python program to convert integer to roman.

Examples:

Input: 5
Output: V

Input: 9
Output: IX

Input: 40
Output: XL

Input:  1904
Output: MCMIV
"""


def convert_to_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    i = 12
    roman = ""
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            roman += sym[i]
            div -= 1
        i -= 1
    return roman


if __name__ == "__main__":
    num1 = 3549
    num2 = 124
    num3 = 910
    num4 = 450
    num5 = 789
    num6 = 91
    num7 = 54
    num8 = 40
    num9 = 12
    num10 = 24
    num11 = 7
    num12 = 5

    print(convert_to_roman(num1))
    print(convert_to_roman(num2))
    print(convert_to_roman(num3))
    print(convert_to_roman(num4))
    print(convert_to_roman(num5))
    print(convert_to_roman(num6))
    print(convert_to_roman(num7))
    print(convert_to_roman(num8))
    print(convert_to_roman(num9))
    print(convert_to_roman(num10))
    print(convert_to_roman(num11))
    print(convert_to_roman(num12))
