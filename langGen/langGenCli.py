import re
from itertools import product
from random import sample

vowels = input('Enter vowel inventory (no spaces): ')
cons = input('Entr consonant inventory (no spaces): ')
syll_stuct = input('Enter regex for permissible phomeme pattern: ')
cv_struct = input('Enter consonant-vowel pattern of syllables (ex: CV, CVC, etc.): ')

vowels = vowels.split()
cons = cons.split()
syll_stuct = re.compile(syll_stuct)
cartesian_product = list(product(cons,vowels,cons))

def join_tuple_strings(list_of_tuples):
    return (''.join(list_of_tuples))

potential_sylls = list(map(join_tuple_strings, cartesian_product))

sylls = []

for item in potential_sylls:
    syll = re.match(syll_stuct,item)
    
    if syll != None and syll.group() not in sylls:
        sylls.append(syll.group())

print(sorted(sample(sylls,205)))