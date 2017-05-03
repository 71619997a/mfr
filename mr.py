import re

def getWords(filename):
    with open(filename) as f:
        spl = re.sub('[^\w]', ' ', f.read())
    return re.sub('[ \t\n]+', ' ', spl).split()

def frequency(word, words):
    return len(filter(lambda w: w == word, words))

def frequencies(wordgroup, words):
    return len(filter(lambda w: w in wordgroup, words))

def mostfrequent(words):
    def biggest(a, b):
        if a[1] > b[1]:
            return a
        return b
    return reduce(biggest, map(lambda a: (a, frequency(a, words)), set(words)))[0]

if __name__ == '__main__':
    words = getWords('book.txt')
    print 'Frequency of me:', frequency('me', words)
    print 'Total frequency of me, him, and her:', frequencies(['me', 'him', 'her'], words)
    mfw = mostfrequent(words)  # xd
    print 'Most frequent word: %s, frequency: %d' % (mfw, frequency(mfw, words))