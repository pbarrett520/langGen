import pytest
from phones import Phones, Syllable_patterns
import re


class TestPhones:
    """Comprehensive test suite for Phones class functionality"""

    def setup_method(self):
        """Set up test fixtures"""
        self.test_object_custom_regex = Phones(
            "voiced_consonants.csv",
            "voiceless_consonants.csv",
            "vowels.csv",
            syll_struct=r"[ptkbdgθð]?[aeiouʌæ]?[aeiouʌæ][ptkbdgθð]?[ptkbdgθð]?",
        )

        self.test_object_syllable_template = Phones(
            "voiced_consonants.csv",
            "voiceless_consonants.csv",
            "vowels.csv",
            syll_struct=Syllable_patterns.polyneisian,
        )

    def test_make_sylls_basic_functionality(self):
        """Test basic syllable generation functionality"""
        test_inventory = self.test_object_custom_regex.make_sylls(10)

        # Check return value
        assert len(test_inventory) == 10
        assert all(isinstance(syll, str) for syll in test_inventory)

        # Check internal state
        assert len(self.test_object_custom_regex.syll_inventory) == 10
        assert self.test_object_custom_regex.syll_inventory == test_inventory

        # Check pattern matching
        for syll in test_inventory:
            assert re.match(self.test_object_custom_regex.syll_struct, syll)

    def test_make_sylls_with_predefined_patterns(self):
        """Test syllable generation with predefined language family patterns"""
        # Test Polynesian pattern
        poly_inventory = self.test_object_syllable_template.make_sylls(10)
        assert len(poly_inventory) == 10

        for syll in poly_inventory:
            assert re.match(Syllable_patterns.polyneisian, syll)

        # Test other patterns
        sinitic_obj = Phones(
            "voiced_consonants.csv",
            "voiceless_consonants.csv",
            "vowels.csv",
            syll_struct=Syllable_patterns.south_sinitic,
        )

        sinitic_inventory = sinitic_obj.make_sylls(5)
        assert len(sinitic_inventory) == 5

        for syll in sinitic_inventory:
            assert re.match(Syllable_patterns.south_sinitic, syll)

    def test_make_sylls_edge_cases(self):
        """Test edge cases for syllable generation"""
        # Test size=1
        single_syll = self.test_object_custom_regex.make_sylls(1)
        assert len(single_syll) == 1

        # Test larger size
        large_inventory = self.test_object_custom_regex.make_sylls(50)
        assert len(large_inventory) == 50

        # Test that syllables are unique (sorted sampling should give unique results)
        assert len(set(large_inventory)) == len(large_inventory)

    def test_phoneme_categorization(self):
        """Test that phonemes are properly categorized"""
        # Test consonant categorization
        assert len(self.test_object_custom_regex.all_consonants) > 0
        assert len(self.test_object_custom_regex.all_vowels) > 0

        # Test specific categories
        assert "p" in self.test_object_custom_regex.bilabial
        assert "b" in self.test_object_custom_regex.bilabial
        assert "t" in self.test_object_custom_regex.alveolar
        assert "d" in self.test_object_custom_regex.alveolar

        # Test manner of articulation
        assert "p" in self.test_object_custom_regex.plosive
        assert "b" in self.test_object_custom_regex.plosive
        assert "m" in self.test_object_custom_regex.nasal
        assert "n" in self.test_object_custom_regex.nasal

    def test_clean_method(self):
        """Test the _clean method functionality"""
        # Test with normal data
        clean_data = self.test_object_custom_regex._clean(["a", "b", "c"])
        assert clean_data == ["a", "b", "c"]

        # Test with NaN values (simulate pandas NaN as string)
        dirty_data = ["a", "NaN", "b", "c"]
        cleaned = self.test_object_custom_regex._clean(dirty_data)
        assert "NaN" not in cleaned
        assert "a" in cleaned
        assert "b" in cleaned
        assert "c" in cleaned

    def test_syllable_patterns_availability(self):
        """Test that all predefined syllable patterns are available"""
        assert hasattr(Syllable_patterns, "polyneisian")
        assert hasattr(Syllable_patterns, "south_sinitic")
        assert hasattr(Syllable_patterns, "north_sinitic")

        # Test that patterns are valid regex
        assert re.compile(Syllable_patterns.polyneisian)
        assert re.compile(Syllable_patterns.south_sinitic)
        assert re.compile(Syllable_patterns.north_sinitic)

    def test_linguistic_realism(self):
        """Test that generated syllables are linguistically realistic"""
        inventory = self.test_object_custom_regex.make_sylls(20)

        # Check average syllable length is reasonable (1-6 characters for IPA)
        avg_length = sum(len(syll) for syll in inventory) / len(inventory)
        assert 1 <= avg_length <= 6  # Allow flexibility for complex IPA

        # Check that syllables contain expected phonemes
        all_text = "".join(inventory)
        assert any(char in all_text for char in "aeiouʌæ")  # Should have vowels
        assert any(char in all_text for char in "ptkbdgθð")  # Should have consonants

        # Check that syllables are not all identical (variety test)
        assert len(set(inventory)) > 1  # Should have variety in actual syllables

    def test_reproducibility(self):
        """Test that syllable generation has some consistency"""
        # This is tricky since we use random sampling
        # But we can test that the same object produces valid results consistently
        inventory1 = self.test_object_custom_regex.make_sylls(10)
        inventory2 = self.test_object_custom_regex.make_sylls(10)

        # Both should be valid
        assert len(inventory1) == 10
        assert len(inventory2) == 10

        # All should match pattern
        for syll in inventory1 + inventory2:
            assert re.match(self.test_object_custom_regex.syll_struct, syll)


# Keep the original simple tests for backward compatibility
def test_make_sylls():
    """Original test - maintained for backward compatibility"""
    test_object_custom_regex = Phones(
        "voiced_consonants.csv",
        "voiceless_consonants.csv",
        "vowels.csv",
        syll_struct=r"[ptkbdgθð]?[aeiouʌæ]?[aeiouʌæ][ptkbdgθð]?[ptkbdgθð]?",
    )

    test_inventory_1 = test_object_custom_regex.make_sylls(10)
    assert len(test_object_custom_regex.syll_inventory) == 10

    for i in test_inventory_1:
        assert re.match(test_object_custom_regex.syll_struct, i)


def test_syllable_patterns():
    """Original test - maintained for backward compatibility"""
    test_object_custom_regex = Phones(
        "voiced_consonants.csv",
        "voiceless_consonants.csv",
        "vowels.csv",
        syll_struct=r"[ptkbdgθð]?[aeiouʌæ]?[aeiouʌæ][ptkbdgθð]?[ptkbdgθð]?",
    )

    test_inventory_2 = test_object_custom_regex.make_sylls(10)

    for i in test_inventory_2:
        assert re.match(test_object_custom_regex.syll_struct, i)


# =============================================================================
# ASPIRATIONAL TESTS - Next Phase Development Goals
# These tests define the API we want to build. They will fail initially.
# =============================================================================


@pytest.mark.xfail(reason="Forge API not yet implemented")
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


@pytest.mark.xfail(reason="Package structure not yet created")
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
    demo_poly = Phones(
        "voiced_consonants.csv",
        "voiceless_consonants.csv",
        "vowels.csv",
        syll_struct=Syllable_patterns.polyneisian,
    )

    print("\nPolynesian-style syllables:")
    print(demo_poly.make_sylls(10))

    # Demo with South Sinitic pattern
    demo_sinitic = Phones(
        "voiced_consonants.csv",
        "voiceless_consonants.csv",
        "vowels.csv",
        syll_struct=Syllable_patterns.south_sinitic,
    )

    print("\nSouth Sinitic-style syllables:")
    print(demo_sinitic.make_sylls(10))

    print("\n=== All Tests Ready! ===")
