import nltk, re, pprint
from nltk import bigrams

def sentence_parsing(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    return(sentences)


if __name__ == "__main__":
    #sentences = sentence_parsing("more is said then done")
    classifier_char_nr = 25
    sentence = "The red wine tasted wonderfull"
    print("%-50s : %s" % ("sentence", sentence))
    sentences = sentence_parsing(sentence)
    print("parsed sentence : %s" % sentences)
    bigrams_list = nltk.text.Text(bigrams(sentences[0]))
    print("bigrams : %s" % bigrams_list)
    col = bigrams_list.collocations()
    print(col)


