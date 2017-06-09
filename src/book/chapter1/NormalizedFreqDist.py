from nltk.book import *


def freqdist_normalize(text):
    fdist = FreqDist([len(w) for w in text])
    tmp = fdist.copy()
    norm = len(text)
    for key in tmp.keys():
        tmp[key] = float(fdist[key]) / norm
    tmp.plot(50)


if __name__ == "__main__":
    freqdist_normalize(text1)