# LangForge: Algorithmic Constructed Language Generator

A systematic, test-driven approach to generating complete constructed languages from phonemic inventory through Swadesh lists to example sentences.

## Vision

LangForge aims to create linguistically coherent constructed languages that can produce:
- **Phonemic inventories** with realistic sound systems
- **Syllable structures** with proper phonotactic constraints  
- **Core vocabulary** mapped to 207 Swadesh concepts
- **Example sentences** demonstrating grammar and syntax

Inspired by [VulgarLang](https://www.vulgarlang.com/how-it-works/), but built with a library-first, test-driven architecture.

## Current Status: Expanded Language Family Support & TDD Success

### ✅ **Major Achievement: Multi-Language Family Generator with TDD Methodology!**
- **Expanded Language Support**: 5 realistic language families + truly random generation (14+ passing tests)
- **Test-Driven Development Proven**: New features implemented using TDD - tests first, implementation second
- **Advanced Syllable Patterns**: Germanic complexity, Romance flow, Japanese simplicity, Polynesian openness
- **Truly Random Generation**: Each call creates completely different phoneme inventories from 50+ phoneme pool
- **Production Ready**: Beautiful demo script for showcasing linguistic capabilities

### 🚀 **Multi-Language Family Showcase**
**Polynesian:** `['ma', 'ju', 'wa', 'pi', 'je', 'u', 'fi', 'e', 'wu', 'nu']` - Simple (C)V patterns  
**Germanic:** `['lir', 'θən', 'gɛʃl', 'θpʌg', 'mŋot']` - Complex clusters & diverse vowels  
**Japanese:** `['we', 'ra', 'he', 'ri', 'sa', 'mo', 'e', 'bo']` - Predominantly CV patterns  
**Romance:** `['fɲo', 'gmu', 'ʎe', 'bo', 'ʎo', 'ro', 'li']` - Flowing open syllables  
**Sinitic:** `['ɻu', 'dak', 'pə', 'at', 'iŋ', 'men', 'fo']` - Tonal-ready with limited finals  

**Truly Random:** Each generation creates entirely different phoneme inventories:
- Random #1: `['ɥɯʎ', 'ʀɯχdz', 'ʎøw', 'pø']` (phonemes: χ, ɣ, ʝ, ʀ, ɥ, ʒ...)
- Random #2: `['ʁɨtʍ', 'dʒɵqʍ', 'ɳʌʍ']` (phonemes: dʒ, z, q, ʍ, ç, ʒ, ʕ...)

### 🔄 **Development Roadmap - Next Phase: Morpheme Generation**
**Phase 1 COMPLETE**: ✅ Advanced syllable generation with 5 language families + truly random
- ✅ Package structure and imports  
- ✅ **Forge API with multi-language support**
- ✅ **Test-driven development methodology proven**
- ✅ **Production-ready demo capabilities**

**Phase 2 Current**: Morpheme & vocabulary generation (leverage syllable system)
- 🎯 **Next Goal**: Morpheme generator that builds words from syllables
- ❌ SwadeshList data structure for concept mapping
- ❌ Root morpheme generation using syllable patterns
- ❌ Affix system (prefixes, suffixes, infixes)
- ❌ CSV/JSON export functionality

**Phase 3 Goals:**
- `Forge.swadesh("random")` - Generate complete Swadesh lists
- `Forge.generate("polynesian").vocabulary` - Full vocabulary with morphology
- Method chaining with `.to_csv()` and `.to_json()`

## Quick Start

### Current Working Functionality

Generate linguistically accurate syllables across 5 language families:

```python
import langforge

# Create language generator
forge = langforge.Forge()

# Generate different language families
polynesian = forge.generate("polynesian")    # Simple (C)V patterns
germanic = forge.generate("germanic")        # Complex clusters  
japanese = forge.generate("japanese")        # Predominantly CV
romance = forge.generate("romance")          # Flowing open syllables
sinitic = forge.generate("sinitic")          # Tonal-ready patterns

# Each language has unique characteristics
print(f"Polynesian: {polynesian.syllables[:6]}")
# Output: ['ma', 'ju', 'wa', 'pi', 'je', 'u']

print(f"Germanic: {germanic.syllables[:4]}")  
# Output: ['lir', 'θən', 'gɛʃl', 'θpʌg']

# Truly random generation - different each time!
random1 = forge.generate("random")
random2 = forge.generate("random")
print(f"Random inventories are different: {random1.phonology['consonants'][:5] != random2.phonology['consonants'][:5]}")
# Output: True

# Access detailed phonological information
print(f"Germanic consonants: {germanic.phonology['consonants']}")
print(f"Japanese vowels: {japanese.phonology['vowels']}")
print(f"Syllable patterns: {romance.phonology['pattern']['structure']}")
```

### Demo Script - Perfect for Showcasing!

Run the beautiful demo to showcase LangForge's capabilities:

```bash
# In the langforge directory
python demo.py
```

**Features elegant formatting with:**
- Multi-language family demonstrations
- Phoneme inventory analysis  
- Linguistic complexity comparisons
- Random generation showcases
- Technical feature highlights

Perfect for job interviews, presentations, or showing friends!

### Future API (Guided by Tests)

The next phase will add morpheme and vocabulary generation:

```python
import langforge

# Morpheme generation (Phase 2 goal)
roots = langforge.Forge.morphemes("polynesian", type="roots", count=50)
affixes = langforge.Forge.morphemes("germanic", type="affixes")

# Swadesh list generation with morphology
swadesh = langforge.Forge.swadesh("random")
swadesh = langforge.Forge.swadesh("polynesian")

# Full language with vocabulary
language = langforge.Forge.generate("romance")
print(language.phonology.inventory)
print(language.vocabulary.swadesh_list)  # 207 concepts
print(language.vocabulary.morphology)    # Root + affix system
```

## Development & Testing

### Run Tests
```bash
# Run all tests (14+ passing + 6 aspirational)
python -m pytest tests.py -v

# Run foundation tests (all language families)
python -m pytest tests.py::TestForge -v

# Run only passing tests
python -m pytest tests.py -v -k "not xfail"

# Demo the results
python demo.py
```

### Test-Driven Development Success Story
Our latest development cycle proves **TDD methodology works perfectly**:

- **✅ Tests First**: Defined new language patterns in test cases
- **✅ Implementation Second**: Built features to make tests pass
- **✅ Green Tests**: All 14+ foundation tests passing
- **✅ TDD Proven**: Added Germanic, Romance, Japanese, and truly random generation
- **✅ Production Ready**: Beautiful demo script validates real-world usage
- **Test Categories**: Multi-language family validation, truly random behavior, linguistic characteristics

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
├── forge.py               # ✅ Multi-language family syllable generation
├── demo.py                # ✅ NEW: Beautiful demo for showcasing capabilities  
├── tests.py               # 20+ comprehensive tests (14+ passing, 6 aspirational)
├── phones.py              # Legacy phoneme management (deprecated)
├── voiced_consonants.csv  # IPA consonant data
├── voiceless_consonants.csv
├── vowels.csv
└── debugging.ipynb        # Development notebook
```

## Goals

**✅ Phase 1 COMPLETE**: Advanced syllable generation with multi-language family support!
- ✅ Package structure ✅ Multi-language Forge API ✅ TDD methodology ✅ Production demo

**🎯 Phase 2 CURRENT**: Morpheme generation & vocabulary building
- 🚧 Root morpheme generation using syllable patterns
- 🚧 Affix system (prefixes, suffixes, derivational morphology)  
- 🚧 SwadeshList with 207 concept mappings
- 🚧 CSV/JSON export functionality

**Phase 3**: Complete language generation with syntax and example sentences

Built with ❤️ for the constructed language community.