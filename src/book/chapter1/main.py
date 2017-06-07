from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)


def percentage(count, total):
    return 100 * count / total

def characteristics(text, min_len, min_counts):
    fdist = FreqDist(text)
    V = set(text)
    long_words = [w for w in V if len(w) > min_len and fdist[w] > min_counts]
    print("%d words bigger then %d characters and min count of %d" % (len(long_words), min_len, min_counts))
    for word in sorted(long_words):
        print("%-100s  char : %5d    occurences : %5d" % (word, len(word), fdist[word]))

    print("%d words bigger then %d characters and min count of %d" % (len(long_words), min_len, min_counts))


if __name__ == "__main__":
    characteristics(text1, 7, 100)