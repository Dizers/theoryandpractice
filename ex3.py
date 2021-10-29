file = open("words.txt").read().split()
word = ""
len_word = 0
for w in file:
    l = len(w)
    if l > len_word:
       word = w
       len_word = l
print(word)