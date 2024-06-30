## synonyms and antonyms of a given word

from nltk.corpus import wordnet
synonyms=[]
antonyms=[]
for syn in wordnet.synsets("work"):
    for l in syn.lemmas():
        synonyms.append(l.name())
    if l.antonyms():
        antonyms.append(l.antonyms()[0].name())
        

print('\n set of synonyms of the said word:')
print(set(synonyms))
print('\n set of antonyms of the said word:')
print(set(antonyms))

## output
 #set of synonyms of the said word:
{'turn', 'body_of_work', 'lick', 'study', 'work_on', 'shape', 'employment', 'cultivate', 'operate', 'put_to_work', 'solve', 'forge', 'figure_out', 'act', 'work_out', 'oeuvre', 'workplace', 'exploit', 'function', 'puzzle_out', 'mold', 'piece_of_work', 'go', 'do_work', 'wreak', 'ferment', 'mould', 'sour', 'exercise', 'play', 'process', 'crop', 'work', 'bring', 'knead', 'make', 'act_upon', 'influence', 'form', 'run', 'make_for'}

#set of antonyms of the said word:
{'idle'}
