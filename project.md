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

### What Works ✅
- **Solid Foundation**: CSV-based phoneme inventory system with IPA organization
- **Syllable Generation**: Regex-based patterns with language family templates
- **Linguistic Realism**: Validated phonotactic constraints and realistic output
- **Comprehensive Testing**: 18 total tests (10 passing, 8 aspirational)
- **Clean Architecture**: Resolved merge conflicts, organized codebase structure
- **Test-Driven Development**: Aspirational tests define clear development roadmap

### Foundation Components (Fully Tested)
- ✅ Phoneme inventory loading and management
- ✅ Syllable structure generation with custom patterns
- ✅ Language family templates (Polynesian, Sinitic, North Sinitic)
- ✅ Data cleaning and validation
- ✅ Linguistic realism verification
- ✅ Reproducibility and consistency checks

### Development Guided by Tests
**10 Passing Tests** validate core functionality:
- Basic syllable generation with custom regex patterns
- Predefined language family pattern integration
- Edge case handling and error management
- Phoneme categorization and data cleaning
- Linguistic realism and variety validation
- Reproducibility and consistency verification

**8 Aspirational Tests** define development roadmap:
- 3 Long-term API goals (Forge class, Swadesh generation, fluent interface)
- 5 Short-term stepping stones (package structure, data classes, templates, I/O, integration)

### Ready for Implementation
- ❌ Package structure and imports (`import langforge`)
- ❌ SwadeshList data structure for concept mapping
- ❌ Template system for language family access
- ❌ CSV/JSON export functionality
- ❌ Phones integration wrapper for new API
- ❌ Morphological system (roots, affixes, word formation)
- ❌ Syntactic system (grammar rules, sentence generation)

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

### Test-Driven Development Approach

**Current Status**: 10 passing tests validate core phonological system, 8 aspirational tests guide development

### Phase 1: Basic API Structure (Short-term Tests)
**Goal**: Make 5 short-term aspirational tests pass

1. **Package Structure** → `test_langforge_package_import`
   - [ ] Create `langforge/__init__.py` with version and exports
   - [ ] Set up basic import structure
   - [ ] Define `Forge` class interface

2. **Data Structures** → `test_swadesh_list_data_structure`
   - [ ] Implement `SwadeshList` class with concept mapping
   - [ ] Add `add_concept()` and `concepts` property
   - [ ] Create basic concept-to-word storage

3. **Template System** → `test_language_family_template_access`
   - [ ] Create `Templates` class wrapping existing `Syllable_patterns`
   - [ ] Add `.available()` and `.get()` methods
   - [ ] Bridge old and new template systems

4. **Export System** → `test_basic_csv_export`
   - [ ] Create `langforge.io.export_csv` function
   - [ ] Handle dictionary-to-CSV conversion
   - [ ] Add basic file I/O operations

5. **Phonology Integration** → `test_phones_integration_wrapper`
   - [ ] Create `PhonologySystem` class wrapping existing `Phones`
   - [ ] Add `.from_csv_files()` class method
   - [ ] Implement `.generate_syllables()` method

### Phase 2: Core API Implementation (Long-term Tests)
**Goal**: Make 3 long-term aspirational tests pass

6. **Forge Class** → `test_forge_api_basic_functionality`
   - [ ] Implement main `Forge` class with `.generate()` method
   - [ ] Create `GeneratedLanguage` class with phonology/syllables/vocabulary
   - [ ] Connect to existing syllable generation system

7. **Swadesh Generation** → `test_forge_swadesh_list_generation`
   - [ ] Implement `Forge.swadesh()` class method
   - [ ] Create concept-to-word mapping logic
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

### Test-Driven Success Metrics
- **Phase 1 Complete**: 15 passing tests (10 current + 5 short-term)
- **Phase 2 Complete**: 18 passing tests (all current aspirational tests pass)
- **Each Phase**: All tests pass, no regressions in existing functionality
- **Continuous**: New features guided by additional aspirational tests

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
- **Phase 1 Complete**: 15 passing tests (10 foundation + 5 short-term aspirational)
- **Phase 2 Complete**: 18 passing tests (all aspirational tests pass)
- **Code Coverage**: Above 80% for core functionality
- **Test Quality**: Comprehensive linguistic realism validation
- **API Validation**: All public interfaces tested before implementation

### Linguistic Quality
- Generated languages pass basic typological consistency checks
- Phonological systems remain stable across word generation
- Morphological processes apply consistently
- Syntactic patterns follow cross-linguistic universals
- **Current Achievement**: 10 passing tests validate phonological realism

### Technical Quality
- Generation time under 30 seconds for complete language
- Memory usage remains reasonable for desktop applications
- Test suite runs in under 30 seconds
- User satisfaction with generated content
- **Current Achievement**: Robust foundation with comprehensive testing

### Community Engagement
- Active use by worldbuilders and conlang enthusiasts
- Contributions from linguistic community
- Integration with existing conlanging tools
- Educational use in linguistic courses
- **Development Goal**: Open-source project with contributor-friendly test suite

---

*This document serves as the technical and linguistic blueprint for LangForge. All development decisions should align with these goals and principles.* 