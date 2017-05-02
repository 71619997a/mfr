import re

def getWords(filename):
    with open(filename) as f:
        spl = re.sub('[^\w]', ' ', f.read())
    return re.sub('[ \t\n]+', ' ', spl).split()


def frequency(word, words):
    return len(filter(lambda w: w == word, words))

def frequencies(wordgroup, words):
    return len(filter(lambda w: w in wordgroup, words))

def mostfrequent(wordgroup, words):
    def biggest(a, b):
        if a[1] > b[1]:
            return a
        return b
    return reduce(biggest, map(lambda a: (a, frequency(a, words)), set(words)))

