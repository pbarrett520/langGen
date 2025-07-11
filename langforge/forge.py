"""
Main Forge class for LangForge language generation.

This module contains the primary API entry point for generating constructed languages.
"""

import random
from typing import List, Dict, Any


class ImprovedSyllablePatterns:
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

    # Random: More variety for testing
    random = {
        "name": "Random",
        "structure": ["V", "CV", "VC", "CVC", "CCV", "CCVC"],
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
            "θ",
            "ð",
        ],
        "vowels": ["a", "e", "i", "o", "u", "ə", "ɑ", "ɛ", "ɪ", "ʊ"],
        "weights": [0.1, 0.3, 0.2, 0.25, 0.1, 0.05],
    }


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
            pattern = ImprovedSyllablePatterns.polynesian
        elif template in ["sinitic", "sino-tibetan"]:
            pattern = ImprovedSyllablePatterns.sinitic
        else:
            pattern = ImprovedSyllablePatterns.random

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

    def __repr__(self):
        """Return a string representation of the Forge instance."""
        return f"Forge(version='{__import__('langforge').__version__}')"
