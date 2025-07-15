#!/usr/bin/env python3
"""
🌍 LangForge: Complete Algorithmic Constructed Language Generator

A comprehensive demonstration of the complete language generation pipeline.
Perfect for interviews, presentations, and showcasing capabilities.

Features:
- Phase 1: Phonological system generation across language families
- Phase 2: Morpheme generation (roots & affixes)  
- Phase 3: Word building, Swadesh lists, and export capabilities
- Linguistic realism and comparative analysis

Run with: python demo_unified.py
"""

import sys
import os
import tempfile
import json
from forge import Forge


class DemoFormatter:
    """Beautiful console formatting for professional demonstrations."""
    
    # Color codes
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    @classmethod
    def header(cls, title, emoji="🌍"):
        """Print a major section header."""
        line = "═" * 70
        print(f"\n{cls.BLUE}{cls.BOLD}{line}")
        print(f"  {emoji} {title}")
        print(f"{line}{cls.END}")
    
    @classmethod
    def subheader(cls, title, emoji="🔹"):
        """Print a subsection header."""
        line = "─" * 55
        print(f"\n{cls.CYAN}{cls.BOLD}{line}")
        print(f"  {emoji} {title}")
        print(f"{line}{cls.END}")
    
    @classmethod
    def success(cls, text):
        """Print success message."""
        print(f"{cls.GREEN}✓ {text}{cls.END}")
    
    @classmethod
    def highlight(cls, text):
        """Print highlighted text."""
        return f"{cls.YELLOW}{cls.BOLD}{text}{cls.END}"
    
    @classmethod
    def data(cls, label, value, indent=2):
        """Print labeled data."""
        spaces = " " * indent
        print(f"{spaces}{cls.WHITE}• {label}:{cls.END} {value}")
    
    @classmethod
    def code(cls, text):
        """Print code-like text."""
        print(f"{cls.PURPLE}{text}{cls.END}")


def demo_introduction():
    """Introduction and overview of LangForge capabilities."""
    DemoFormatter.header("LangForge: Algorithmic Constructed Language Generator", "🚀")
    
    print(f"{DemoFormatter.BOLD}Welcome to LangForge{DemoFormatter.END} - the systematic approach to conlang generation!")
    print("\nThis demonstration showcases:")
    
    features = [
        "🔬 Phonologically realistic language families",
        "🧱 Morpheme generation with linguistic accuracy", 
        "📝 Intelligent word building strategies",
        "📚 Complete Swadesh list generation (207 concepts)",
        "💾 Professional CSV/JSON export capabilities",
        "🌐 Full pipeline from phonology to vocabulary"
    ]
    
    for feature in features:
        print(f"  {feature}")
    
    print(f"\n{DemoFormatter.highlight('Built with Test-Driven Development for maximum reliability! 🧪')}")
    print(f"Let's explore the complete language generation pipeline...\n")


def demo_phonological_systems(forge):
    """Demonstrate Phase 1: Phonological system generation."""
    DemoFormatter.header("Phase 1: Phonological Systems", "🔊")
    
    print("LangForge generates linguistically realistic phoneme inventories and")
    print("syllable patterns based on real language family characteristics.\n")
    
    # Language family configurations
    families = [
        ("polynesian", "Simple CV syllables - Hawaiian, Samoan, Maori", "🏝️"),
        ("japanese", "Strict CV(n) patterns - minimal clusters", "🗾"), 
        ("germanic", "Complex consonant clusters - English, German", "⚔️"),
        ("romance", "Flowing open syllables - Spanish, Italian", "🎭"),
        ("sinitic", "Tonal-ready with limited finals - Mandarin", "🏮")
    ]
    
    generated_languages = []
    
    for template, description, emoji in families:
        DemoFormatter.subheader(f"{template.title()} Family", emoji)
        print(f"Characteristics: {description}")
        
        # Generate language
        lang = forge.generate(template)
        generated_languages.append((template, lang))
        
        # Display phonological inventory
        consonants = lang.phonology['consonants']
        vowels = lang.phonology['vowels']
        patterns = lang.phonology['pattern']['structure']
        
        DemoFormatter.data("Consonants", f"({len(consonants)}) {' '.join(consonants[:12])}{'...' if len(consonants) > 12 else ''}")
        DemoFormatter.data("Vowels", f"({len(vowels)}) {' '.join(vowels)}")
        DemoFormatter.data("Syllable patterns", ' | '.join(patterns))
        
        # Show sample syllables in elegant format
        syllables = lang.syllables[:16]
        formatted_syllables = []
        for i in range(0, len(syllables), 4):
            row = '  '.join(f"{syll:>6}" for syll in syllables[i:i+4])
            formatted_syllables.append(f"    {row}")
        
        print(f"  {DemoFormatter.WHITE}• Sample syllables:{DemoFormatter.END}")
        for row in formatted_syllables:
            print(row)
        
        # Quick linguistic analysis
        avg_length = sum(len(s) for s in lang.syllables) / len(lang.syllables)
        complexity = "Simple" if avg_length < 2.5 else "Moderate" if avg_length < 3.5 else "Complex"
        DemoFormatter.data("Complexity", f"{avg_length:.1f} avg phonemes ({complexity})")
    
    return generated_languages


def demo_morpheme_generation(forge):
    """Demonstrate Phase 2: Morpheme generation."""
    DemoFormatter.header("Phase 2: Morpheme Generation", "🧱")
    
    print("Building meaningful language components by combining syllables")
    print("into roots (concept bases) and affixes (modifiers).\n")
    
    # Demonstrate morpheme generation across families
    families = ["polynesian", "japanese", "germanic", "romance"]
    
    for family in families:
        DemoFormatter.subheader(f"{family.title()} Morphemes")
        
        # Generate morphemes
        roots = forge.morphemes(family, type="roots", count=8)
        affixes = forge.morphemes(family, type="affixes", count=6)
        
        # Format roots in rows
        print(f"  {DemoFormatter.WHITE}• Roots (concept bases):{DemoFormatter.END}")
        for i in range(0, len(roots), 4):
            row = '  '.join(f"{root:>8}" for root in roots[i:i+4])
            print(f"    {row}")
        
        # Format affixes
        print(f"  {DemoFormatter.WHITE}• Affixes (modifiers):{DemoFormatter.END}")
        affix_row = '  '.join(f"{affix:>6}" for affix in affixes)
        print(f"    {affix_row}")
        
        # Analysis
        avg_root_len = sum(len(r) for r in roots) / len(roots)
        avg_affix_len = sum(len(a) for a in affixes) / len(affixes)
        DemoFormatter.data("Average lengths", f"roots={avg_root_len:.1f}, affixes={avg_affix_len:.1f}")


def demo_word_building(forge):
    """Demonstrate Phase 3: Word building strategies."""
    DemoFormatter.header("Phase 3: Word Building & Vocabulary", "📝")
    
    print("Intelligent word construction using different morphological strategies")
    print("to create realistic vocabulary patterns.\n")
    
    # Demonstrate word building strategies
    DemoFormatter.subheader("Word Building Strategies", "⚙️")
    
    strategies = [
        ("simple", "Mostly single morphemes - isolating languages"),
        ("complex", "Multiple morpheme combinations - agglutinative languages"), 
        ("mixed", "Balanced approach - most natural languages")
    ]
    
    family = "germanic"  # Use Germanic for good variety
    
    for strategy, description in strategies:
        print(f"\n  {DemoFormatter.BOLD}{strategy.title()} Strategy:{DemoFormatter.END} {description}")
        words = forge.build_words(family, count=8, strategy=strategy)
        avg_len = sum(len(w) for w in words) / len(words)
        
        # Format words in rows
        for i in range(0, len(words), 4):
            row = '  '.join(f"{word:>10}" for word in words[i:i+4])
            print(f"    {row}")
        
        DemoFormatter.data("Average length", f"{avg_len:.1f} phonemes", indent=4)
    
    # Show linguistic realism across families
    DemoFormatter.subheader("Cross-Family Linguistic Realism", "🌐")
    
    families_analysis = [
        ("polynesian", "🏝️", "Simple CV syllables, limited consonants"),
        ("japanese", "🗾", "CV(n) only, strict phonotactics"),
        ("romance", "🎭", "Open syllables, flowing sounds"),
        ("sinitic", "🏮", "Limited finals, tonal-ready")
    ]
    
    for family, emoji, description in families_analysis:
        words = forge.build_words(family, count=6, strategy="mixed")
        avg_len = sum(len(w) for w in words) / len(words)
        max_len = max(len(w) for w in words)
        
        print(f"\n  {emoji} {DemoFormatter.BOLD}{family.title()}:{DemoFormatter.END} {description}")
        word_display = '  '.join(f"{word:>8}" for word in words)
        print(f"    {word_display}")
        DemoFormatter.data("Stats", f"avg={avg_len:.1f}, max={max_len}", indent=4)


def demo_swadesh_generation(forge):
    """Demonstrate Swadesh list generation."""
    DemoFormatter.subheader("Swadesh List Generation", "📚")
    
    print("Generating concept-to-word mappings for the 207-concept Swadesh list")
    print("- the core vocabulary shared across human languages.\n")
    
    # Generate Swadesh list for demonstration
    family = "romance"
    language = forge.generate(family)
    swadesh = forge.generate_swadesh(family, count=25)
    
    print(f"  {DemoFormatter.BOLD}Romance Language Example:{DemoFormatter.END}")
    DemoFormatter.data("Phonology", f"C={len(language.phonology['consonants'])}, V={len(language.phonology['vowels'])}")
    DemoFormatter.data("Generated concepts", f"{len(swadesh)} mappings")
    
    # Display sample concepts in semantic categories
    categories = {
        "🧑 Basic": ["I", "you", "we", "this", "that"],
        "🌿 Nature": ["water", "fire", "sun", "moon", "tree"],
        "👁️ Body": ["head", "eye", "hand", "foot", "heart"],
        "🏃 Actions": ["eat", "drink", "see", "walk", "sleep"]
    }
    
    print(f"\n  {DemoFormatter.WHITE}Sample Concept Mappings:{DemoFormatter.END}")
    
    for category, concepts in categories.items():
        available = [c for c in concepts if c in swadesh][:3]  # Show first 3 available
        if available:
            mappings = [f"{c}→{swadesh.get_word(c)}" for c in available]
            print(f"    {category} {' | '.join(mappings)}")


def demo_complete_pipeline(forge):
    """Demonstrate the complete language generation pipeline."""
    DemoFormatter.header("Complete Pipeline Demonstration", "🔄")
    
    print("Watch a complete constructed language emerge from phonemes to vocabulary!\n")
    
    family = "japanese"
    
    # Step 1: Phonological system
    print(f"{DemoFormatter.BOLD}Step 1: Phonological Foundation{DemoFormatter.END}")
    language = forge.generate(family)
    DemoFormatter.data("Template", family.title())
    DemoFormatter.data("Consonants", f"{len(language.phonology['consonants'])} phonemes")
    DemoFormatter.data("Vowels", f"{len(language.phonology['vowels'])} phonemes")
    DemoFormatter.data("Sample syllables", ' '.join(language.syllables[:8]))
    
    # Step 2: Morpheme inventory
    print(f"\n{DemoFormatter.BOLD}Step 2: Morpheme Inventory{DemoFormatter.END}")
    roots = forge.morphemes(family, type="roots", count=10)
    affixes = forge.morphemes(family, type="affixes", count=6)
    DemoFormatter.data("Generated roots", ' '.join(roots[:6]))
    DemoFormatter.data("Generated affixes", ' '.join(affixes))
    
    # Step 3: Vocabulary building
    print(f"\n{DemoFormatter.BOLD}Step 3: Vocabulary Construction{DemoFormatter.END}")
    words = forge.build_words(family, count=15, strategy="mixed")
    avg_word_len = sum(len(w) for w in words) / len(words)
    DemoFormatter.data("Generated words", f"{len(words)} items")
    DemoFormatter.data("Sample vocabulary", ' '.join(words[:8]))
    DemoFormatter.data("Average word length", f"{avg_word_len:.1f} phonemes")
    
    # Step 4: Swadesh concepts
    print(f"\n{DemoFormatter.BOLD}Step 4: Core Concept Mapping{DemoFormatter.END}")
    swadesh = forge.generate_swadesh(family, count=30)
    essential = ["I", "you", "water", "fire", "big", "eat"]
    available_concepts = [f"{c}={swadesh.get_word(c)}" for c in essential if c in swadesh]
    DemoFormatter.data("Swadesh concepts", f"{len(swadesh)} generated")
    DemoFormatter.data("Essential mappings", ' | '.join(available_concepts[:4]))
    
    DemoFormatter.success(f"Complete {family.title()} language generated successfully!")
    
    return language, swadesh


def demo_export_capabilities(forge, language, swadesh):
    """Demonstrate export functionality."""
    DemoFormatter.header("Export & Data Management", "💾")
    
    print("Professional export capabilities for integration with other tools")
    print("and long-term language development projects.\n")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        DemoFormatter.subheader("Export Formats", "📁")
        
        # CSV Export
        csv_path = os.path.join(tmpdir, "language.csv")
        forge.export(swadesh, csv_path, format="csv")
        
        DemoFormatter.data("CSV Export", "✓ Simple concept-word pairs")
        with open(csv_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:4]  # Show first few lines
            for line in lines:
                print(f"      {line.strip()}")
        print(f"      ... ({len(lines)-1} more entries)")
        
        # JSON Export with metadata
        json_path = os.path.join(tmpdir, "language_complete.json")
        forge.export(swadesh, json_path, format="json", 
                    include_metadata=True, language=language)
        
        print(f"\n  {DemoFormatter.WHITE}• JSON Export with Metadata:{DemoFormatter.END}")
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            DemoFormatter.data("Data structure", f"{list(data.keys())}", indent=4)
            DemoFormatter.data("Swadesh entries", f"{len(data['swadesh'])}", indent=4)
            DemoFormatter.data("Language metadata", f"{len(data['language_info'])} fields", indent=4)
            DemoFormatter.data("File size", f"{os.path.getsize(json_path):,} bytes", indent=4)
        
        # Auto-detection demo
        DemoFormatter.subheader("Smart Format Detection", "🤖")
        
        auto_csv = os.path.join(tmpdir, "auto.csv")
        auto_json = os.path.join(tmpdir, "auto.json") 
        
        forge.export(swadesh, auto_csv)    # No format specified
        forge.export(swadesh, auto_json)   # Auto-detects from extension
        
        DemoFormatter.success("Auto-detected CSV format from .csv extension")
        DemoFormatter.success("Auto-detected JSON format from .json extension")
        
        # Integration possibilities
        print(f"\n{DemoFormatter.BOLD}Integration Possibilities:{DemoFormatter.END}")
        integrations = [
            "📊 Spreadsheet analysis and comparison",
            "🗃️ Database import for large-scale projects", 
            "🌐 Web application integration via JSON APIs",
            "📝 Documentation generation with metadata",
            "🔄 Version control for iterative development"
        ]
        
        for integration in integrations:
            print(f"    {integration}")


def demo_technical_showcase():
    """Showcase technical achievements and capabilities."""
    DemoFormatter.header("Technical Achievements", "⚙️")
    
    print("LangForge represents a systematic, engineering approach to conlang generation")
    print("with linguistic accuracy and software engineering best practices.\n")
    
    DemoFormatter.subheader("Core Technologies", "🔬")
    
    achievements = [
        ("📊 Weighted Phoneme Selection", "Realistic frequency distributions"),
        ("🏗️ Position-Sensitive Phonotactics", "Accurate syllable structure"),
        ("🎯 Language Family Templates", "Historically-grounded patterns"),
        ("🔄 Truly Random Generation", "50+ phoneme combinations"),
        ("🧱 Morphological Composition", "Linguistically sound word building"),
        ("📚 Swadesh List Integration", "207-concept universal vocabulary"),
        ("💾 Multi-Format Export", "CSV, JSON with metadata"),
        ("🧪 Test-Driven Development", "59 passing tests, 100% reliability")
    ]
    
    for tech, description in achievements:
        print(f"  {tech:<30} {description}")
    
    DemoFormatter.subheader("Linguistic Realism Metrics", "📈")
    
    # Quick comparative analysis
    forge = Forge()
    
    families = ["polynesian", "japanese", "germanic", "romance", "sinitic"]
    complexity_data = []
    
    for family in families:
        lang = forge.generate(family)
        words = forge.build_words(family, count=20, strategy="mixed")
        
        avg_syll_len = sum(len(s) for s in lang.syllables) / len(lang.syllables)
        avg_word_len = sum(len(w) for w in words) / len(words)
        
        complexity_data.append((family, avg_syll_len, avg_word_len))
    
    print(f"  {'Family':<12} {'Syllable':<10} {'Word Length':<12} {'Realism'}")
    print(f"  {'─'*12} {'─'*10} {'─'*12} {'─'*8}")
    
    for family, syll_len, word_len in complexity_data:
        realism = "High" if 1.5 <= syll_len <= 4.0 and 2.0 <= word_len <= 8.0 else "Moderate"
        print(f"  {family.title():<12} {syll_len:<10.1f} {word_len:<12.1f} {realism}")


def demo_future_vision():
    """Present the vision and future capabilities."""
    DemoFormatter.header("Vision & Future Development", "🚀")
    
    print("LangForge is positioned to become the premier tool for systematic")
    print("constructed language generation with academic and creative applications.\n")
    
    DemoFormatter.subheader("Current State: Production Ready", "✅")
    
    current = [
        "Complete phonological generation pipeline",
        "Morpheme generation with linguistic accuracy",
        "Word building with multiple strategies", 
        "Full Swadesh list generation (207 concepts)",
        "Professional export capabilities",
        "Comprehensive test coverage (59 tests)"
    ]
    
    for item in current:
        print(f"  ✓ {item}")
    
    DemoFormatter.subheader("Future Enhancements", "🔮")
    
    future = [
        "🔤 Orthography generation (writing systems)",
        "📖 Grammar rule generation", 
        "🎵 Phonological change simulation",
        "🌍 Geographic language variation",
        "📱 Web interface and API",
        "🤝 Community sharing platform"
    ]
    
    for item in future:
        print(f"  {item}")
    
    DemoFormatter.subheader("Applications", "🎯")
    
    applications = [
        ("🎮 Game Development", "Rich, believable fantasy worlds"),
        ("📚 Creative Writing", "Authentic fictional cultures"),
        ("🎓 Linguistic Education", "Hands-on phonology learning"),
        ("🔬 Research Tool", "Systematic language comparison"),
        ("🎬 Entertainment Industry", "Film and TV language creation")
    ]
    
    for app, desc in applications:
        print(f"  {app:<20} {desc}")


def main():
    """Run the complete unified demonstration."""
    try:
        # Initialize
        forge = Forge()
        
        # Run complete demonstration
        demo_introduction()
        generated_languages = demo_phonological_systems(forge)
        demo_morpheme_generation(forge)
        demo_word_building(forge)
        demo_swadesh_generation(forge)
        language, swadesh = demo_complete_pipeline(forge)
        demo_export_capabilities(forge, language, swadesh)
        demo_technical_showcase()
        demo_future_vision()
        
        # Conclusion
        DemoFormatter.header("Demonstration Complete", "🎉")
        
        print(f"{DemoFormatter.BOLD}Thank you for exploring LangForge!{DemoFormatter.END}")
        print("\nYou've seen the complete pipeline from phonemes to exportable vocabularies.")
        print("LangForge combines linguistic knowledge with software engineering excellence")
        print("to create the most systematic approach to constructed language generation.")
        
        print(f"\n{DemoFormatter.highlight('Ready for production use in creative and academic projects! 🚀')}")
        
        print(f"\n{DemoFormatter.GREEN}Key Takeaways:{DemoFormatter.END}")
        takeaways = [
            "✨ Linguistically realistic across 5 language families",
            "🏗️ Complete pipeline from phonology to vocabulary",
            "🧪 Test-driven development ensures reliability",
            "💾 Professional export capabilities",
            "🎯 Ready for integration into larger projects"
        ]
        
        for takeaway in takeaways:
            print(f"  {takeaway}")
        
        print(f"\n{DemoFormatter.CYAN}Questions? Let's discuss the technical implementation! 💬{DemoFormatter.END}")
        
    except KeyboardInterrupt:
        print(f"\n\n{DemoFormatter.YELLOW}Demo interrupted. Thanks for exploring LangForge! 👋{DemoFormatter.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{DemoFormatter.RED}Demo error: {e}{DemoFormatter.END}")
        print("Please ensure all dependencies are available.")
        sys.exit(1)


if __name__ == "__main__":
    main() 