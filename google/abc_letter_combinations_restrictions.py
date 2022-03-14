"""
Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’
with at-most one ‘b’ and two ‘c’s allowed.

Example
Input : n = 3
Output : 19
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb

Input  : n = 4
Output : 39

"""


def prepare_word(word, count, b_count, c_count, total):

    letters = ['a', 'b', 'c']
    if b_count == 0 and c_count == 0:
        letters.remove('b')
        letters.remove('c')
    elif b_count == 0:
        letters.remove('b')
    elif c_count == 0:
        letters.remove('c')

    if count == 0:
        return 1

    temp = total
    for letter in letters:
        if letter == 'a':
            total += prepare_word(word+letter, count-1, b_count, c_count, temp)
        elif letter == 'b':
            total += prepare_word(word+letter, count-1, b_count-1, c_count, temp)
        else:
            total += prepare_word(word+letter, count-1, b_count, c_count-1, temp)
    return total


if __name__ == "__main__":
    n = 4
    b_limit = 1
    c_limit = 2
    sum = 0
    sum += prepare_word('a', n-1, b_limit, c_limit, 0)
    sum += prepare_word('b', n-1, b_limit-1, c_limit, 0)
    sum += prepare_word('c', n-1, b_limit, c_limit-1, 0)
    print("Total Combination based on problem constraint is: ", sum)




