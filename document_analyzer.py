import re
import string
from string import punctuation
from operator import itemgetter

def count_word():

    N = 100
    words = {}

    words_gen = (word.strip(punctuation).lower() for line in open("document.txt")
                 for word in line.split())

    for word in words_gen:
        words[word] = words.get(word, 0) + 1

    top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:N]

    list=top_words[0:5]
    for word, frequency in list:
        print("%s %d" % (word, frequency))



if __name__ == '__main__':
    count_word()