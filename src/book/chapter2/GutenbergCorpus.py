from nltk.corpus import gutenberg

if __name__ == "__main__":
    emma = gutenberg.words('austen-emma.txt')

    for fileid in gutenberg.fileids():
        num_chars = len(gutenberg.raw(fileid))
        num_words = len(gutenberg.words(fileid))
        num_sents = len(gutenberg.sents(fileid))
        num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
        print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)