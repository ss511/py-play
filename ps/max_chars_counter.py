char_dict = {}
text = input()
print(text)
for x in sorted(text):
    char_dict[x] = char_dict.get(x, 0) + 1
dict_keys = sorted(char_dict, key=char_dict.get, reverse=True)
for key in dict_keys[:3]:
    print(key, char_dict[key])
