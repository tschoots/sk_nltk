import nltk
from nltk import bigrams
from nltk.collocations import BigramCollocationFinder

if __name__ == "__main__":
    text = "I do not like green eggs and ham, I do not like them Sam I am!"
    tokens = nltk.wordpunct_tokenize(text)
    print("wordpunct : %s" % tokens)
    finder = BigramCollocationFinder.from_words(tokens)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    sorted_col = sorted(bigram for bigram, socre in scored)
    print("sorted : %s" % sorted_col)

    word_fd = nltk.FreqDist(tokens)
    bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
    finder = BigramCollocationFinder(word_fd, bigram_fd)
    word_fd.plot(50)
    bigram_fd.plot(50)