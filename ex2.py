word = input()
vowels = set("aeiouy")
word_set = set(word.lower())

print('Гласных {}, согласных {}'.format(len(word_set.intersection(vowels)),
                                        len(word_set.difference(vowels))))
