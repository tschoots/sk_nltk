import nltk, re, pprint

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    print(sentences)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print(sentences)
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return(sentences)


if __name__ == "__main__":

    #test = "We saw the yellow dog"
    chunk_test = "the little yellow dog barked at the cat"
    sentence = ie_preprocess(chunk_test)
    print(sentence)

    grammar = "NP: {<DT>?<JJ>*<NN>}"
    # This rule says that an NP chunk should be formed whenever the chunker finds an optional determiner (DT) followed by any number of adjectives (JJ) and then a noun (NN)

    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence[0])
    print(result)
    result.draw()