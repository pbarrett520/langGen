import pytest
from phones import  *
import re

test_object = Phones('voiced_consonants.csv', 'voiceless_consonants.csv', 'vowels.csv',
syll_struct = r"[ptkbdgθð]?[aeiouʌæ]?[aeiouʌæ][ptkbdgθð]?[ptkbdgθð]?")
def test_func():

    test_inventory = test_object.make_sylls(10)

    assert len(test_object.syll_inventory) == 10

    for i in test_inventory:
        assert re.match(test_object.syll_struct, i)