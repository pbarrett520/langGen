#!/usr/bin/env python3
"""
LangForge Phase 3 Demo: Word Building, Swadesh Lists, and Export

This demo showcases the complete Phase 3 functionality of LangForge:
- Word building from morphemes
- Swadesh list generation
- CSV and JSON export capabilities
- Complete language generation pipeline

NOTE: This demo focuses specifically on Phase 3 features.
For a complete demonstration of all phases with beautiful formatting,
see demo_unified.py which provides a comprehensive, interview-ready showcase.

Use this demo for:
- Detailed exploration of Phase 3 capabilities
- Development and testing of word building features
- Understanding export functionality

Use demo_unified.py for:
- Complete feature demonstrations with professional formatting
- Interviews and presentations
- Showcasing the full LangForge pipeline

Run with: python demo_phase3.py
"""

import os
import tempfile
import json
from forge import Forge


def demo_word_building():
    """Demonstrate word building capabilities across language families."""
    print("=" * 60)
    print("PHASE 3 DEMO: WORD BUILDING")
    print("=" * 60)
    
    forge = Forge()
    
    # Test different language families and strategies
    families = ["polynesian", "japanese", "germanic", "romance", "sinitic"]
    strategies = ["simple", "complex", "mixed"]
    
    print("Building words with different strategies:\n")
    
    for family in families:
        print(f"{family.capitalize()} Language Family:")
        print("-" * 30)
        
        for strategy in strategies:
            words = forge.build_words(family, count=5, strategy=strategy)
            avg_len = sum(len(w) for w in words) / len(words)
            print(f"  {strategy:8} strategy (avg: {avg_len:.1f}): {words}")
        print()


def demo_swadesh_generation():
    """Demonstrate Swadesh list generation with realistic words."""
    print("=" * 60)
    print("PHASE 3 DEMO: SWADESH LIST GENERATION")
    print("=" * 60)
    
    forge = Forge()
    
    # Generate Swadesh lists for different language families
    families = ["polynesian", "japanese", "germanic", "romance"]
    
    for family in families:
        print(f"\n{family.capitalize()} Swadesh List (first 20 concepts):")
        print("-" * 50)
        
        # Generate language and Swadesh list
        language = forge.generate(family)
        swadesh = forge.generate_swadesh(family, count=20)
        
        # Display phonological info
        consonants = ", ".join(language.phonology["consonants"][:10])
        vowels = ", ".join(language.phonology["vowels"])
        print(f"Phonology: C={consonants}... V={vowels}")
        print(f"Generated {len(swadesh)} concept-word mappings:")
        print()
        
        # Display Swadesh mappings in columns
        items = list(swadesh.to_dict().items())
        for i in range(0, len(items), 2):
            left = f"{items[i][0]:12} → {items[i][1]:8}"
            if i + 1 < len(items):
                right = f"{items[i+1][0]:12} → {items[i+1][1]:8}"
                print(f"  {left}  |  {right}")
            else:
                print(f"  {left}")
        print()


def demo_export_functionality():
    """Demonstrate CSV and JSON export capabilities."""
    print("=" * 60)
    print("PHASE 3 DEMO: EXPORT FUNCTIONALITY")
    print("=" * 60)
    
    forge = Forge()
    
    # Generate a language and Swadesh list
    language = forge.generate("romance")
    swadesh = forge.generate_swadesh("romance", count=25)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Exporting to temporary directory: {tmpdir}\n")
        
        # Test CSV export
        csv_path = os.path.join(tmpdir, "romance_swadesh.csv")
        forge.export(swadesh, csv_path, format="csv")
        
        print("1. CSV Export:")
        print(f"   File: {os.path.basename(csv_path)}")
        with open(csv_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:6]  # First 5 lines + header
            for line in lines:
                print(f"   {line.strip()}")
        print(f"   ... ({len(lines)-1} more rows)")
        print()
        
        # Test JSON export (simple)
        json_path = os.path.join(tmpdir, "romance_swadesh.json")
        forge.export(swadesh, json_path, format="json")
        
        print("2. JSON Export (Swadesh only):")
        print(f"   File: {os.path.basename(json_path)}")
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            sample_items = list(data['swadesh'].items())[:5]
            for concept, word in sample_items:
                print(f"   \"{concept}\": \"{word}\"")
        print(f"   ... ({len(data['swadesh'])} total mappings)")
        print()
        
        # Test JSON export with metadata
        meta_path = os.path.join(tmpdir, "romance_complete.json")
        forge.export(swadesh, meta_path, format="json", 
                    include_metadata=True, language=language)
        
        print("3. JSON Export (with language metadata):")
        print(f"   File: {os.path.basename(meta_path)}")
        with open(meta_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"   Keys: {list(data.keys())}")
            print(f"   Language template: {data['language_info']['template']}")
            print(f"   Consonants: {len(data['language_info']['phonology']['consonants'])}")
            print(f"   Vowels: {len(data['language_info']['phonology']['vowels'])}")
            print(f"   Syllables generated: {data['language_info']['syllable_count']}")
        print()
        
        # Test auto-format detection
        auto_csv = os.path.join(tmpdir, "auto_detected.csv")
        auto_json = os.path.join(tmpdir, "auto_detected.json")
        
        forge.export(swadesh, auto_csv)  # Should auto-detect CSV
        forge.export(swadesh, auto_json)  # Should auto-detect JSON
        
        print("4. Auto-format Detection:")
        print(f"   Created CSV: {os.path.exists(auto_csv)}")
        print(f"   Created JSON: {os.path.exists(auto_json)}")


def demo_complete_pipeline():
    """Demonstrate the complete language generation pipeline."""
    print("=" * 60)
    print("PHASE 3 DEMO: COMPLETE PIPELINE")
    print("=" * 60)
    
    forge = Forge()
    
    print("Generating a complete constructed language:\n")
    
    # Step 1: Generate language with phonology
    print("Step 1: Generating phonological system...")
    language = forge.generate("germanic")
    print(f"   Template: {language.template}")
    print(f"   Consonants ({len(language.phonology['consonants'])}): {', '.join(language.phonology['consonants'][:15])}...")
    print(f"   Vowels ({len(language.phonology['vowels'])}): {', '.join(language.phonology['vowels'])}")
    print(f"   Sample syllables: {', '.join(language.syllables[:10])}")
    print()
    
    # Step 2: Generate morphemes
    print("Step 2: Generating morpheme inventory...")
    roots = forge.morphemes("germanic", type="roots", count=15)
    affixes = forge.morphemes("germanic", type="affixes", count=8)
    print(f"   Roots ({len(roots)}): {', '.join(roots[:10])}")
    print(f"   Affixes ({len(affixes)}): {', '.join(affixes)}")
    print()
    
    # Step 3: Build vocabulary
    print("Step 3: Building vocabulary...")
    words = forge.build_words("germanic", count=30, strategy="mixed")
    avg_word_len = sum(len(w) for w in words) / len(words)
    print(f"   Generated {len(words)} words (avg length: {avg_word_len:.1f})")
    print(f"   Sample vocabulary: {', '.join(words[:12])}")
    print()
    
    # Step 4: Generate Swadesh list
    print("Step 4: Generating Swadesh list...")
    swadesh = forge.generate_swadesh("germanic", count=50)
    print(f"   Generated {len(swadesh)} concept mappings")
    
    # Show semantic categories
    categories = {
        "Basic": ["I", "you", "we", "this", "that"],
        "Nature": ["water", "fire", "sun", "moon", "tree"],
        "Body": ["head", "eye", "hand", "foot", "heart"],
        "Actions": ["eat", "drink", "see", "hear", "walk"]
    }
    
    for category, concepts in categories.items():
        available = [c for c in concepts if c in swadesh]
        if available:
            words_in_cat = [f"{c}→{swadesh.get_word(c)}" for c in available[:3]]
            print(f"   {category}: {', '.join(words_in_cat)}")
    print()
    
    # Step 5: Export everything
    print("Step 5: Exporting complete language...")
    with tempfile.TemporaryDirectory() as tmpdir:
        output_file = os.path.join(tmpdir, "germanic_language.json")
        forge.export(swadesh, output_file, format="json", 
                    include_metadata=True, language=language)
        
        # Display file size and structure
        file_size = os.path.getsize(output_file)
        print(f"   Exported to: {os.path.basename(output_file)}")
        print(f"   File size: {file_size:,} bytes")
        
        with open(output_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"   Swadesh concepts: {len(data['swadesh'])}")
            print(f"   Language metadata: {len(data['language_info'])} fields")
    
    print("\n✓ Complete language generation pipeline successful!")


def demo_linguistic_realism():
    """Demonstrate linguistic realism across different language families."""
    print("=" * 60)
    print("PHASE 3 DEMO: LINGUISTIC REALISM")
    print("=" * 60)
    
    forge = Forge()
    
    print("Comparing linguistic characteristics across families:\n")
    
    families = {
        "polynesian": "Simple CV syllables, limited consonants",
        "japanese": "CV(n) only, strict phonotactics", 
        "germanic": "Complex clusters, long words",
        "romance": "Open syllables, flowing sounds",
        "sinitic": "Limited finals, tonal-ready"
    }
    
    for family, description in families.items():
        print(f"{family.capitalize()} ({description}):")
        print("-" * 50)
        
        # Generate samples
        words = forge.build_words(family, count=8, strategy="mixed")
        swadesh = forge.generate_swadesh(family, count=15)
        
        # Calculate stats
        avg_word_len = sum(len(w) for w in words) / len(words)
        max_word_len = max(len(w) for w in words)
        
        print(f"  Word length - Avg: {avg_word_len:.1f}, Max: {max_word_len}")
        print(f"  Sample words: {', '.join(words[:6])}")
        
        # Show how basic concepts are realized
        basic_concepts = ["water", "fire", "big", "eat"]
        realizations = []
        for concept in basic_concepts:
            if concept in swadesh:
                realizations.append(f"{concept}={swadesh.get_word(concept)}")
        print(f"  Basic concepts: {', '.join(realizations[:3])}")
        print()


def main():
    """Run all Phase 3 demos."""
    print("🚀 LangForge Phase 3 Complete Functionality Demo")
    print("Built with systematic TDD approach for maximum reliability\n")
    
    try:
        demo_word_building()
        demo_swadesh_generation()
        demo_export_functionality()
        demo_complete_pipeline()
        demo_linguistic_realism()
        
        print("=" * 60)
        print("DEMO COMPLETE ✓")
        print("=" * 60)
        print("All Phase 3 features demonstrated successfully!")
        print("\nPhase 3 includes:")
        print("  ✓ Intelligent word building from morphemes")
        print("  ✓ Complete Swadesh list generation")
        print("  ✓ CSV and JSON export with metadata")
        print("  ✓ Linguistic realism across language families")
        print("  ✓ Full pipeline from phonology to vocabulary")
        print("\nLangForge is now ready for advanced conlang generation! 🎯")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        print("Please check the implementation and try again.")


if __name__ == "__main__":
    main() 