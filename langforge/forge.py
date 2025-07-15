"""
Main Forge class for LangForge language generation.

This module contains the primary API entry point for generating constructed languages.
"""

import random
from typing import List, Dict, Any


class SyllablePatterns:
    """
    Linguistically accurate syllable patterns for different language families.

    These patterns are designed to generate realistic syllable structures
    rather than filtering through Cartesian products.
    """

    # Polynesian: Simple (C)V structure, very open syllables
    polynesian = {
        "name": "Polynesian",
        "structure": ["V", "CV"],  # Just V or CV - realistic!
        "consonants": ["p", "t", "k", "f", "s", "h", "m", "n", "ŋ", "l", "w", "j"],
        "vowels": ["a", "e", "i", "o", "u"],
        "weights": [0.2, 0.8],  # Favor CV over V
    }

    # Chinese-style: (C)V(C) with limited finals
    sinitic = {
        "name": "Sinitic",
        "structure": ["V", "CV", "VC", "CVC"],
        "consonants": [
            "p",
            "t",
            "k",
            "b",
            "d",
            "g",
            "f",
            "s",
            "ʃ",
            "m",
            "n",
            "ŋ",
            "l",
            "ɻ",
            "j",
            "w",
        ],
        "vowels": ["a", "e", "i", "o", "u", "ə"],
        "final_consonants": ["n", "ŋ", "k", "t", "p"],  # Limited finals
        "weights": [0.1, 0.4, 0.2, 0.3],
    }

    # Germanic: Complex consonant clusters, diverse vowels
    germanic = {
        "name": "Germanic",
        "structure": ["V", "CV", "VC", "CVC", "CCV", "CCVC", "CVCC", "CCVCC"],
        "consonants": [
            "p",
            "t",
            "k",
            "b",
            "d",
            "g",
            "f",
            "θ",
            "s",
            "ʃ",
            "h",
            "m",
            "n",
            "ŋ",
            "l",
            "r",
            "w",
            "j",
        ],
        "vowels": ["i", "ɪ", "e", "ɛ", "æ", "ʌ", "ə", "ɑ", "ɔ", "o", "ʊ", "u"],
        "cluster_initials": [
            "bl",
            "br",
            "fl",
            "fr",
            "gl",
            "gr",
            "kl",
            "kr",
            "pl",
            "pr",
            "sl",
            "sp",
            "st",
            "sk",
            "tr",
            "tw",
            "sw",
        ],
        "cluster_finals": ["st", "nt", "nd", "mp", "nk", "lt", "rt", "ft"],
        "weights": [0.05, 0.25, 0.15, 0.35, 0.10, 0.07, 0.02, 0.01],
    }

    # Romance: Open syllables, specific clusters
    romance = {
        "name": "Romance",
        "structure": ["V", "CV", "CVC", "CCV"],
        "consonants": [
            "p",
            "t",
            "k",
            "b",
            "d",
            "g",
            "f",
            "s",
            "m",
            "n",
            "ɲ",
            "l",
            "ʎ",
            "r",
            "ɾ",
        ],
        "vowels": ["a", "e", "i", "o", "u"],
        "cluster_initials": [
            "bl",
            "br",
            "fl",
            "fr",
            "gl",
            "gr",
            "kl",
            "kr",
            "pl",
            "pr",
            "tr",
            "dr",
        ],
        "final_consonants": ["n", "r", "l", "s"],
        "weights": [0.15, 0.60, 0.15, 0.10],
    }

    # Japanese: Very simple CV structure
    japanese = {
        "name": "Japanese",
        "structure": ["V", "CV", "CVC"],
        "consonants": [
            "k",
            "g",
            "s",
            "z",
            "t",
            "d",
            "n",
            "h",
            "b",
            "p",
            "m",
            "j",
            "r",
            "w",
        ],
        "vowels": ["a", "i", "u", "e", "o"],
        "final_consonants": ["n"],  # Only /n/ can be final
        "weights": [0.10, 0.85, 0.05],
    }

    @staticmethod
    def generate_random_pattern():
        """Generate a completely random syllable pattern each time it's called."""

        # Pool of all possible phonemes
        ALL_CONSONANTS = [
            "p",
            "t",
            "k",
            "q",
            "b",
            "d",
            "g",
            "ɢ",
            "f",
            "θ",
            "s",
            "ʃ",
            "x",
            "χ",
            "h",
            "ħ",
            "ʔ",
            "v",
            "ð",
            "z",
            "ʒ",
            "ɣ",
            "ʁ",
            "ʕ",
            "m",
            "n",
            "ɲ",
            "ŋ",
            "ɴ",
            "l",
            "ʎ",
            "ʟ",
            "r",
            "ɾ",
            "ʀ",
            "w",
            "j",
            "ɥ",
            "ʍ",
            "tʃ",
            "dʒ",
            "ts",
            "dz",
            "ʈ",
            "ɖ",
            "ɳ",
            "ɭ",
            "ɻ",
            "c",
            "ɟ",
            "ç",
            "ʝ",
        ]

        ALL_VOWELS = [
            "a",
            "e",
            "i",
            "o",
            "u",
            "ɑ",
            "ɛ",
            "ɪ",
            "ɔ",
            "ʊ",
            "ə",
            "ɨ",
            "ʉ",
            "ɯ",
            "y",
            "ø",
            "œ",
            "æ",
            "ɐ",
            "ɒ",
            "ʌ",
            "ɤ",
            "ɵ",
            "ɶ",
            "ɘ",
            "ɜ",
            "ɞ",
            "ɚ",
            "ɝ",
        ]

        # Randomly select consonants (5-25)
        consonant_count = random.randint(5, 25)
        consonants = random.sample(ALL_CONSONANTS, consonant_count)

        # Randomly select vowels (3-15)
        vowel_count = random.randint(3, 15)
        vowels = random.sample(ALL_VOWELS, vowel_count)

        # Randomly choose syllable structures
        possible_structures = [
            "V",
            "CV",
            "VC",
            "CVC",
            "CCV",
            "VCC",
            "CCVC",
            "CVCC",
            "CCVCC",
        ]
        structure_count = random.randint(2, 8)
        structures = random.sample(possible_structures, structure_count)

        # Generate random weights
        weights = [random.random() for _ in structures]
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]

        # Randomly decide final consonant restrictions
        has_final_restrictions = random.choice([True, False])
        pattern = {
            "name": "Random",
            "structure": structures,
            "consonants": consonants,
            "vowels": vowels,
            "weights": weights,
        }

        if has_final_restrictions:
            final_count = random.randint(1, min(5, len(consonants)))
            pattern["final_consonants"] = random.sample(consonants, final_count)

        return pattern

    @staticmethod
    def random():
        """Generate a truly random pattern each time."""
        return SyllablePatterns.generate_random_pattern()


class SyllableGenerator:
    """Smart syllable generator that builds syllables according to patterns."""

    def __init__(self, pattern: Dict[str, Any]):
        """Initialize generator with a syllable pattern."""
        self.pattern = pattern

    def generate_syllables(self, count: int) -> List[str]:
        """Generate a list of syllables following the pattern."""
        syllables = []

        for _ in range(count):
            # Choose syllable structure based on weights
            structure = random.choices(
                self.pattern["structure"], weights=self.pattern.get("weights", None)
            )[0]

            syllable = self._build_syllable(structure)
            syllables.append(syllable)

        return syllables

    def _build_syllable(self, structure: str) -> str:
        """Build a single syllable with the given structure."""
        result = ""

        for i, slot in enumerate(structure):
            if slot == "C":
                # Choose consonant (consider position)
                if i == len(structure) - 1 and "final_consonants" in self.pattern:
                    # Final position - use limited set if available
                    consonant = random.choice(self.pattern["final_consonants"])
                else:
                    # Initial/medial position
                    consonant = random.choice(self.pattern["consonants"])
                result += consonant
            elif slot == "V":
                vowel = random.choice(self.pattern["vowels"])
                result += vowel

        return result


class GeneratedLanguage:
    """A generated constructed language with phonological and lexical properties."""

    def __init__(self, template: str = "random"):
        """Initialize a generated language."""
        self.template = template
        self._generate_phonology(template)
        self._generate_syllables()
        self._generate_vocabulary()

    def _generate_phonology(self, template: str):
        """Generate the phonological system."""
        # Map template names to patterns
        if template == "polynesian":
            pattern = SyllablePatterns.polynesian
        elif template in ["sinitic", "sino-tibetan"]:
            pattern = SyllablePatterns.sinitic
        elif template == "germanic":
            pattern = SyllablePatterns.germanic
        elif template == "romance":
            pattern = SyllablePatterns.romance
        elif template == "japanese":
            pattern = SyllablePatterns.japanese
        else:
            pattern = SyllablePatterns.random()  # Call method for truly random

        self.phonology = {
            "template": template,
            "pattern": pattern,
            "consonants": pattern["consonants"],
            "vowels": pattern["vowels"],
        }

        self._syllable_generator = SyllableGenerator(pattern)

    def _generate_syllables(self):
        """Generate a sample of syllables for this language."""
        self.syllables = self._syllable_generator.generate_syllables(20)

    def _generate_vocabulary(self):
        """Generate basic vocabulary structure."""
        # Placeholder for now - will be expanded
        self.vocabulary = {"size": 0, "words": [], "concepts": {}}


class Forge:
    """
    Main LangForge class for language generation.

    This class provides the primary interface for generating constructed languages,
    including phonological systems, vocabularies, and linguistic structures.
    """

    def __init__(self):
        """Initialize a new Forge instance."""
        pass

    def generate(self, template: str = "random") -> GeneratedLanguage:
        """
        Generate a complete constructed language.

        Args:
            template: Language family template to use ("random", "polynesian", "sinitic", etc.)

        Returns:
            GeneratedLanguage instance with phonology, syllables, and vocabulary
        """
        return GeneratedLanguage(template)

    def morphemes(
        self, template: str = "random", type: str = "roots", count: int = 20
    ) -> List[str]:
        """
        Generate morphemes using existing syllable patterns.

        Args:
            template: Language family template to use
            type: Type of morphemes ("roots" or "affixes")
            count: Number of morphemes to generate

        Returns:
            List of morpheme strings
        """
        # Create a language to get consistent phoneme inventory
        language = self.generate(template)
        syllable_gen = language._syllable_generator

        # Generate morphemes with appropriate lengths
        morphemes = []
        for _ in range(count):
            # Determine morpheme length based on language and type
            length = self._get_morpheme_length(template, type)

            # Generate syllables and combine into morpheme
            syllables = syllable_gen.generate_syllables(length)
            morpheme = "".join(syllables)
            morphemes.append(morpheme)

        return morphemes

    def _get_morpheme_length(self, template: str, type: str) -> int:
        """Determine syllable count for morpheme based on language and type."""

        if type == "roots":
            if template == "japanese":
                return random.choices([1, 2, 3], weights=[0.1, 0.7, 0.2])[
                    0
                ]  # Favor 2-syllable
            elif template == "polynesian":
                return random.choices([1, 2], weights=[0.6, 0.4])[
                    0
                ]  # Favor 1-syllable, simpler
            elif template == "germanic":
                return random.choices([1, 2], weights=[0.6, 0.4])[0]
            elif template == "romance":
                return random.choices([1, 2, 3], weights=[0.2, 0.6, 0.2])[0]
            elif template == "sinitic":
                return random.choices([1, 2], weights=[0.7, 0.3])[0]
            else:  # random
                return random.choices([1, 2, 3], weights=[0.4, 0.4, 0.2])[0]

        elif type == "affixes":
            # Most affixes are single syllables across languages
            return 1

        else:
            # Default to single syllable
            return 1

    def __repr__(self):
        """Return a string representation of the Forge instance."""
        return f"Forge(version='{__import__('langforge').__version__}')"

    def build_words(self, template: str = "random", count: int = 20, strategy: str = "mixed") -> List[str]:
        """
        Build words by combining morphemes using different strategies.
        
        Args:
            template: Language family template to use
            count: Number of words to generate
            strategy: Word building strategy ("simple", "complex", "mixed")
            
        Returns:
            List of generated words
        """
        words = []
        
        # Generate morpheme pools
        roots = self.morphemes(template, type="roots", count=count * 2)
        affixes = self.morphemes(template, type="affixes", count=count)
        
        for _ in range(count):
            word = self._build_single_word(template, strategy, roots, affixes)
            words.append(word)
            
        return words
    
    def _build_single_word(self, template: str, strategy: str, roots: List[str], affixes: List[str]) -> str:
        """Build a single word using the specified strategy."""
        import random
        
        if strategy == "simple":
            # Simple strategy: mostly single morphemes
            if random.random() < 0.8:
                return random.choice(roots)
            else:
                # Occasionally add a simple affix
                root = random.choice(roots)
                affix = random.choice(affixes)
                return root + affix if random.random() < 0.5 else affix + root
                
        elif strategy == "complex":
            # Complex strategy: prefer multiple morphemes
            root = random.choice(roots)
            
            # Add 1-3 affixes
            num_affixes = random.choices([1, 2, 3], weights=[0.5, 0.4, 0.1])[0]
            affixes_to_add = random.sample(affixes, min(num_affixes, len(affixes)))
            
            # Randomly place affixes before or after root
            result = root
            for affix in affixes_to_add:
                if random.random() < 0.3:  # Prefix
                    result = affix + result
                else:  # Suffix
                    result = result + affix
            return result
            
        else:  # mixed strategy
            # Mix of simple and complex
            if random.random() < 0.6:
                return self._build_single_word(template, "simple", roots, affixes)
            else:
                return self._build_single_word(template, "complex", roots, affixes)
    
    def generate_swadesh(self, template: str = "random", count: int = 50) -> 'SwadeshList':
        """
        Generate a Swadesh list with words for core concepts.
        
        Args:
            template: Language family template to use
            count: Number of concepts to generate words for
            
        Returns:
            SwadeshList instance with concept-to-word mappings
        """
        swadesh = SwadeshList()
        
        # Get the first 'count' concepts from the core list
        concepts_to_generate = SwadeshList.CORE_CONCEPTS[:count]
        
        # Generate a word pool using different strategies for variety
        simple_words = self.build_words(template, count=count//3, strategy="simple")
        complex_words = self.build_words(template, count=count//3, strategy="complex") 
        mixed_words = self.build_words(template, count=count - len(simple_words) - len(complex_words), strategy="mixed")
        
        all_words = simple_words + complex_words + mixed_words
        
        # Assign words to concepts
        import random
        random.shuffle(all_words)  # Randomize word assignment
        
        for i, concept in enumerate(concepts_to_generate):
            if i < len(all_words):
                swadesh.add_concept(concept, all_words[i])
            else:
                # Generate additional word if needed
                extra_word = self.build_words(template, count=1, strategy="mixed")[0]
                swadesh.add_concept(concept, extra_word)
                
        return swadesh
    
    def export(self, swadesh: 'SwadeshList', filepath: str, format: str = None, 
               include_metadata: bool = False, language: 'GeneratedLanguage' = None) -> None:
        """
        Export Swadesh list and optionally language data to file.
        
        Args:
            swadesh: SwadeshList to export
            filepath: Path to output file
            format: Export format ("csv", "json", or None for auto-detect)
            include_metadata: Whether to include language metadata (JSON only)
            language: GeneratedLanguage instance for metadata
        """
        import os
        import csv
        import json
        
        # Auto-detect format from file extension if not specified
        if format is None:
            _, ext = os.path.splitext(filepath)
            if ext.lower() == '.csv':
                format = 'csv'
            elif ext.lower() == '.json':
                format = 'json'
            else:
                raise ValueError(f"Cannot auto-detect format from extension: {ext}")
        
        # Validate format
        if format not in ['csv', 'json']:
            raise ValueError(f"Unsupported format: {format}. Use 'csv' or 'json'")
        
        if format == 'csv':
            self._export_csv(swadesh, filepath)
        elif format == 'json':
            self._export_json(swadesh, filepath, include_metadata, language)
    
    def _export_csv(self, swadesh: 'SwadeshList', filepath: str) -> None:
        """Export Swadesh list to CSV format."""
        import csv
        
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Concept', 'Word'])  # Header
            
            for concept, word in swadesh.to_dict().items():
                writer.writerow([concept, word])
    
    def _export_json(self, swadesh: 'SwadeshList', filepath: str, 
                     include_metadata: bool = False, language: 'GeneratedLanguage' = None) -> None:
        """Export Swadesh list and optionally language metadata to JSON format."""
        import json
        
        data = {
            'swadesh': swadesh.to_dict()
        }
        
        if include_metadata and language:
            data['language_info'] = {
                'template': language.template,
                'phonology': {
                    'consonants': language.phonology['consonants'],
                    'vowels': language.phonology['vowels'],
                    'pattern_name': language.phonology['pattern']['name']
                },
                'syllable_count': len(language.syllables),
                'vocabulary_size': language.vocabulary['size']
            }
        
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)


class SwadeshList:
    """
    Swadesh concept-to-word mappings for cross-linguistic comparison.
    
    The Swadesh list contains 207 core concepts that are considered
    universal across human languages, providing a basis for vocabulary
    generation and cross-linguistic comparison.
    """
    
    # Organized by semantic categories for maintainability and future features
    CONCEPT_CATEGORIES = {
        "pronouns_basic": [
            "I", "you", "we", "this", "that", "who", "what", "where", "when", "how",
            "not", "all", "many", "some", "few", "other"
        ],
        
        "numbers": [
            "one", "two", "three", "four", "five"
        ],
        
        "body_parts": [
            "head", "hair", "eye", "nose", "mouth", "tooth", "tongue", "fingernail",
            "foot", "leg", "knee", "hand", "neck", "breast", "heart", "liver", "blood"
        ],
        
        "nature_environment": [
            "water", "fire", "sun", "moon", "star", "earth", "stone", "tree", "forest",
            "mountain", "cloud", "rain", "wind", "snow", "ice", "smoke", "ash", "sand",
            "night", "day", "shadow", "lightning", "thunder", "fog", "dew"
        ],
        
        "animals_life": [
            "dog", "fish", "bird", "snake", "worm", "louse", "spider", "ant", "mosquito",
            "egg", "horn", "tail", "feather", "wing", "claw", "animal", "meat", "fat", "bone"
        ],
        
        "actions_verbs": [
            "eat", "drink", "bite", "suck", "spit", "vomit", "blow", "breathe", "laugh",
            "see", "hear", "know", "think", "smell", "fear", "sleep", "live", "die", "kill",
            "fight", "hunt", "hit", "cut", "split", "stab", "scratch", "dig", "swim", "fly",
            "walk", "come", "lie", "sit", "stand", "turn", "fall", "give", "hold", "squeeze", "rub"
        ],
        
        "descriptors_properties": [
            "big", "long", "wide", "thick", "heavy", "small", "short", "narrow", "thin",
            "woman", "man", "person", "child", "wife", "husband", "mother", "father",
            "red", "green", "yellow", "white", "black", "hot", "cold", "full", "new", "old",
            "good", "bad", "rotten", "dirty", "straight", "round", "sharp", "dull", "smooth",
            "wet", "dry", "correct", "near", "far", "right", "left", "at", "in", "with"
        ],
        
        "materials_objects": [
            "leaf", "root", "bark", "flower", "fruit", "seed", "grass", "rope", "skin",
            "grease", "salt", "dust", "name", "say", "sing", "float", "flow",
            "freeze", "swell", "river", "lake", "sea", "sky", "path", "road", "year",
            "when", "if", "because", "count", "tie", "sew", "push", "pull",
            "throw", "wash", "wipe", "choose", "work"
        ]
    }
    
    # Flatten all categories into the standard 207-concept list
    CORE_CONCEPTS = [
        concept 
        for category in CONCEPT_CATEGORIES.values() 
        for concept in category
    ]
    
    def __init__(self):
        """Initialize an empty SwadeshList."""
        self.concepts: Dict[str, str] = {}
    
    def add_concept(self, concept: str, word: str) -> None:
        """
        Add a concept-to-word mapping.
        
        Args:
            concept: The semantic concept (e.g., "water")
            word: The generated word for this concept (e.g., "mizu")
            
        Raises:
            TypeError: If concept or word is not a string
        """
        if not isinstance(concept, str):
            raise TypeError(f"Concept must be a string, got {type(concept)}")
        if not isinstance(word, str):
            raise TypeError(f"Word must be a string, got {type(word)}")
            
        self.concepts[concept] = word
    
    def get_word(self, concept: str) -> str:
        """
        Get the word for a given concept.
        
        Args:
            concept: The concept to look up
            
        Returns:
            The word mapped to this concept, or None if not found
        """
        return self.concepts.get(concept)
    
    def to_dict(self) -> Dict[str, str]:
        """Return the concept mappings as a dictionary."""
        return self.concepts.copy()
    
    def __len__(self) -> int:
        """Return the number of concept mappings."""
        return len(self.concepts)
    
    def __contains__(self, concept: str) -> bool:
        """Check if a concept is in the list."""
        return concept in self.concepts
    
    def __iter__(self):
        """Iterate over the concept names."""
        return iter(self.concepts.keys())
