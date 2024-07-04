### number of male and female names in the names corpus
from nltk.corpus import names
print("\n number df male names")
print(len(names.words('male.txt')))
print("\n number df male names")
print(len(names.words('female.txt')))
male_names=names.words('male.txt')
female_names=names.words('female.txt')
print("\n First 10 male names")
print(male_names[0:10])
print("\n First 10 female names")
print(female_names[0:10])


### outputs
""" number df male names
2943

 number df male names
5001

 First 10 male names
['Aamir', 'Aaron', 'Abbey', 'Abbie', 'Abbot', 'Abbott', 'Abby', 'Abdel', 'Abdul', 'Abdulkarim']       

 First 10 female names
['Abagael', 'Abagail', 'Abbe', 'Abbey', 'Abbi', 'Abbie', 'Abby', 'Abigael', 'Abigail', 'Abigale']      """