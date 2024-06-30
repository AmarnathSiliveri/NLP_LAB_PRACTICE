# To remove stop words from the given text

from nltk.corpus import stopwords
stoplist=stopwords.words('english')
text="Hii, hello Namaste Dosto.NLP stands for NATURAL LANGUAGE PROCESSING "
clean_words=[word for word in text.split() if word not in stoplist]
print(text)
print("NEW text",end="--->")
print(clean_words)


### output
#   Hii, hello Namaste Dosto.NLP stands for NATURAL LANGUAGE PROCESSING 
#   NEW text--->['Hii,', 'hello', 'Namaste', 'Dosto.NLP', 'stands', 'NATURAL', 'LANGUAGE', 'PROCESSING']