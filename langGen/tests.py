import pytest
from phones import  *
import re

test_object_custom_regex = Phones('voiced_consonants.csv', 'voiceless_consonants.csv', 'vowels.csv',
syll_struct = r"[ptkbdgθð]?[aeiouʌæ]?[aeiouʌæ][ptkbdgθð]?[ptkbdgθð]?")

test_object_syllable_template = Phones('voiced_consonants.csv', 'voiceless_consonants.csv', 'vowels.csv',
syll_struct=Syllable_patterns.polyneisian)

print(test_object_syllable_template.make_sylls(10))
def test_make_sylls():

    test_inventory_1 = test_object_custom_regex.make_sylls(10) # generate a small syllable inventory

    assert len(test_object_custom_regex.syll_inventory) == 10 # make sure the number of elements is correct

    for i in test_inventory_1:
        assert re.match(test_object_custom_regex.syll_struct, i) # make sure syllables match pattern

def test_syllable_patterns():

    test_inventory_2 = test_object_custom_regex.make_sylls(10)


    for i in test_inventory_2:
        assert re.match(test_object_custom_regex.syll_struct, i)