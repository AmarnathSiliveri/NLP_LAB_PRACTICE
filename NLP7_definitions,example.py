## defination and meaning of a specific word
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
syns=wordnet.synsets('fight')
print("definition")
print(syns[0].definition())
print("example")
print(syns[0].examples())

# output

#   definition
#       a hostile meeting of opposing military forces in the course of a war
#   example
#       ['Grant won a decisive victory in the battle of Chickamauga', 'he lost his romantic ideas about war when he got into a real engagement']