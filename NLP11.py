#nltk lemmatizer
from nltk.stem import WordNetLemmatizer
lemmatizer =WordNetLemmatizer()
print("reads:",lemmatizer.lemmatize("reads"))
print("mice:",lemmatizer.lemmatize("mice"))
print("worse:",lemmatizer.lemmatize("worse",pos="a"))
print("hero:",lemmatizer.lemmatize("hero"))