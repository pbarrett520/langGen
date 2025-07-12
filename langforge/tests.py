import pytest
import re
from forge import Forge, SyllablePatterns, SyllableGenerator


class TestForge:
    """Comprehensive test suite for Forge class functionality"""

    def setup_method(self):
        """Set up test fixtures"""
        self.forge = Forge()

        # Test with custom pattern (equivalent to old custom regex)
        self.custom_pattern = {
            "name": "Custom",
            "structure": ["V", "CV", "VC", "CVC"],
            "consonants": ["p", "t", "k", "b", "d", "g", "θ", "ð"],
            "vowels": ["a", "e", "i", "o", "u", "ʌ", "æ"],
            "weights": [0.2, 0.3, 0.2, 0.3],
        }
        self.custom_generator = SyllableGenerator(self.custom_pattern)

        # Test with Polynesian template
        self.polynesian_language = self.forge.generate("polynesian")

    def test_make_sylls_basic_functionality(self):
        """Test basic syllable generation functionality"""
        test_inventory = self.custom_generator.generate_syllables(10)

        # Check return value
        assert len(test_inventory) == 10
        assert all(isinstance(syll, str) for syll in test_inventory)

        # Check that syllables follow expected patterns
        for syll in test_inventory:
            # Should contain only expected phonemes
            assert all(char in "ptkbdgθðaeiouʌæ" for char in syll)

    def test_make_sylls_with_predefined_patterns(self):
        """Test syllable generation with predefined language family patterns"""
        # Test Polynesian pattern
        poly_language = self.forge.generate("polynesian")
        assert len(poly_language.syllables) == 20

        # Polynesian syllables should be simple (C)V patterns
        for syll in poly_language.syllables[:5]:
            assert len(syll) <= 2  # Simple CV or V structure
            # Should contain only Polynesian phonemes
            poly_consonants = set(SyllablePatterns.polynesian["consonants"])
            poly_vowels = set(SyllablePatterns.polynesian["vowels"])
            assert all(char in poly_consonants.union(poly_vowels) for char in syll)

        # Test Sinitic pattern
        sinitic_language = self.forge.generate("sinitic")
        assert len(sinitic_language.syllables) == 20

        for syll in sinitic_language.syllables[:5]:
            # Should contain only Sinitic phonemes
            sinitic_consonants = set(SyllablePatterns.sinitic["consonants"])
            sinitic_vowels = set(SyllablePatterns.sinitic["vowels"])
            sinitic_finals = set(SyllablePatterns.sinitic.get("final_consonants", []))
            all_phonemes = sinitic_consonants.union(sinitic_vowels).union(
                sinitic_finals
            )
            assert all(char in all_phonemes for char in syll)

    def test_make_sylls_edge_cases(self):
        """Test edge cases for syllable generation"""
        # Test different sizes
        single_syll = self.custom_generator.generate_syllables(1)
        assert len(single_syll) == 1

        # Test larger size
        large_inventory = self.custom_generator.generate_syllables(50)
        assert len(large_inventory) == 50

        # All syllables should be valid
        for syll in large_inventory:
            assert isinstance(syll, str)
            assert len(syll) > 0

    def test_phoneme_categorization(self):
        """Test that phonemes are properly categorized in generated languages"""
        # Test with different language templates
        poly_lang = self.forge.generate("polynesian")
        sinitic_lang = self.forge.generate("sinitic")
        random_lang = self.forge.generate("random")

        # Check that phonology information is accessible
        assert len(poly_lang.phonology["consonants"]) > 0
        assert len(poly_lang.phonology["vowels"]) > 0

        # Check specific phonemes for Polynesian
        assert "p" in poly_lang.phonology["consonants"]
        assert "t" in poly_lang.phonology["consonants"]
        assert "a" in poly_lang.phonology["vowels"]
        assert "e" in poly_lang.phonology["vowels"]

        # Check that different templates have different inventories
        assert poly_lang.phonology["consonants"] != sinitic_lang.phonology["consonants"]

    def test_clean_method(self):
        """Test that generated syllables are clean (no invalid characters)"""
        # Generate syllables and check they're clean
        test_inventory = self.custom_generator.generate_syllables(20)

        for syll in test_inventory:
            # No spaces, no empty strings, no special characters
            assert " " not in syll
            assert len(syll) > 0
            assert syll.isascii() or any(
                char in syll for char in "æʌθðŋʃɻəɑɛɪʊ"
            )  # Allow IPA

    def test_syllable_patterns_availability(self):
        """Test that all predefined syllable patterns are available"""
        assert hasattr(SyllablePatterns, "polynesian")
        assert hasattr(SyllablePatterns, "sinitic")
        assert hasattr(SyllablePatterns, "random")
        # Test new patterns
        assert hasattr(SyllablePatterns, "germanic")
        assert hasattr(SyllablePatterns, "romance")
        assert hasattr(SyllablePatterns, "japanese")

        # Test that patterns have required structure
        assert "structure" in SyllablePatterns.polynesian
        assert "consonants" in SyllablePatterns.polynesian
        assert "vowels" in SyllablePatterns.polynesian

    def test_linguistic_realism(self):
        """Test that generated syllables are linguistically realistic"""
        poly_lang = self.forge.generate("polynesian")
        inventory = poly_lang.syllables

        # Check average syllable length is reasonable for Polynesian (should be short)
        avg_length = sum(len(syll) for syll in inventory) / len(inventory)
        assert 1 <= avg_length <= 3  # Polynesian should be simple

        # Check that syllables contain expected phonemes
        all_text = "".join(inventory)
        assert any(char in all_text for char in "aeiou")  # Should have vowels
        assert any(char in all_text for char in "ptkmnl")  # Should have consonants

        # Check that syllables are not all identical (variety test)
        assert len(set(inventory)) > 1  # Should have variety

    def test_reproducibility(self):
        """Test that syllable generation produces valid results consistently"""
        # Generate multiple languages and test consistency
        lang1 = self.forge.generate("polynesian")
        lang2 = self.forge.generate("polynesian")

        # Both should be valid
        assert len(lang1.syllables) == 20
        assert len(lang2.syllables) == 20

        # All should be valid syllables
        for syll in lang1.syllables + lang2.syllables:
            assert isinstance(syll, str)
            assert len(syll) > 0

    def test_new_language_patterns(self):
        """Test new language family patterns work correctly"""
        forge = Forge()

        # Test Germanic - should have complex clusters
        germanic_lang = forge.generate("germanic")
        assert len(germanic_lang.syllables) == 20

        # Germanic should have some complex syllables
        complex_sylls = [s for s in germanic_lang.syllables if len(s) > 2]
        assert len(complex_sylls) > 0, "Germanic should have some complex syllables"

        # Test Romance - should be more open
        romance_lang = forge.generate("romance")
        avg_length = sum(len(s) for s in romance_lang.syllables) / len(
            romance_lang.syllables
        )
        assert avg_length < 3.5, "Romance should have relatively simple syllables"

        # Test Japanese - should be very simple
        japanese_lang = forge.generate("japanese")
        for syll in japanese_lang.syllables:
            assert len(syll) <= 3, "Japanese syllables should be simple"
            # Should end in vowel or 'n' only
            assert (
                syll[-1] in "aeioun"
            ), f"Japanese syllable '{syll}' should end in vowel or 'n'"

    def test_truly_random_pattern(self):
        """Test that random patterns are actually different each time"""
        forge = Forge()

        # Generate multiple random languages
        random_lang1 = forge.generate("random")
        random_lang2 = forge.generate("random")

        # Phoneme inventories should be different (high probability)
        inventory1 = set(
            random_lang1.phonology["consonants"] + random_lang1.phonology["vowels"]
        )
        inventory2 = set(
            random_lang2.phonology["consonants"] + random_lang2.phonology["vowels"]
        )

        # Should have different phonemes (very high probability with large phoneme pool)
        assert (
            inventory1 != inventory2
        ), "Random patterns should have different phoneme inventories"

        # Should have different syllable structures (high probability)
        structures1 = set(random_lang1.phonology["pattern"]["structure"])
        structures2 = set(random_lang2.phonology["pattern"]["structure"])

        # At least one should be different
        assert (
            structures1 != structures2
        ), "Random patterns should have different syllable structures"

    def test_pattern_linguistic_characteristics(self):
        """Test that each pattern has expected linguistic characteristics"""
        forge = Forge()

        # Polynesian: Very open, simple
        poly = forge.generate("polynesian")
        avg_poly_length = sum(len(s) for s in poly.syllables) / len(poly.syllables)
        assert avg_poly_length <= 2.5, "Polynesian should have very short syllables"

        # Germanic: More complex, allows clusters
        germanic = forge.generate("germanic")
        max_germanic_length = max(len(s) for s in germanic.syllables)
        assert max_germanic_length >= 3, "Germanic should have some long syllables"

        # Japanese: Only 'n' finals allowed
        japanese = forge.generate("japanese")
        for syll in japanese.syllables:
            if len(syll) > 1 and syll[-1] not in "aeiou":
                assert (
                    syll[-1] == "n"
                ), f"Japanese syllable '{syll}' can only end in 'n' as consonant"


# Keep the original simple tests for backward compatibility, but updated for Forge
def test_make_sylls():
    """Original test - updated to use Forge instead of Phones"""
    forge = Forge()

    # Generate custom pattern similar to old regex
    custom_pattern = {
        "structure": ["V", "CV", "VC", "CVC"],
        "consonants": ["p", "t", "k", "b", "d", "g", "θ", "ð"],
        "vowels": ["a", "e", "i", "o", "u", "ʌ", "æ"],
        "weights": [0.2, 0.3, 0.2, 0.3],
    }
    generator = SyllableGenerator(custom_pattern)

    test_inventory_1 = generator.generate_syllables(10)
    assert len(test_inventory_1) == 10

    for syll in test_inventory_1:
        # Check that syllables contain only expected phonemes
        assert all(char in "ptkbdgθðaeiouʌæ" for char in syll)


def test_syllable_patterns():
    """Original test - updated to use Forge instead of Phones"""
    forge = Forge()

    # Test with Polynesian pattern
    poly_lang = forge.generate("polynesian")
    test_inventory_2 = poly_lang.syllables

    for syll in test_inventory_2:
        # Should contain only Polynesian phonemes
        poly_consonants = set(SyllablePatterns.polynesian["consonants"])
        poly_vowels = set(SyllablePatterns.polynesian["vowels"])
        assert all(char in poly_consonants.union(poly_vowels) for char in syll)


# =============================================================================
# ASPIRATIONAL TESTS - Next Phase Development Goals
# These tests define the API we want to build. They will fail initially.
# =============================================================================


def test_forge_api_basic_functionality():
    """Test that the main Forge class can be instantiated and generate basic content"""
    from langforge import Forge

    # Should be able to create Forge instance
    forge = Forge()

    # Should be able to generate a language with basic method
    language = forge.generate("random")

    # Language should have basic properties
    assert hasattr(language, "phonology")
    assert hasattr(language, "syllables")
    assert hasattr(language, "vocabulary")

    # Should be able to access basic syllable generation
    assert len(language.syllables) > 0
    assert all(isinstance(syll, str) for syll in language.syllables)


@pytest.mark.xfail(reason="Swadesh list generation not yet implemented")
def test_forge_swadesh_list_generation():
    """Test that Forge can generate a basic Swadesh list with concept mapping"""
    from langforge import Forge

    # Should be able to generate Swadesh list directly
    swadesh = Forge.swadesh("random")

    # Should contain basic Swadesh concepts
    core_concepts = ["I", "you", "water", "fire", "sun", "moon", "tree", "stone"]

    # Should have concept-to-word mapping
    assert hasattr(swadesh, "concepts")
    assert len(swadesh.concepts) > 0

    # Should contain some core concepts
    swadesh_concept_keys = list(swadesh.concepts.keys())
    assert any(concept in swadesh_concept_keys for concept in core_concepts)

    # Words should be linguistically valid (contain IPA characters)
    sample_words = list(swadesh.concepts.values())[:5]
    for word in sample_words:
        assert len(word) > 0
        assert isinstance(word, str)


@pytest.mark.xfail(reason="Fluent interface chaining not yet implemented")
def test_forge_fluent_interface_chaining():
    """Test that the fluent interface allows method chaining"""
    from langforge import Forge
    import tempfile
    import os

    # Should be able to chain methods fluently
    with tempfile.TemporaryDirectory() as tmp_dir:
        csv_path = os.path.join(tmp_dir, "test_swadesh.csv")
        json_path = os.path.join(tmp_dir, "test_swadesh.json")

        # Test CSV export chaining
        result = Forge.swadesh("random").to_csv(csv_path)

        # Should return something that allows further chaining
        assert result is not None
        assert os.path.exists(csv_path)

        # Test JSON export chaining
        result = Forge.swadesh("random").to_json(json_path)

        # Should return something that allows further chaining
        assert result is not None
        assert os.path.exists(json_path)

        # Should be able to access data after chaining
        swadesh = Forge.swadesh("random")
        swadesh.to_csv(csv_path)

        # Original object should still have data
        assert hasattr(swadesh, "concepts")
        assert len(swadesh.concepts) > 0


# =============================================================================
# SHORT-TERM ASPIRATIONAL TESTS - Immediate Development Steps
# These represent smaller, more achievable building blocks
# =============================================================================


def test_langforge_package_import():
    """Test that the langforge package can be imported"""
    import langforge

    # Should be able to import the package
    assert langforge is not None

    # Should have basic attributes available
    assert hasattr(langforge, "__version__")
    assert hasattr(langforge, "Forge")


@pytest.mark.xfail(reason="SwadeshList class not yet implemented")
def test_swadesh_list_data_structure():
    """Test that SwadeshList can be created and accessed"""
    from langforge import SwadeshList

    # Should be able to create empty SwadeshList
    swadesh = SwadeshList()

    # Should be able to add concept mappings
    swadesh.add_concept("water", "mizu")
    swadesh.add_concept("fire", "hi")

    # Should be able to access concepts
    assert "water" in swadesh.concepts
    assert swadesh.concepts["water"] == "mizu"
    assert len(swadesh.concepts) == 2


@pytest.mark.xfail(reason="Template system not yet implemented")
def test_language_family_template_access():
    """Test that language family templates can be accessed through new API"""
    from langforge import Templates

    # Should be able to get available templates
    templates = Templates.available()
    assert "random" in templates
    assert "polynesian" in templates
    assert "sino-tibetan" in templates

    # Should be able to get template details
    poly_template = Templates.get("polynesian")
    assert hasattr(poly_template, "syllable_pattern")
    assert hasattr(poly_template, "name")


@pytest.mark.xfail(reason="Export functionality not yet implemented")
def test_basic_csv_export():
    """Test that basic CSV export works without full Forge API"""
    from langforge.io import export_csv
    import tempfile
    import os

    # Should be able to export simple data to CSV
    test_data = {"I": "mi", "you": "tu", "water": "awa"}

    with tempfile.TemporaryDirectory() as tmp_dir:
        csv_path = os.path.join(tmp_dir, "test.csv")

        export_csv(test_data, csv_path)

        # File should exist and have content
        assert os.path.exists(csv_path)

        # Should be able to read it back
        with open(csv_path, "r") as f:
            content = f.read()
            assert "I,mi" in content or "mi,I" in content


@pytest.mark.xfail(reason="Phones integration not yet implemented")
def test_phones_integration_wrapper():
    """Test that existing Phones functionality can be wrapped in new API"""
    from langforge import PhonologySystem

    # Should be able to create phonology system using existing data
    phonology = PhonologySystem.from_csv_files(
        "voiced_consonants.csv", "voiceless_consonants.csv", "vowels.csv"
    )

    # Should be able to generate syllables
    syllables = phonology.generate_syllables("polynesian", count=10)

    # Should get valid results
    assert len(syllables) == 10
    assert all(isinstance(syll, str) for syll in syllables)

    # Should be able to access phoneme categories
    assert len(phonology.consonants) > 0
    assert len(phonology.vowels) > 0


# Demo output for manual inspection
if __name__ == "__main__":
    print("=== LangForge Test Demo ===")

    # Demo with Polynesian pattern
    forge = Forge()
    demo_poly = forge.generate("polynesian")

    print("\nPolynesian-style syllables:")
    print(demo_poly.syllables)

    # Demo with Sinitic pattern
    demo_sinitic = forge.generate("sinitic")

    print("\nSinitic-style syllables:")
    print(demo_sinitic.syllables)

    # Demo with Random pattern
    demo_random = forge.generate("random")

    print("\nRandom-style syllables:")
    print(demo_random.syllables[:10])  # First 10

    print("\n=== All Tests Ready! ===")
