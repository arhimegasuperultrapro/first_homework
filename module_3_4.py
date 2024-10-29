def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    start_other_words = other_words                 # создаем список чтобы функция вернула слова с учетом регистра
    other_words = [x.lower() for x in other_words]  # а чтобы сравнивать строки из списка с первым параметром уберем заглавные буквы
    same_words= []
    for i in range(len(other_words)):
        if other_words[i] in root_word or root_word in other_words[i]:
            same_words.append(start_other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)