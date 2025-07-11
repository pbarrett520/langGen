# LangForge: Algorithmic Constructed Language Generator

## Vision & Goals

### Project Purpose
Create a systematic, algorithmic tool for generating complete constructed languages (conlangs) that can produce linguistically coherent Swadesh lists and example sentences. The goal is to model the natural process of language emergence computationally.

### End Goal
A system that can generate a complete basic language consisting of:
- Phonemic inventory (consonants, vowels, prosodic features)
- Syllable system with realistic phonotactic constraints
- Morphological system (roots, affixes, word formation rules)
- Core vocabulary mapped to 207 Swadesh concepts
- 20 example sentences demonstrating syntax and grammar

### Success Criteria
- Generate linguistically plausible languages that feel "natural"
- Produce consistent phonological, morphological, and syntactic systems
- Create usable Swadesh lists for worldbuilding/linguistic purposes
- Support both random generation and language-family-specific styles

## Current State Assessment

### Major Achievement: Unified Forge API ✅
- **Complete Migration**: Successfully migrated all tests from phones.py to forge.py
- **Improved Syllable Generation**: Fixed broken regex patterns with linguistically accurate generation
- **Smart Algorithm**: Replaced inefficient Cartesian product filtering with direct construction
- **Unified Testing**: 18 total tests (12 passing, 6 aspirational) all using improved API
- **Quality Validation**: Real syllable output demonstrates dramatic improvement

### Foundation Components (Migrated & Enhanced)
- ✅ **Improved phonological patterns**: Polynesian (C)V, Sinitic (C)V(C), Random complexity
- ✅ **Smart syllable generation**: Direct construction instead of filtering
- ✅ **Language family templates**: ImprovedSyllablePatterns with weights and position-aware consonants
- ✅ **Linguistic realism**: Validated through actual syllable output quality
- ✅ **API consistency**: All tests use unified Forge interface

### Development Guided by Tests (Updated)
**12 Passing Tests** validate improved system:
- TestForge class validates all core syllable generation functionality
- Language family pattern testing with real phoneme validation
- Edge case handling and quality assurance
- Linguistic realism verification through output analysis
- Reproducibility and consistency across different templates

**6 Aspirational Tests** define remaining roadmap:
- 3 Long-term API goals (Swadesh generation, fluent interface chaining)
- 3 Short-term stepping stones (SwadeshList, Templates, CSV export)

### Implementation Status
- ✅ **Package structure** (`import langforge`)
- ✅ **Forge API basic functionality** (`forge.generate("polynesian")`)
- ❌ SwadeshList data structure for concept mapping
- ❌ Template system for language family access
- ❌ CSV/JSON export functionality
- ❌ Phones integration wrapper (may be deprecated)
- ❌ Morphological system (roots, affixes, word formation)
- ❌ Syntactic system (grammar rules, sentence generation)

### Quality Improvement Evidence
**Before (phones.py)**: Broken diphthong artifacts from regex filtering
**After (forge.py)**: 
- Polynesian: `['ma', 'ju', 'wa', 'pi', 'je', 'u', 'fi', 'e', 'wu', 'nu']` - Clean (C)V patterns!
- Sinitic: `['ŋa', 'mep', 'ɻa', 'ku', 'oŋ', 'tən', 'gaŋ', 'at', 'en', 'ek']` - Realistic CVC with proper finals!

## Technical Architecture

### Design Principles
- **Object-Oriented**: Use classes and composition over complex inheritance
- **Modular**: Separate concerns into distinct, testable components
- **Extensible**: Build minimal control with hooks for future customization
- **Deterministic**: Same seed should produce same language (when desired)
- **Stable**: Prefer simple, proven approaches over complex abstractions

### Core Module Structure
```
langforge/
├── __init__.py         # Main library API (Forge class)
├── language.py         # GeneratedLanguage class with fluent methods
├── phonology/          # Sound system generation
│   ├── inventory.py    # Phoneme management
│   ├── syllables.py    # Syllable structure and generation
│   └── phonotactics.py # Sound combination rules
├── morphology/         # Word formation system
│   ├── roots.py        # Root generation
│   ├── affixes.py      # Prefix/suffix systems
│   └── processes.py    # Morphophonological rules
├── lexicon/            # Vocabulary and meaning
│   ├── swadesh.py      # Swadesh list management
│   └── assignment.py   # Concept-to-word mapping
├── syntax/             # Grammar and sentence structure
│   ├── grammar.py      # Grammatical rules
│   └── sentences.py    # Sentence generation
├── generation/         # Language generation orchestration
│   ├── templates.py    # Language family templates
│   └── generator.py    # Internal generation engine
├── io/                 # File operations
│   ├── export.py       # Save languages to files
│   └── import.py       # Load saved languages
└── interfaces/         # Interface wrappers (future)
    ├── cli.py          # Command-line interface
    ├── web.py          # Web API
    └── mcp.py          # MCP tool integration
```

### Data Flow
```
Seed → Language Template → Phonology → Morphology → Lexicon → Syntax → Output
```

## Test-Driven Development Strategy

### Testing Philosophy
LangForge uses **aspirational test-driven development** to guide implementation. Tests are written first to define the desired API, then implementation follows to make tests pass.

### Test Suite Structure
```
18 Total Tests
├── 10 Passing Tests (Foundation)
│   ├── Core syllable generation
│   ├── Language family templates
│   ├── Phoneme management
│   ├── Data validation
│   └── Linguistic realism
└── 8 Aspirational Tests (Roadmap)
    ├── 5 Short-term (API building blocks)
    │   ├── Package structure
    │   ├── Data classes
    │   ├── Template system
    │   ├── Export functionality
    │   └── Integration wrappers
    └── 3 Long-term (Full API)
        ├── Forge class
        ├── Swadesh generation
        └── Fluent interface
```

### Test-Driven Benefits
- **Clear Development Path**: Each test defines exactly what needs to be built
- **API Design Validation**: Tests ensure the API works as intended before implementation
- **Regression Prevention**: Existing functionality protected while adding new features
- **Concrete Progress**: Tests turning green provides measurable progress
- **Refactoring Safety**: Comprehensive tests enable confident code improvements

### Development Workflow
1. **Write Aspirational Test**: Define desired behavior in test form
2. **Run Test (Expect Fail)**: Confirm test fails for right reasons
3. **Implement Minimal Code**: Write just enough to make test pass
4. **Run All Tests**: Ensure no regressions in existing functionality
5. **Refactor**: Improve code while keeping tests green
6. **Repeat**: Move to next aspirational test

### Test Categories
- **Unit Tests**: Individual class/function behavior
- **Integration Tests**: Component interaction validation
- **Linguistic Tests**: Ensure output quality and realism
- **API Tests**: Validate public interface design
- **Regression Tests**: Protect against breaking changes

## Linguistic Design Decisions

### Phonological System
- **Inventory Size**: 15-40 consonants, 5-15 vowels (typologically realistic)
- **Syllable Structure**: CV, CVC, CCV, CCVC patterns with language-specific constraints
- **Prosodic Features**: Stress patterns, potential tone systems (future)
- **Phonotactics**: Realistic sound combination rules based on sonority hierarchy

### Morphological Complexity
Three-axis typological system:
- **Inflectional**: Languages with rich case/tense/agreement systems (like Latin)
- **Analytical**: Languages with minimal morphology (like Chinese)
- **Agglutinative**: Languages with extensive affixation (like Turkish)

Each generated language will lean toward one type while incorporating elements of others.

### Syntactic Variety
- **Word Order**: Generate SOV, SVO, VSO, etc. with typological consistency
- **Case Systems**: Nominative-accusative, ergative-absolutive, or minimal case
- **Agreement**: Subject-verb, adjective-noun agreement patterns
- **Complexity**: Start simple, build toward moderate complexity

### Typological Constraints
- Follow linguistic universals (Greenberg's word order correlations)
- Ensure internal consistency within each language
- Model realistic language families when requested

## Development Roadmap

### Test-Driven Development Success

**Current Status**: 12 passing tests validate improved Forge API, 6 aspirational tests guide remaining development

**Major Achievement**: Successfully migrated all foundation tests from phones.py to forge.py with improved syllable generation!

### Phase 1: Basic API Structure (Short-term Tests)
**Goal**: Make 5 short-term aspirational tests pass (**2/5 Complete!**)

1. **✅ Package Structure** → `test_langforge_package_import` 
   - ✅ Created `langforge/__init__.py` with version and exports
   - ✅ Set up basic import structure
   - ✅ Defined `Forge` class interface

2. **Data Structures** → `test_swadesh_list_data_structure`
   - [ ] Implement `SwadeshList` class with concept mapping
   - [ ] Add `add_concept()` and `concepts` property
   - [ ] Create basic concept-to-word storage

3. **Template System** → `test_language_family_template_access`
   - [ ] Create `Templates` class exposing `ImprovedSyllablePatterns`
   - [ ] Add `.available()` and `.get()` methods
   - [ ] Bridge improved patterns to public API

4. **Export System** → `test_basic_csv_export`
   - [ ] Create `langforge.io.export_csv` function
   - [ ] Handle dictionary-to-CSV conversion
   - [ ] Add basic file I/O operations

5. **Phonology Integration** → `test_phones_integration_wrapper`
   - [ ] Create `PhonologySystem` class wrapping Forge syllable generation
   - [ ] Add `.from_csv_files()` class method (may deprecate)
   - [ ] Implement `.generate_syllables()` method

### Phase 2: Core API Implementation (Long-term Tests)
**Goal**: Make 3 long-term aspirational tests pass (**1/3 Complete!**)

6. **✅ Forge Class** → `test_forge_api_basic_functionality`
   - ✅ Implemented main `Forge` class with `.generate()` method
   - ✅ Created `GeneratedLanguage` class with phonology/syllables/vocabulary
   - ✅ Connected to improved syllable generation system

7. **Swadesh Generation** → `test_forge_swadesh_list_generation`
   - [ ] Implement `Forge.swadesh()` class method
   - [ ] Create concept-to-word mapping logic using syllable generation
   - [ ] Load and assign 207 Swadesh concepts

8. **Fluent Interface** → `test_forge_fluent_interface_chaining`
   - [ ] Add `.to_csv()` and `.to_json()` methods to SwadeshList
   - [ ] Implement method chaining that preserves object state
   - [ ] Connect export functionality to SwadeshList

### Phase 3: Enhanced Phonology
**Goal**: Improve and expand phonological system

- [ ] Add phonotactic constraint system
- [ ] Implement language family templates
- [ ] Add prosodic feature generation
- [ ] Create phoneme frequency weighting

### Phase 4: Morphological System
**Goal**: Build word formation beyond syllables

- [ ] Build root generation system
- [ ] Implement affix creation and attachment
- [ ] Add morphophonological processes
- [ ] Create morphological type system (inflectional/analytical/agglutinative)
- [ ] Develop word formation rules

### Phase 5: Syntactic System
**Goal**: Generate sentences and grammar

- [ ] Generate basic grammatical rules
- [ ] Implement sentence template system
- [ ] Add agreement and case marking
- [ ] Create example sentence generation
- [ ] Ensure typological consistency

### Phase 6: Integration & Polish
**Goal**: Complete system integration

- [ ] Create unified language generation pipeline
- [ ] Implement multiple output formats (CSV, JSON, Markdown)
- [ ] Build CLI wrapper around library
- [ ] Add comprehensive documentation
- [ ] Prepare for future interface development (Web, MCP)

### Test-Driven Success Metrics (Updated)
- **Current Achievement**: 12 passing tests (improved from 10) - migration success!
- **Phase 1 Target**: 15 passing tests (12 current + 3 remaining short-term)
- **Phase 2 Complete**: 18 passing tests (all current aspirational tests pass)
- **Each Phase**: All tests pass, no regressions in existing functionality
- **Continuous**: New features guided by additional aspirational tests
- **Migration Success**: phones.py → forge.py with improved syllable generation quality

## Implementation Preferences

### Coding Style
- **Architecture**: Object-oriented with composition
- **Naming**: Clear, descriptive variable and method names
- **Documentation**: Docstrings for all public methods
- **Type Hints**: Use throughout for better IDE support
- **Testing**: Unit tests for all core functionality

### Testing Strategy
- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Linguistic Tests**: Verify linguistic plausibility
- **Regression Tests**: Ensure changes don't break existing functionality

### User Interface Strategy
**Primary: Python Library** - Core functionality as importable modules with fluent API
- **Command Line Interface**: Wrapper around library functions
- **Web Interface**: FastAPI/Flask endpoints calling library
- **MCP Tool**: Integration tool using library functions
- **REST API**: Web service wrapper around library

### API Design Vision
**Clean, Fluent Interface (Validated by Tests):**
```python
# Quick generation (test_forge_swadesh_list_generation)
swadesh_list = Forge.swadesh("random")
swadesh_list = Forge.swadesh("indo-european")

# With export chaining (test_forge_fluent_interface_chaining)
Forge.swadesh("random").to_csv("swadesh")
Forge.swadesh("sino-tibetan").to_json("language_data")

# Full language generation (test_forge_api_basic_functionality)
language = Forge.generate("random")
language = Forge.generate("austronesian", morphology="agglutinative")

# Access specific components (validated by integration tests)
language.phonology.inventory
language.swadesh_list
language.example_sentences
```

**Test-Validated Design Decisions:**
- **Fluent Interface**: `test_forge_fluent_interface_chaining` ensures method chaining works
- **SwadeshList Class**: `test_swadesh_list_data_structure` validates concept mapping
- **Package Structure**: `test_langforge_package_import` confirms clean imports
- **Template System**: `test_language_family_template_access` validates family templates
- **Export System**: `test_basic_csv_export` ensures file output works
- **Phonology Integration**: `test_phones_integration_wrapper` bridges old and new systems

### Control Levels
- **Minimal Control (MVP)**: "Generate random language" or "Generate X-family-style language"
- **Parameter Control**: Adjust phonological/morphological complexity
- **Template Control**: Use specific language family templates
- **Advanced Control**: Fine-tune individual linguistic features

## Output Specifications

### Primary Output: Swadesh List
- 207 core concepts with generated words
- IPA transcriptions for all entries
- Optional anglicized pronunciations
- Morphological analysis for complex words
- Semantic field organization

### Secondary Output: Example Sentences
- 20 sentences demonstrating core grammar
- Range from simple (SVO) to complex (embedded clauses)
- IPA and anglicized versions
- Grammatical annotations
- Translation notes

### File Formats
- **JSON**: Machine-readable language data
- **CSV**: Swadesh lists for spreadsheet analysis
- **Markdown**: Human-readable documentation
- **Plain Text**: Simple word lists

## Language Family Templates

### Planned Templates
- **Random**: No specific family resemblance
- **Indo-European**: Moderate inflection, familiar sound patterns
- **Sino-Tibetan**: Tonal, analytical morphology
- **Austronesian**: Simple phonotactics, verb-initial order
- **Afroasiatic**: Semitic-style root-and-pattern morphology
- **Niger-Congo**: Noun classes, complex tone systems

### Template Parameters
- Phonological inventory constraints
- Morphological complexity settings
- Syntactic feature preferences
- Prosodic system specifications

## Future Enhancements

### Planned Features
- **Phonological Evolution**: Model sound changes over time
- **Dialectal Variation**: Generate related language varieties
- **Writing Systems**: Create alphabets and orthographies
- **Advanced Syntax**: Complex clause structures, discourse markers
- **Semantic Fields**: Expanded vocabulary beyond Swadesh
- **Cultural Integration**: Generate culturally appropriate naming patterns

### Technical Improvements
- **Performance Optimization**: Faster generation algorithms
- **Memory Management**: Handle large language inventories
- **Parallel Processing**: Generate multiple languages simultaneously
- **Machine Learning**: Learn from natural language corpora
- **Visualization**: Interactive phonological and grammatical charts

## Success Metrics

### Test-Driven Development Success
- **Major Achievement**: 12 passing tests (improved from 10) after successful migration
- **Phase 1 Progress**: 2/5 short-term aspirational tests complete (package + Forge API)
- **Phase 2 Progress**: 1/3 long-term aspirational tests complete (basic functionality)
- **Code Quality**: All foundation tests migrated to improved system
- **API Validation**: All public interfaces tested before implementation

### Linguistic Quality  
- Generated languages pass basic typological consistency checks
- **Dramatically improved syllable generation**: Fixed broken regex patterns with direct construction
- **Quality Evidence**: Clean Polynesian (C)V and Sinitic (C)V(C) patterns without artifacts
- Morphological processes apply consistently
- Syntactic patterns follow cross-linguistic universals
- **Current Achievement**: 12 passing tests validate improved phonological realism

### Technical Quality
- Generation time under 30 seconds for complete language
- Memory usage remains reasonable for desktop applications
- Test suite runs in under 30 seconds
- User satisfaction with generated content
- **Current Achievement**: Robust foundation with unified API and dramatically improved output quality
- **Architecture Success**: phones.py → forge.py migration demonstrates test-driven development effectiveness

### Community Engagement
- Active use by worldbuilders and conlang enthusiasts
- Contributions from linguistic community
- Integration with existing conlanging tools
- Educational use in linguistic courses
- **Development Goal**: Open-source project with contributor-friendly test suite

---

*This document serves as the technical and linguistic blueprint for LangForge. All development decisions should align with these goals and principles.* 