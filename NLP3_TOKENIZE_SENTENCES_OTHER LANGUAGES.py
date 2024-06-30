import nltk
from nltk.tokenize import sent_tokenize

def tokenize_sentences_in_other_Languages(text,language='english'):
    if language not in nltk.corpus.stopwords.fileids():
        print(f"Language '{language}' not found in NLTK stopwords corpus.")
    else:
        sentences=sent_tokenize(text,language)
        return sentences
    
# English text
english_text = "Hii, hello, namaste. NLP is used to derive insights from text."
print("English sentences:", tokenize_sentences_in_other_Languages(english_text, language='english'))
print()
# Spanish text
spanish_text = "¡Hola, hello, namaste! NLP se utiliza para obtener información de texto."
print("Spanish sentences:", tokenize_sentences_in_other_Languages(spanish_text, language='spanish'))
print()
# German text
german_text = "Hallo, hello, namaste. NLP wird verwendet, um Erkenntnisse aus Text zu gewinnen."
print("German sentences:", tokenize_sentences_in_other_Languages(german_text, language='german'))
print()


#### outputs
#   English sentences: ['Hii, hello, namaste.', 'NLP is used to derive insights from text.']

#   Spanish sentences: ['¡Hola, hello, namaste!', 'NLP se utiliza para obtener información de texto.']

#   German sentences: ['Hallo, hello, namaste.', 'NLP wird verwendet, um Erkenntnisse aus Text zu gewinnen.']