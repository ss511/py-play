"""
Given two strings, the task is to check whether these strings are meta strings or not.
Meta strings are the strings which can be made equal by exactly one swap in any of the strings.
Equal string are not considered here as Meta strings.
Examples:
Input : str1 = "geeks"
        str2 = "keegs"
Output : Yes
By just swapping 'k' and 'g' in any of string,
both will become same.

Input : str1 = "rsting"
        str2 = "string
Output : No

Input :  str1 = "Converse"
         str2 = "Conserve"
Output : Yes
"""


def is_strings_meta(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    if len1 != len2:
        return False

    misaligned_count = 0
    m_index1 = -1
    m_index2 = -1
    i = 0
    while i < len1:
        if word1[i] != word2[i]:
            misaligned_count += 1
            if m_index1 != -1:
                m_index2 = i
            else:
                m_index1 = i
        i += 1

    return misaligned_count == 2 and word1[m_index1] == word2[m_index2] and word1[m_index2] == word2[m_index1]


if __name__ == "__main__":
    print(is_strings_meta("geeks", "keegs"))
    print(is_strings_meta("rsting", "string"))
    print(is_strings_meta("Converse", "Conserve"))
    print(is_strings_meta("Converse", "Conservation"))
    print(is_strings_meta("Program", "Program"))
    print(is_strings_meta("Mine", "Dime"))


