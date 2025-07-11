# LangForge: Algorithmic Constructed Language Generator

A systematic, test-driven approach to generating complete constructed languages from phonemic inventory through Swadesh lists to example sentences.

## Vision

LangForge aims to create linguistically coherent constructed languages that can produce:
- **Phonemic inventories** with realistic sound systems
- **Syllable structures** with proper phonotactic constraints  
- **Core vocabulary** mapped to 207 Swadesh concepts
- **Example sentences** demonstrating grammar and syntax

Inspired by [VulgarLang](https://www.vulgarlang.com/how-it-works/), but built with a library-first, test-driven architecture.

## Current Status: Unified Forge API with Improved Syllable Generation

### ✅ **Major Achievement: phones.py → forge.py Migration Complete!**
- **Unified System**: All tests now use the improved Forge API (12 passing tests)
- **Fixed Syllable Patterns**: Replaced broken regex with linguistically accurate generation
- **Smart Algorithm**: Direct syllable construction instead of inefficient Cartesian product filtering
- **Quality Improvement**: Realistic Polynesian (ka, ma, tu), Sinitic (kan, tuk, ŋoŋ), and Random patterns
- **Test-Driven Migration**: All foundation tests successfully migrated to new system

### 🚀 **Improved Syllable Generation Showcase**
**Polynesian Output:** `['ma', 'ju', 'wa', 'pi', 'je', 'u', 'fi', 'e', 'wu', 'nu']`
- ✅ Simple (C)V patterns - linguistically accurate!
- ✅ No more diphthong artifacts from broken regex

**Sinitic Output:** `['ŋa', 'mep', 'ɻa', 'ku', 'oŋ', 'tən', 'gaŋ', 'at', 'en', 'ek']`
- ✅ Realistic CVC patterns with proper final consonants
- ✅ Chinese-style phonemes (ŋ, ɻ, ə)

### 🔄 **Development Roadmap (6 Remaining Aspirational Tests)**
**Phase 1 Progress**: 2/5 short-term tests complete!
- ✅ Package structure and imports  
- ✅ **Forge API basic functionality**
- ❌ SwadeshList data structure
- ❌ Template system integration
- ❌ CSV/JSON export functionality  
- ❌ Phonology system wrapper

**Phase 2 Goals:**
- `Forge.swadesh("random")` - Generate Swadesh lists
- `Forge.generate("polynesian")` - Full language generation
- Method chaining with `.to_csv()` and `.to_json()`

## Quick Start

### Current Working Functionality

Generate linguistically accurate syllables using the improved Forge API:

```python
import langforge

# Create language generator
forge = langforge.Forge()

# Generate different language families with improved patterns
poly_lang = forge.generate("polynesian")
print(poly_lang.syllables)
# Output: ['ma', 'ju', 'wa', 'pi', 'je', 'u', 'fi', 'e', 'wu', 'nu']
# ✅ Simple (C)V patterns - no more diphthong artifacts!

sinitic_lang = forge.generate("sinitic") 
print(sinitic_lang.syllables)
# Output: ['ŋa', 'mep', 'ɻa', 'ku', 'oŋ', 'tən', 'gaŋ', 'at', 'en', 'ek']
# ✅ Realistic CVC with proper final consonants

# Access phonological information
print(poly_lang.phonology['consonants'])  # Polynesian consonant inventory
print(poly_lang.phonology['vowels'])      # Polynesian vowel inventory
print(poly_lang.template)                 # "polynesian"
```

### Future API (Guided by Tests)

The aspirational API being built through test-driven development:

```python
import langforge

# Quick Swadesh list generation
swadesh = langforge.Forge.swadesh("random")
swadesh = langforge.Forge.swadesh("polynesian")

# Fluent interface with export
(langforge.Forge.swadesh("random")
    .to_csv("my_language.csv")
    .to_json("my_language.json"))

# Full language generation
language = langforge.Forge.generate("austronesian")
print(language.phonology.inventory)
print(language.swadesh_list)
print(language.example_sentences)
```

## Development & Testing

### Run Tests
```bash
# Run all tests (12 passing + 6 aspirational)
python -m pytest tests.py -v

# Run foundation tests (migrated to Forge API)
python -m pytest tests.py::TestForge -v

# Run only passing tests
python -m pytest tests.py -v -k "not xfail"
```

### Test-Driven Development Success Story
Our migration showcases **aspirational test-driven development** in action:

- **12 Passing Tests**: All foundation tests migrated to improved Forge API
- **6 Aspirational Tests**: Define remaining development roadmap
- **Test Categories**: Linguistic realism, API design, syllable quality validation
- **Migration Achievement**: Successfully moved from legacy phones.py to forge.py

### Contributing

LangForge uses test-driven development. To contribute:

1. **Run existing tests**: Ensure foundation is solid
2. **Read aspirational tests**: Understand the API vision
3. **Implement features**: Make failing tests pass
4. **Add linguistic tests**: Validate realism of generated languages

## Project Structure

```
langGen/langforge/
├── __init__.py            # Package exports (Forge class)
├── forge.py               # ✅ NEW: Improved syllable generation API
├── phones.py              # Legacy phoneme management (deprecated)
├── tests.py               # 18 comprehensive tests (12 passing, 6 aspirational)
├── voiced_consonants.csv  # IPA consonant data
├── voiceless_consonants.csv
├── vowels.csv
└── debugging.ipynb        # Development notebook
```

## Goals

**✅ Phase 1 Progress**: 2/5 short-term aspirational tests complete!
- ✅ Package structure ✅ Forge API basic functionality
- ❌ SwadeshList ❌ Template system ❌ CSV export

**Phase 2**: Complete fluent interface with Swadesh generation  
**Phase 3**: Expand to full morphology, syntax, and sentence generation

Built with ❤️ for the constructed language community.