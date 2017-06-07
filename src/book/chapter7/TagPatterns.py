import nltk, re, pprint

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    print(sentences)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print(sentences)
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return(sentences)


if __name__ == "__main__":


    #chunk_test = "another sharp dive trade figures any new policy measures earlier stages Panamanian dictator Manuel Noriega"
    chunk_test = "his Mansion House speech the price cutting 3% to 4% more than 10% the fastest developing trends 's skill"
    sentence = ie_preprocess(chunk_test)
    print(sentence)

    grammar = "NP: {<DT>?<JJ.*>*<NN.*>+}"
    # This will chunk any sequence of tokens beginning with an optional determiner, followed by zero or more adjectives of any type (including relative adjectives like earlier/JJR), followed by one or more nouns of any type

    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence[0])
    print(result)
    result.draw()