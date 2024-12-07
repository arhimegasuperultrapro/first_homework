
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [x for x in file_names]
    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding="utf-8") as file:
                string_ = file.read().lower()
                for i in string_:
                    if i in  [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        string_ = string_.replace(i, '')
                    if i == "\n":
                        string_ = string_.replace(i, " ")
                string_ = string_.split(" ")
            for num, i in enumerate(string_):
                if string_[num] == '': del string_[num]
            all_words[name] = string_
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        words = self.get_all_words()
        for key in words.keys():
            if word in words[key]:
                positions[key] = words[key].index(word) + 1
        return positions

    def count(self, word):
        word = word.lower()
        word_count = {}
        words = self.get_all_words()
        for key in words.keys():
            if word in words[key]:
                word_count[key] = words[key].count(word)
        return word_count



finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
