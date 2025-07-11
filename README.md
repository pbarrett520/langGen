# LangForge: Algorithmic Constructed Language Generator

A systematic, test-driven approach to generating complete constructed languages from phonemic inventory through Swadesh lists to example sentences.

## Vision

LangForge aims to create linguistically coherent constructed languages that can produce:
- **Phonemic inventories** with realistic sound systems
- **Syllable structures** with proper phonotactic constraints  
- **Core vocabulary** mapped to 207 Swadesh concepts
- **Example sentences** demonstrating grammar and syntax

Inspired by [VulgarLang](https://www.vulgarlang.com/how-it-works/), but built with a library-first, test-driven architecture.

## Current Status: Test-Driven Foundation

### ✅ **Solid Foundation (10 Passing Tests)**
- **Phoneme Management**: CSV-based IPA consonant/vowel organization
- **Syllable Generation**: Regex-based patterns with language family templates
- **Linguistic Realism**: Validated phonotactic constraints and variety
- **Data Quality**: Robust cleaning and validation systems
- **Language Templates**: Polynesian, Sinitic, and North Sinitic patterns

### 🔄 **Development Roadmap (8 Aspirational Tests)**
**Short-term API Building Blocks:**
- Package structure and imports
- SwadeshList data structure
- Template system integration
- CSV/JSON export functionality  
- Phonology system wrapper

**Long-term Fluent Interface:**
- `Forge.swadesh("random")` - Generate Swadesh lists
- `Forge.generate("polynesian")` - Full language generation
- Method chaining with `.to_csv()` and `.to_json()`

## Quick Start

### Current Working Functionality

Generate syllables using language family templates:

```python
from phones import Phones
from syllable_patterns import Syllable_patterns

# Create phonology system
poly_lang = Phones(
    'voiced_consonants.csv', 
    'voiceless_consonants.csv', 
    'vowels.csv',
    syll_struct=Syllable_patterns.polyneisian  # Pre-defined template
)

# Generate Polynesian-style syllables
syllables = poly_lang.make_sylls(10)
# Output: ['ka', 'lu', 'ma', 'na', 'pa', 'ta', 'wa', 'ko', 'mo', 'no']

# Access phoneme categories
print(poly_lang.bilabial)      # ['b', 'm', 'ʙ', 'β', 'p', 'ɸ']
print(poly_lang.all_consonants) # All consonants
print(poly_lang.all_vowels)     # All vowels
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
# Run all tests (10 passing + 8 aspirational)
python -m pytest tests.py -v

# Run only passing tests
python -m pytest tests.py -v -k "not xfail"
```

### Test-Driven Development
Each feature is guided by **aspirational tests** that define the desired API before implementation:

- **10 Passing Tests**: Validate current phonological system
- **8 Aspirational Tests**: Define development roadmap
- **Test Categories**: Unit, integration, linguistic realism, API design

### Contributing

LangForge uses test-driven development. To contribute:

1. **Run existing tests**: Ensure foundation is solid
2. **Read aspirational tests**: Understand the API vision
3. **Implement features**: Make failing tests pass
4. **Add linguistic tests**: Validate realism of generated languages

## Project Structure

```
langGen/langforge/
├── phones.py              # Current phoneme management
├── syllable_patterns.py   # Language family templates
├── tests.py               # 18 comprehensive tests
├── voiced_consonants.csv  # IPA consonant data
├── voiceless_consonants.csv
├── vowels.csv
└── debugging.ipynb        # Development notebook
```

## Goals

**Phase 1**: Make 5 short-term aspirational tests pass (basic API)
**Phase 2**: Make 3 long-term aspirational tests pass (fluent interface)  
**Phase 3**: Expand to full morphology, syntax, and sentence generation

Built with ❤️ for the constructed language community.