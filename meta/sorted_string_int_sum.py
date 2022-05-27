"""
Rearrange a string in sorted order followed by the integer sum

Difficulty Level : Easy
Last Updated : 28 Apr, 2021
Given a string containing uppercase alphabets and integer digits (from 0 to 9), the task is to print the alphabets in the order followed by the sum of digits.


Examples:

Input : AC2BEW3
Output : ABCEW5
Alphabets in the lexicographic order
followed by the sum of integers(2 and 3).
"""


MAX_CHAR = 26


def sorted_string_int_sum(text):
    char_count = [0] * MAX_CHAR
    total = 0

    for i in range(len(text)):
        if "A" <= text[i] <= "Z":
            char_count[ord(text[i]) - ord("A")] += 1
        else:
            total += ord(text[i]) - ord("0")

    res = ""
    for i in range(MAX_CHAR):
        ch = chr(ord("A") + i)
        print(ch)
        while char_count[i]:
            res += ch
            char_count[i] -= 1

    if total > 0:
        res += str(total)
    return res


if __name__ == "__main__":
    print(sorted_string_int_sum("AC2BEW3"))
    print(sorted_string_int_sum("ACC0BEW3"))
    print(sorted_string_int_sum("AAACCBBBBBEWW"))
