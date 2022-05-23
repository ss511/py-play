"""
An encoded string (s) is given, the task is to decode it. The pattern in which the strings are encoded is as follows.

<count>[sub_str] ==> The substring 'sub_str'
                      appears count times.

Examples:

Input : str[] = "1[b]"
Output : b

Input : str[] = "2[ab]"
Output : abab

Input : str[] = "2[a2[b]]"
Output : abbabb

Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca
"""


def decode_string(text):
    num_st = []
    string_st = []
    result = ""
    i = 0
    while i < len(text):
        count = 0
        if '0' <= text[i] <= '9':
            while '0' <= text[i] <= '9':
                count = count * 10 + ord(text[i]) - ord('0')
                i += 1
            i -= 1
            num_st.append(count)
        elif text[i] == ']':
            temp = ""
            count = 0
            if len(num_st) != 0:
                count = num_st[-1]
                num_st.pop()
            while len(string_st) != 0 and string_st[-1] != "[":
                temp = string_st[-1] + temp
                string_st.pop()
            if len(string_st) != 0 and string_st[-1] == "[":
                string_st.pop()
            temp_res = ""
            while count > 0:
                temp_res += temp
                count -= 1
            string_st.append(temp_res)
        elif text[i] == '[':
            if '0' <= text[i - 1] <= '9':
                string_st.append(text[i])
            else:
                string_st.append(text[i])
                num_st.append(1)
        else:
            string_st.append(text[i])
        i += 1

    while len(string_st) != 0:
        result = string_st[-1] + result
        string_st.pop()
    return result


if __name__ == "__main__":
    print(decode_string("1[b]"))
    print(decode_string("2[ab]"))
    print(decode_string("2[a2[b]]"))
    print(decode_string("3[b2[ca]]"))