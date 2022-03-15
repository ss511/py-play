"""
Giving a dictionary and a string ‘str’, find the longest string in dictionary which can be formed by deleting some characters of the given ‘str’.
Examples:

Input : dict = {"ale", "apple", "monkey", "plea"}
        str = "abpcplea"
Output : apple

Input  : dict = {"pintu", "geeksfor", "geeksgeeks",
                                        " forgeek"}
         str = "geeksforgeeks"
Output : geeksgeeks

"""


def is_subsequence(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    if len1 > len2 or len1 == len2 and word1 != word2:
        return False
    i, j = 0, 0
    while i < len1 and j < len2:
        if word1[i] == word2[j]:
            i += 1
            j += 1
        else:
            j += 1
        if i == len1:
            return True
    return False


def find_longest_word(word_list, word):
    word_list.sort(key=len, reverse=True)
    for w in word_list:
        if is_subsequence(w, word):
            return w
    return "No matching word found."


if __name__ == "__main__":
    words = ["ale", "apple", "monkey", "plea", "extremely", "extreme"]
    inp_word = 'abpcplea'

    print(find_longest_word(words, inp_word))