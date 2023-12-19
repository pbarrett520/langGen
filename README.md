# LangGen: One Dev's Quixotic Quest to Write a Conlang Generator in Python

This project is my humble attempt to try to emulate some of the functionalities in the very cool program [VulgarLang](https://www.vulgarlang.com/how-it-works/).

# Features so far:

- logic for reading csv files of phonemes, placing consonants into grouping by both place and manner of articulation
- additional logic for parsing csv files with vowels into ordered groupings based on their properties
- a simple utility for generating syllable vocabularies of an arbitrary length

# Features to be implemented:

- the ability to create syllables of arbitrary consonant-vowel structure
- a more user-friendly system for defining syllable structure that doesn't rely on regex
- a utility which will combine generated syllables into words

# Demo:

Instantiate an object by passing in the paths for the voiceless consonants, voiced consonants, and vowels, as well as the regex to define the desired syllable structure, like so:

```python3
demo_object = Phones('voiced_consonants.csv', 'voiceless_consonants.csv', 'vowels.csv',
    syll_struct= "[ptkbdgθð]?[aeiouʌæ]?[aeiouʌæ][ptkbdgθð]?[ptkbdgθð]?")
```

Specific categories of phonemes can be seen by calling the corresponding attribute. For example, to see all bilabial consonants:

```python3
demo_object.bilabial

['b', 'm', 'ʙ', 'β', 'p', 'ɸ']
```
To see all consonants or vowels, simply call:
```python3
demo_object.all_consonants
# Or
demo_object.all_vowels
```

To generate a vocabulary of syllables:
```python3
test_inventory = test_object.make_sylls(10)

['doaʔ', 'doɘɮ', 'duɶʋ', 'dʌɔç', 'pʌok', 'pʌɑʁ', 'taʊɰ', 'tʌʉβ', 'ðaɑm', 'ðiœq']
```

Thank you to anyone who shows any interest or support in this project.