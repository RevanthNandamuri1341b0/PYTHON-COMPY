import re
dict = {}

def uniqueWord(Word):
    if Word in dict:
        dict[words] += 1
    else:
        dict.update({words: 1})

string = input()
ListOfWords = re.split("[\W]+", string)

for words in ListOfWords:
    uniqueWord(words)

count = 0

for elements in dict:
    if dict[elements] == 1:
        count += 1
print(count)
