#text sentence to split into a list of words
import nltk
nltk.download('punkt')
text="this is an example sentence,words"
split_words=nltk.word_tokenize(text)
print(split_words)


### output

['this', 'is', 'an', 'example', 'sentence', ',', 'words']