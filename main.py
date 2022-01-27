import nltk
from nltk.corpus import words

nltk.download('words')
word_list = words.words()
not_in_list = ['']
in_list = ['']
for i in word_list:
    if len(i) == 5 and 'n' in i[3] and all(character_in_list in i for character_in_list in in_list) and all(
            character not in i for character in not_in_list):
        print(i)

        
