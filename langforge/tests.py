import pytest
import re
from forge import Forge, SyllablePatterns, SyllableGenerator, SwadeshList


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

    

    def test_morpheme_type_characteristics(self):
        """Test that different morpheme types have appropriate characteristics"""
        forge = Forge()

        # Test different types
        roots = forge.morphemes("germanic", type="roots", count=20)
        affixes = forge.morphemes("germanic", type="affixes", count=20)

        # Roots should generally be longer than affixes on average
        avg_root_length = sum(len(root) for root in roots) / len(roots)
        avg_affix_length = sum(len(affix) for affix in affixes) / len(affixes)

        # Affixes are typically shorter (often single syllables)
        assert avg_affix_length <= avg_root_length + 0.5, "Affixes should be relatively short"

    def test_morpheme_language_consistency(self):
        """Test that morphemes are consistent within a language family"""
        forge = Forge()

        # Generate multiple sets from same language - should use same phonology
        poly_roots1 = forge.morphemes("polynesian", type="roots", count=10)
        poly_roots2 = forge.morphemes("polynesian", type="roots", count=10)

        # Should use the same phoneme inventory
        all_chars1 = set(''.join(poly_roots1))
        all_chars2 = set(''.join(poly_roots2))

        # Should have significant overlap (since using same language pattern)
        overlap = len(all_chars1 & all_chars2)
        assert overlap > 0, "Same language should produce phonetically consistent morphemes"

    # ========== PHASE 3 TESTS: WORD BUILDING ==========

    def test_word_building_basic_functionality(self):
        """Test basic word building from morphemes"""
        forge = Forge()

        # Should be able to build words
        words = forge.build_words("polynesian", count=15)

        # Check return value
        assert len(words) == 15
        assert all(isinstance(word, str) for word in words)
        assert all(len(word) > 0 for word in words)

    def test_word_building_realistic_lengths(self):
        """Test that built words have realistic lengths for language families"""
        forge = Forge()

        # Polynesian words should be relatively simple
        poly_words = forge.build_words("polynesian", count=20)
        avg_poly_length = sum(len(word) for word in poly_words) / len(poly_words)
        assert 2 <= avg_poly_length <= 6, f"Polynesian words should be 2-6 chars, got {avg_poly_length}"

        # Germanic words can be longer and more complex
        germanic_words = forge.build_words("germanic", count=20)
        max_germanic_length = max(len(word) for word in germanic_words)
        assert max_germanic_length >= 4, "Germanic should have some longer words"

    def test_word_building_morpheme_combination(self):
        """Test that words are built by combining morphemes appropriately"""
        forge = Forge()

        # Generate some words
        words = forge.build_words("japanese", count=10)

        # Words should be combinations of valid syllables/morphemes
        for word in words:
            # Should contain only valid phonemes for the language
            # (This is a basic check - more detailed phonotactic checking could be added)
            assert len(word) > 0
            assert isinstance(word, str)

    def test_word_building_variety(self):
        """Test that word building produces variety, not repetition"""
        forge = Forge()

        words = forge.build_words("romance", count=20)

        # Should have reasonable variety
        unique_words = set(words)
        assert len(unique_words) >= 15, "Should generate mostly unique words"

    def test_word_building_different_strategies(self):
        """Test different word building strategies"""
        forge = Forge()

        # Simple strategy - single morphemes as words
        simple_words = forge.build_words("polynesian", count=10, strategy="simple")
        assert all(len(word) <= 5 for word in simple_words), "Simple strategy should produce short words"

        # Complex strategy - multiple morpheme combinations
        complex_words = forge.build_words("germanic", count=10, strategy="complex")
        avg_complex_length = sum(len(word) for word in complex_words) / len(complex_words)
        assert avg_complex_length >= 4, "Complex strategy should produce longer words"

    # ========== PHASE 3 TESTS: SWADESH GENERATION ==========

    def test_swadesh_generation_basic_functionality(self):
        """Test basic Swadesh list generation"""
        forge = Forge()

        # Should be able to generate Swadesh list
        swadesh = forge.generate_swadesh("polynesian")

        # Check return value
        assert isinstance(swadesh, SwadeshList)
        assert len(swadesh) > 0, "Should generate some concept mappings"

    def test_swadesh_generation_coverage(self):
        """Test that Swadesh generation covers core concepts"""
        forge = Forge()

        # Generate full Swadesh list
        swadesh = forge.generate_swadesh("romance", count=50)

        # Should cover essential concepts
        essential_concepts = ["I", "you", "water", "fire", "big", "small"]
        for concept in essential_concepts:
            if concept in SwadeshList.CORE_CONCEPTS[:50]:  # If in first 50
                assert concept in swadesh, f"Should include essential concept: {concept}"

    def test_swadesh_generation_word_quality(self):
        """Test that generated Swadesh words are realistic"""
        forge = Forge()

        swadesh = forge.generate_swadesh("japanese", count=20)

        # Check word quality
        for concept, word in swadesh.to_dict().items():
            assert isinstance(word, str), f"Word for {concept} should be string"
            assert len(word) > 0, f"Word for {concept} should not be empty"
            assert len(word) <= 10, f"Word for {concept} should be reasonable length"

    def test_swadesh_generation_language_consistency(self):
        """Test that Swadesh words are consistent with language phonology"""
        forge = Forge()

        # Generate language and Swadesh list
        language = forge.generate("polynesian")
        swadesh = forge.generate_swadesh("polynesian", count=30)

        # Words should use the same phoneme inventory
        lang_phonemes = set(language.phonology["consonants"] + language.phonology["vowels"])
        
        for concept, word in swadesh.to_dict().items():
            word_phonemes = set(word)
            # All phonemes in word should be from language inventory
            invalid_phonemes = word_phonemes - lang_phonemes
            assert len(invalid_phonemes) == 0, f"Word '{word}' for '{concept}' uses invalid phonemes: {invalid_phonemes}"

    def test_swadesh_generation_semantic_appropriateness(self):
        """Test that Swadesh generation produces semantically appropriate words"""
        forge = Forge()

        swadesh = forge.generate_swadesh("sinitic", count=30)

        # Different concepts should generally have different words
        words = list(swadesh.to_dict().values())
        unique_words = set(words)
        
        # Should have good variety (allowing some duplication for closed-class items)
        variety_ratio = len(unique_words) / len(words)
        assert variety_ratio >= 0.7, f"Should have good word variety, got {variety_ratio}"

    def test_swadesh_generation_count_parameter(self):
        """Test that count parameter works correctly"""
        forge = Forge()

        # Test different counts
        small_swadesh = forge.generate_swadesh("germanic", count=10)
        large_swadesh = forge.generate_swadesh("germanic", count=50)

        assert len(small_swadesh) == 10, "Should generate exactly the requested count"
        assert len(large_swadesh) == 50, "Should generate exactly the requested count"

    def test_swadesh_generation_prioritizes_core_concepts(self):
        """Test that generation prioritizes the most essential concepts"""
        forge = Forge()

        # Generate small list
        swadesh = forge.generate_swadesh("romance", count=20)

        # Should include very basic concepts
        very_basic = ["I", "you", "water", "fire"]
        included_basic = [concept for concept in very_basic if concept in swadesh]
        
        # Should include most basic concepts in small lists
        assert len(included_basic) >= 2, "Should prioritize very basic concepts in small lists"

    # ========== PHASE 3 TESTS: EXPORT FUNCTIONALITY ==========

    def test_export_csv_basic_functionality(self):
        """Test basic CSV export functionality"""
        forge = Forge()
        import tempfile
        import os

        # Generate language and Swadesh list
        swadesh = forge.generate_swadesh("polynesian", count=20)

        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = os.path.join(tmp_dir, "test_export.csv")
            
            # Should be able to export
            forge.export(swadesh, csv_path, format="csv")

            # File should exist
            assert os.path.exists(csv_path), "CSV file should be created"
            
            # File should have content
            with open(csv_path, 'r') as f:
                content = f.read()
                assert len(content) > 0, "CSV file should have content"
                assert "," in content, "CSV should use comma separator"

    def test_export_json_basic_functionality(self):
        """Test basic JSON export functionality"""
        forge = Forge()
        import tempfile
        import os
        import json

        # Generate language and Swadesh list
        swadesh = forge.generate_swadesh("romance", count=15)

        with tempfile.TemporaryDirectory() as tmp_dir:
            json_path = os.path.join(tmp_dir, "test_export.json")
            
            # Should be able to export
            forge.export(swadesh, json_path, format="json")

            # File should exist
            assert os.path.exists(json_path), "JSON file should be created"
            
            # File should be valid JSON
            with open(json_path, 'r') as f:
                data = json.load(f)
                assert isinstance(data, dict), "JSON should contain dictionary"
                assert len(data) > 0, "JSON should have content"

    def test_export_complete_language_data(self):
        """Test exporting complete language data"""
        forge = Forge()
        import tempfile
        import os
        import json

        # Generate complete language
        language = forge.generate("germanic")
        swadesh = forge.generate_swadesh("germanic", count=30)

        with tempfile.TemporaryDirectory() as tmp_dir:
            json_path = os.path.join(tmp_dir, "complete_language.json")
            
            # Export with language metadata
            forge.export(swadesh, json_path, format="json", include_metadata=True, language=language)

            # Should include both Swadesh and language data
            with open(json_path, 'r') as f:
                data = json.load(f)
                
                assert "swadesh" in data, "Should include Swadesh data"
                assert "language_info" in data, "Should include language metadata"
                assert "phonology" in data["language_info"], "Should include phonology info"

    def test_export_format_validation(self):
        """Test that export validates format parameter"""
        forge = Forge()
        swadesh = forge.generate_swadesh("japanese", count=10)

        with pytest.raises(ValueError):
            forge.export(swadesh, "test.xyz", format="invalid_format")

    def test_export_file_extensions(self):
        """Test that export handles file extensions correctly"""
        forge = Forge()
        import tempfile
        import os

        swadesh = forge.generate_swadesh("sinitic", count=10)

        with tempfile.TemporaryDirectory() as tmp_dir:
            # Should auto-detect format from extension
            csv_path = os.path.join(tmp_dir, "auto.csv")
            json_path = os.path.join(tmp_dir, "auto.json")
            
            forge.export(swadesh, csv_path)  # No format specified
            forge.export(swadesh, json_path)  # No format specified

            assert os.path.exists(csv_path), "Should create CSV file"
            assert os.path.exists(json_path), "Should create JSON file"

    def test_morpheme_generation_basic_functionality(self):
        """Test basic morpheme generation functionality"""
        forge = Forge()

        # Should be able to generate morphemes
        roots = forge.morphemes("polynesian", type="roots", count=10)
        affixes = forge.morphemes("polynesian", type="affixes", count=5)

        # Check return values
        assert len(roots) == 10
        assert len(affixes) == 5
        assert all(isinstance(morpheme, str) for morpheme in roots)
        assert all(isinstance(morpheme, str) for morpheme in affixes)

    def test_morpheme_language_specific_patterns(self):
        """Test that morphemes follow language-specific patterns"""
        forge = Forge()

        # Japanese morphemes should tend toward 2-3 syllables
        japanese_roots = forge.morphemes("japanese", type="roots", count=20)
        japanese_lengths = [len(root) for root in japanese_roots]
        avg_japanese_length = sum(japanese_lengths) / len(japanese_lengths)
        assert (
            avg_japanese_length > 2.5
        ), "Japanese morphemes should be longer on average"

        # Polynesian morphemes should be simpler
        poly_roots = forge.morphemes("polynesian", type="roots", count=20)
        poly_lengths = [len(root) for root in poly_roots]
        avg_poly_length = sum(poly_lengths) / len(poly_lengths)
        assert (
            avg_poly_length < avg_japanese_length
        ), "Polynesian should be simpler than Japanese"

    def test_morpheme_types_distinction(self):
        """Test that roots and affixes have different characteristics"""
        forge = Forge()

        roots = forge.morphemes("germanic", type="roots", count=15)
        affixes = forge.morphemes("germanic", type="affixes", count=15)

        # Roots should generally be longer than affixes
        avg_root_length = sum(len(root) for root in roots) / len(roots)
        avg_affix_length = sum(len(affix) for affix in affixes) / len(affixes)

        assert (
            avg_root_length >= avg_affix_length
        ), "Roots should be at least as long as affixes"

        # Most affixes should be short (1-2 syllables worth)
        short_affixes = [affix for affix in affixes if len(affix) <= 3]
        assert len(short_affixes) > len(affixes) * 0.7, "Most affixes should be short"

    def test_morpheme_linguistic_realism(self):
        """Test that morphemes are linguistically realistic"""
        forge = Forge()

        # Generate morphemes for different languages
        for template in ["polynesian", "japanese", "germanic", "romance"]:
            morphemes = forge.morphemes(template, type="roots", count=10)

            # Should have variety (not all identical)
            assert len(set(morphemes)) > 1, f"{template} morphemes should have variety"

            # Should use appropriate phonemes for language family
            language = forge.generate(template)
            valid_phonemes = set(
                language.phonology["consonants"] + language.phonology["vowels"]
            )

            for morpheme in morphemes:
                assert all(
                    char in valid_phonemes for char in morpheme
                ), f"{template} morpheme '{morpheme}' uses invalid phonemes"

    def test_morpheme_builds_on_syllables(self):
        """Test that morphemes properly use existing syllable generation"""
        forge = Forge()

        # Generate morphemes for a non-random language (consistent phoneme inventory)
        morphemes = forge.morphemes("polynesian", type="roots", count=5)

        # Get expected Polynesian phonemes
        expected_consonants = set(
            ["p", "t", "k", "f", "s", "h", "m", "n", "ŋ", "l", "w", "j"]
        )
        expected_vowels = set(["a", "e", "i", "o", "u"])
        expected_phonemes = expected_consonants.union(expected_vowels)

        # Morphemes should only use Polynesian phonemes
        morpheme_phonemes = set("".join(morphemes))
        assert morpheme_phonemes.issubset(
            expected_phonemes
        ), f"Morphemes should only use Polynesian phonemes, but found: {morpheme_phonemes - expected_phonemes}"


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
    forge = Forge()
    swadesh = forge.generate_swadesh("japanese")

    # Should contain basic Swadesh concepts (207 total)
    core_concepts = [
        "I",
        "you",
        "water",
        "fire",
        "sun",
        "moon",
        "tree",
        "stone",
        "eat",
        "big",
        "red",
    ]

    # Should be a dictionary mapping concepts to words
    assert isinstance(swadesh, dict)
    assert len(swadesh) == 207

    # Should contain expected core concepts
    for concept in core_concepts:
        assert concept in swadesh
        assert len(swadesh[concept]) > 0
        assert isinstance(swadesh[concept], str)

    # Words should be linguistically valid morphemes
    sample_words = [swadesh[concept] for concept in core_concepts]
    for word in sample_words:
        assert len(word) > 0
        # Should be built from Japanese phonemes
        japanese_phonemes = set("kasitemonaruhbpjgzdnweflouy")
        assert all(char in japanese_phonemes for char in word)


@pytest.mark.xfail(reason="Morpheme-based Swadesh generation not yet implemented")
def test_forge_swadesh_uses_morphemes():
    """Test that Swadesh generation uses morpheme generation under the hood"""
    from langforge import Forge

    forge = Forge()

    # Should be able to generate Swadesh using morphemes
    swadesh = forge.generate_swadesh("polynesian")

    # Should use same morpheme generation patterns
    roots = forge.morphemes("polynesian", type="roots", count=20)

    # Swadesh words should have similar characteristics to roots
    swadesh_words = list(swadesh.values())[:20]

    # Average lengths should be similar (both using same language patterns)
    avg_swadesh_len = sum(len(word) for word in swadesh_words) / len(swadesh_words)
    avg_root_len = sum(len(root) for root in roots) / len(roots)

    # Should be within reasonable range
    assert (
        abs(avg_swadesh_len - avg_root_len) < 1.0
    ), "Swadesh words should have similar lengths to generated roots"


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
        forge = Forge()
        swadesh = forge.generate_swadesh("random")
        forge.export(swadesh, csv_path, format="csv")

        # Should return something that allows further chaining
        assert result is not None
        assert os.path.exists(csv_path)

        # Test JSON export chaining
        swadesh = forge.generate_swadesh("random")
        forge.export(swadesh, json_path, format="json")

        # Should return something that allows further chaining
        assert result is not None
        assert os.path.exists(json_path)

        # Should be able to access data after chaining
        swadesh = forge.generate_swadesh("random")
        forge.export(swadesh, csv_path, format="csv")

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


# =============================================================================
# COMPREHENSIVE SWADESHLIST TESTS - Category-Based Implementation
# These tests ensure the dictionary-based SwadeshList is bulletproof
# =============================================================================


def test_swadesh_concept_categories_structure():
    """Test that CONCEPT_CATEGORIES is properly structured"""
    from langforge import SwadeshList
    
    # Should have the categories dictionary
    assert hasattr(SwadeshList, 'CONCEPT_CATEGORIES')
    assert isinstance(SwadeshList.CONCEPT_CATEGORIES, dict)
    
    # Should have expected category keys
    expected_categories = [
        "pronouns_basic", "numbers", "body_parts", "nature_environment",
        "animals_life", "actions_verbs", "descriptors_properties", "materials_objects"
    ]
    for category in expected_categories:
        assert category in SwadeshList.CONCEPT_CATEGORIES
        assert isinstance(SwadeshList.CONCEPT_CATEGORIES[category], list)
        assert len(SwadeshList.CONCEPT_CATEGORIES[category]) > 0


def test_swadesh_categories_total_207():
    """Test that all categories sum to exactly 207 concepts"""
    from langforge import SwadeshList
    
    total_concepts = sum(
        len(concepts) for concepts in SwadeshList.CONCEPT_CATEGORIES.values()
    )
    assert total_concepts == 207, f"Expected 207 concepts, got {total_concepts}"


@pytest.mark.xfail(reason="SwadeshList class not yet implemented")
def test_swadesh_categories_no_duplicates():
    """Test that no concept appears in multiple categories"""
    from langforge import SwadeshList
    
    all_concepts = []
    for category, concepts in SwadeshList.CONCEPT_CATEGORIES.items():
        all_concepts.extend(concepts)
    
    # Should have no duplicates across categories
    assert len(all_concepts) == len(set(all_concepts)), "Concepts should not appear in multiple categories"


def test_swadesh_categories_semantic_accuracy():
    """Test that concepts are in semantically appropriate categories"""
    from langforge import SwadeshList
    
    categories = SwadeshList.CONCEPT_CATEGORIES
    
    # Body parts should contain expected body concepts
    assert "head" in categories["body_parts"]
    assert "hand" in categories["body_parts"]
    assert "water" not in categories["body_parts"]  # Wrong category
    
    # Nature should contain natural phenomena
    assert "water" in categories["nature_environment"]
    assert "fire" in categories["nature_environment"]
    assert "hand" not in categories["nature_environment"]  # Wrong category
    
    # Numbers should be numeric concepts
    assert "one" in categories["numbers"]
    assert "two" in categories["numbers"]
    assert "head" not in categories["numbers"]  # Wrong category


def test_swadesh_core_concepts_flattened():
    """Test that CORE_CONCEPTS is properly flattened from categories"""
    from langforge import SwadeshList
    
    # Should have CORE_CONCEPTS attribute
    assert hasattr(SwadeshList, 'CORE_CONCEPTS')
    assert isinstance(SwadeshList.CORE_CONCEPTS, list)
    assert len(SwadeshList.CORE_CONCEPTS) == 207
    
    # Should contain concepts from all categories
    for category, concepts in SwadeshList.CONCEPT_CATEGORIES.items():
        for concept in concepts:
            assert concept in SwadeshList.CORE_CONCEPTS, f"'{concept}' from {category} missing in CORE_CONCEPTS"


def test_swadesh_core_concepts_key_concepts():
    """Test that essential concepts are present in CORE_CONCEPTS"""
    from langforge import SwadeshList
    
    # Essential concepts that should definitely be present
    essential_concepts = ["I", "you", "water", "fire", "sun", "moon", "tree", "stone", "eat", "big"]
    
    for concept in essential_concepts:
        assert concept in SwadeshList.CORE_CONCEPTS, f"Essential concept '{concept}' missing"


def test_swadesh_core_concepts_order_preservation():
    """Test that CORE_CONCEPTS maintains reasonable order"""
    from langforge import SwadeshList
    
    concepts = SwadeshList.CORE_CONCEPTS
    
    # Basic pronouns should come early (from pronouns_basic category)
    i_index = concepts.index("I")
    you_index = concepts.index("you")
    water_index = concepts.index("water")
    
    # Pronouns should generally come before nature concepts
    assert i_index < water_index, "Pronouns should come before nature concepts"
    assert you_index < water_index, "Pronouns should come before nature concepts"


def test_swadesh_list_creation():
    """Test basic SwadeshList instantiation"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    assert swadesh is not None
    assert len(swadesh) == 0
    assert swadesh.concepts == {}


def test_swadesh_list_add_concept():
    """Test adding single concepts"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    
    assert len(swadesh) == 1
    assert "water" in swadesh
    assert swadesh.concepts["water"] == "mizu"
    assert swadesh.get_word("water") == "mizu"


def test_swadesh_list_add_multiple_concepts():
    """Test adding multiple concepts"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    swadesh.add_concept("fire", "hi")
    swadesh.add_concept("sun", "taiyou")
    
    assert len(swadesh) == 3
    assert all(concept in swadesh for concept in ["water", "fire", "sun"])
    assert swadesh.get_word("fire") == "hi"


def test_swadesh_list_category_based_operations():
    """Test operations using the category-based structure"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    
    # Should be able to add concepts from different categories
    swadesh.add_concept("water", "mizu")  # nature_environment
    swadesh.add_concept("I", "watashi")   # pronouns_basic
    swadesh.add_concept("hand", "te")     # body_parts
    
    assert len(swadesh) == 3
    assert swadesh.get_word("water") == "mizu"
    assert swadesh.get_word("I") == "watashi"
    assert swadesh.get_word("hand") == "te"


def test_swadesh_list_all_categories_supported():
    """Test that concepts from all categories can be added"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    
    # Add one concept from each category
    test_concepts = {
        "I": "watashi",           # pronouns_basic
        "one": "ichi",           # numbers  
        "head": "atama",         # body_parts
        "water": "mizu",         # nature_environment
        "dog": "inu",            # animals_life
        "eat": "taberu",         # actions_verbs
        "big": "ookii",          # descriptors_properties
        "leaf": "ha"             # materials_objects
    }
    
    for concept, word in test_concepts.items():
        swadesh.add_concept(concept, word)
    
    assert len(swadesh) == len(test_concepts)
    for concept, word in test_concepts.items():
        assert swadesh.get_word(concept) == word


@pytest.mark.xfail(reason="SwadeshList class not yet implemented")
def test_swadesh_list_full_207_from_categories():
    """Test adding all 207 concepts using category structure"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    
    # Add all concepts from CORE_CONCEPTS
    for i, concept in enumerate(SwadeshList.CORE_CONCEPTS):
        swadesh.add_concept(concept, f"word{i}")
    
    assert len(swadesh) == 207
    
    # Verify concepts from each category are present
    for category, concepts in SwadeshList.CONCEPT_CATEGORIES.items():
        for concept in concepts:
            assert concept in swadesh, f"Concept '{concept}' from {category} not found in instance"


def test_swadesh_list_duplicate_concepts():
    """Test overwriting existing concepts"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    swadesh.add_concept("water", "aqua")  # Overwrite
    
    assert len(swadesh) == 1
    assert swadesh.get_word("water") == "aqua"  # Should be overwritten


def test_swadesh_list_nonexistent_concept():
    """Test accessing concepts that don't exist"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    
    assert swadesh.get_word("fire") is None
    assert "fire" not in swadesh


def test_swadesh_list_to_dict():
    """Test converting to dictionary"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    swadesh.add_concept("fire", "hi")
    
    result = swadesh.to_dict()
    assert isinstance(result, dict)
    assert result == {"water": "mizu", "fire": "hi"}
    
    # Should be a copy, not reference
    result["new"] = "added"
    assert "new" not in swadesh.concepts


def test_swadesh_list_len():
    """Test len() builtin works"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    assert len(swadesh) == 0
    
    swadesh.add_concept("water", "mizu")
    assert len(swadesh) == 1
    
    swadesh.add_concept("fire", "hi")
    assert len(swadesh) == 2


def test_swadesh_list_contains():
    """Test 'in' operator works"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    
    assert "water" in swadesh
    assert "fire" not in swadesh


def test_swadesh_list_iteration():
    """Test that SwadeshList can be iterated over"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    swadesh.add_concept("fire", "hi")
    
    # Should be able to iterate over concepts
    concepts = list(swadesh)
    assert "water" in concepts
    assert "fire" in concepts
    assert len(concepts) == 2


def test_swadesh_list_type_validation():
    """Test proper type validation for inputs"""
    from langforge import SwadeshList
    
    swadesh = SwadeshList()
    
    # Should handle non-string concept names appropriately
    with pytest.raises(TypeError):
        swadesh.add_concept(123, "number")
    
    with pytest.raises(TypeError):
        swadesh.add_concept(["list"], "list_concept")


def test_swadesh_list_backward_compatibility():
    """Test that original CORE_CONCEPTS API still works"""
    from langforge import SwadeshList
    
    # Original API should still work exactly as before
    assert hasattr(SwadeshList, 'CORE_CONCEPTS')
    assert isinstance(SwadeshList.CORE_CONCEPTS, list)
    assert len(SwadeshList.CORE_CONCEPTS) == 207
    
    # All original tests should still pass
    swadesh = SwadeshList()
    swadesh.add_concept("water", "mizu")
    swadesh.add_concept("fire", "hi")
    
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
