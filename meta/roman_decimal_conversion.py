"""
Given a Roman numeral, the task is to find its corresponding decimal value.

Example :

Input: IX
Output: 9
IX is a Roman symbol which represents 9

Input: XL
Output: 40
XL is a Roman symbol which represents 40

Input: MCMIV
Output: 1904
M is a thousand,
CM is nine hundred and
IV is four
"""


roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_decimal(val):
    result = 0
    n = len(val)

    i = 0
    while i < n:
        if i != n-1 and roman[val[i]] < roman[val[i+1]]:
            result += roman[val[i+1]] - roman[val[i]]
            i += 2
            continue
        else:
            result += roman[val[i]]
        i += 1
    return result


if __name__ == "__main__":
    r1 = "MCMIV"
    r2 = "XL"
    r3 = "L"
    r4 = "CLI"
    print(roman_to_decimal(r1))
    print(roman_to_decimal(r2))
    print(roman_to_decimal(r3))
    print(roman_to_decimal(r4))