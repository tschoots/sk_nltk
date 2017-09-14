from nltk.book import text2

if __name__ == "__main__":
    tricky = sorted(w for w in set(text2) if 'cie' in w or 'cei' in w)
    for word in tricky:
        print(word, end=' ')   #end= overides default cariage return linefeed

