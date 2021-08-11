import re

"""
Program to get word count from a paragraph.
"""


class DS:

    def __init__(self):
        self.count_map = {}

    def get_count_map(self, para):
        clean_text = re.sub(r'[^\w\s]', "", para)
        words = clean_text.split()
        for word in words:
            if word in self.count_map:
                self.count_map[word] += 1
            else:
                self.count_map[word] = 1

        max_word = max(self.count_map, key=self.count_map.get)
        return self.count_map, max_word, self.count_map.get(max_word)


if __name__ == "__main__":

    input_para = input("Input text: ")
    ds = DS()

    word_count, max_word, max_count = ds.get_count_map(input_para)
    print("Following unique words are present in the input para")

    print(list(word_count.keys()))
    for word in word_count:
        print(word, " - ", word_count[word])

    print(f"Word {max_word} contains the highest count of {max_count}")

