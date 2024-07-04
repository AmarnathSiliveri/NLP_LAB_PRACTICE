#porter stemmer

from nltk.stem import PorterStemmer
ps=PorterStemmer()
example_words =["work","working","worked","worker"]
for w in example_words:
    print(ps.stem(w))