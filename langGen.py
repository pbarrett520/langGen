import re
from itertools import product
from random import sample

vowels = ['a','e','i','o','u','']
cons = ['p','t','k','b','d','g',"'",'y','w','r','l','n','m','']
syll_stuct = re.compile(r"([ptkbdg'ywrlnm]?)[aeiou]?[aeiou]([nm]?)")
cartesian_product = list(product(cons,cons,vowels,vowels,cons,cons))

def join_tuple_strings(list_of_tuples):
    return (''.join(list_of_tuples))

potential_sylls = list(map(join_tuple_strings, cartesian_product))

sylls = []

for item in potential_sylls:
    syll = re.match(syll_stuct,item)
    
    if syll != None and syll.group() not in sylls:
        sylls.append(syll.group())

print(sorted(sample(sylls, 250)))