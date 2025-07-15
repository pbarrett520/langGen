#!/usr/bin/env python3
"""
LangForge Demo - Algorithmic Constructed Language Generator

A beautiful demonstration of phonologically realistic language generation.
Perfect for showcasing the project's capabilities.

NOTE: This demo focuses on Phase 1 (phonology) and Phase 2 (morphemes).
For a complete demonstration including Phase 3 (word building, Swadesh lists, export),
see demo_unified.py which provides a comprehensive, interview-ready showcase.

Use this demo for:
- Focused exploration of phonological systems
- Educational demonstrations of syllable generation
- Development and testing of morpheme capabilities

Use demo_unified.py for:
- Complete feature demonstrations
- Interviews and presentations
- Showcasing the full LangForge pipeline
"""

import sys
from forge import Forge


def print_header(title):
    """Print a beautiful header for sections."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_subheader(title):
    """Print a subheader for subsections."""
    print(f"\n{'-'*50}")
    print(f"  {title}")
    print(f"{'-'*50}")


def print_language_demo(forge, template_name, description):
    """Demo a specific language pattern with analysis."""
    print_subheader(f"{template_name.upper()} Language Pattern")
    print(f"Description: {description}")

    # Generate language
    lang = forge.generate(template_name)

    # Show phoneme inventory
    print(f"\nPhoneme Inventory:")
    print(
        f"  • Consonants ({len(lang.phonology['consonants'])}): {' '.join(lang.phonology['consonants'])}"
    )
    print(
        f"  • Vowels ({len(lang.phonology['vowels'])}): {' '.join(lang.phonology['vowels'])}"
    )

    # Show syllable patterns
    structures = lang.phonology["pattern"]["structure"]
    print(f"  • Syllable patterns: {' | '.join(structures)}")

    # Show generated syllables
    print(f"\nGenerated Syllables:")
    syllables = lang.syllables[:12]  # Show first 12

    # Format syllables in rows of 4
    for i in range(0, len(syllables), 4):
        row = syllables[i : i + 4]
        formatted_row = "  ".join(f"{syll:>6}" for syll in row)
        print(f"    {formatted_row}")

    # Generate and show morphemes
    print(f"\nGenerated Morphemes:")
    roots = forge.morphemes(template_name, type="roots", count=8)
    affixes = forge.morphemes(template_name, type="affixes", count=4)

    print(f"  Roots (concept bases):")
    for i in range(0, len(roots), 4):
        row = roots[i : i + 4]
        formatted_row = "  ".join(f"{root:>8}" for root in row)
        print(f"    {formatted_row}")

    print(f"  Affixes (modifiers):")
    formatted_affixes = "  ".join(f"{affix:>6}" for affix in affixes)
    print(f"    {formatted_affixes}")

    # Basic linguistic analysis
    avg_length = sum(len(s) for s in lang.syllables) / len(lang.syllables)
    max_length = max(len(s) for s in lang.syllables)
    unique_count = len(set(lang.syllables))

    # Morpheme analysis
    avg_root_length = sum(len(r) for r in roots) / len(roots)
    avg_affix_length = sum(len(a) for a in affixes) / len(affixes)

    print(f"\nLinguistic Analysis:")
    print(f"  • Average syllable length: {avg_length:.1f} phonemes")
    print(f"  • Maximum syllable length: {max_length} phonemes")
    print(f"  • Unique syllables: {unique_count}/{len(lang.syllables)}")
    print(f"  • Average root length: {avg_root_length:.1f} phonemes")
    print(f"  • Average affix length: {avg_affix_length:.1f} phonemes")

    return lang


def demo_random_comparison(forge):
    """Demonstrate truly random pattern generation."""
    print_subheader("TRULY RANDOM Generation Comparison")
    print("Each call generates completely different phoneme inventories:")

    for i in range(1, 4):
        print(f"\nRandom Language #{i}:")
        lang = forge.generate("random")

        # Show key differences
        consonants = lang.phonology["consonants"][:8]
        vowels = lang.phonology["vowels"][:6]
        structures = lang.phonology["pattern"]["structure"]

        print(f"  • Consonants: {' '.join(consonants)} ...")
        print(f"  • Vowels: {' '.join(vowels)} ...")
        print(f"  • Patterns: {' | '.join(structures)}")
        print(f"  • Sample: {' '.join(lang.syllables[:6])}")


def demo_morpheme_progression(forge):
    """Demonstrate how morphemes build on syllables for language building."""
    print_subheader("MORPHEME PROGRESSION - Building Words from Syllables")
    print("Demonstrating the progression: Syllables → Morphemes → Future Words")

    # Pick a language to show progression
    template = "polynesian"
    lang = forge.generate(template)

    print(f"\n🔗 Using {template.title()} as example:")
    print(f"Step 1: Generate syllables from phoneme inventory")
    print(
        f"  Phonemes: {' '.join(lang.phonology['consonants'][:8])} | {' '.join(lang.phonology['vowels'])}"
    )
    print(f"  Syllables: {' '.join(lang.syllables[:8])}")

    print(f"\nStep 2: Combine syllables into morphemes")
    roots = forge.morphemes(template, type="roots", count=6)
    affixes = forge.morphemes(template, type="affixes", count=4)
    print(f"  Roots: {' '.join(roots)}")
    print(f"  Affixes: {' '.join(affixes)}")

    print(f"\nStep 3: Language-specific morpheme patterns")
    templates = ["japanese", "germanic", "sinitic"]
    for t in templates:
        sample_roots = forge.morphemes(t, type="roots", count=3)
        sample_affixes = forge.morphemes(t, type="affixes", count=2)
        print(
            f"  {t.title():>10}: roots={' '.join(sample_roots)}, affixes={' '.join(sample_affixes)}"
        )

    print(f"\n🎯 Next Phase: Word Building")
    print(f"  Future: root + affix → complete words")
    print(f"  Example: '{roots[0]}' + '{affixes[0]}' → '{roots[0]}{affixes[0]}'")
    print(f"  Goal: 207-concept Swadesh list generation")


def main():
    """Main demo function."""
    print_header("🌍 LangForge: Algorithmic Constructed Language Generator")
    print(
        "\nWelcome to LangForge - creating linguistically realistic constructed languages!"
    )
    print(
        "This demo showcases different language family patterns with phonological analysis."
    )

    # Initialize the forge
    forge = Forge()

    # Demo different language families
    languages = [
        (
            "polynesian",
            "Simple open syllables typical of Pacific languages like Hawaiian",
        ),
        ("japanese", "Predominantly CV patterns with minimal consonant clusters"),
        ("romance", "Flowing syllables inspired by Spanish, Italian, and French"),
        ("germanic", "Complex clusters and diverse vowels like English and German"),
        ("sinitic", "Tonal-ready patterns with limited final consonants like Mandarin"),
    ]

    generated_langs = []
    for template, description in languages:
        lang = print_language_demo(forge, template, description)
        generated_langs.append((template, lang))

    # Demo truly random generation
    demo_random_comparison(forge)

    # Demo morpheme generation capabilities
    demo_morpheme_progression(forge)

    # Comparative analysis
    print_subheader("COMPARATIVE ANALYSIS")
    print("Comparing average syllable complexity across language families:")

    for template, lang in generated_langs:
        avg_length = sum(len(s) for s in lang.syllables) / len(lang.syllables)
        complexity = (
            "Simple"
            if avg_length < 2.5
            else "Moderate" if avg_length < 3.5 else "Complex"
        )
        print(f"  • {template.title():>12}: {avg_length:.1f} phonemes ({complexity})")

    # Technical showcase
    print_subheader("TECHNICAL FEATURES")
    print("✓ Linguistically accurate phoneme inventories")
    print("✓ Weighted syllable structure generation")
    print("✓ Position-sensitive consonant placement")
    print("✓ Language family-specific phonotactic constraints")
    print("✓ Truly random pattern generation with 50+ phonemes")
    print("✓ Morpheme generation building on syllable patterns")
    print("✓ Root and affix generation with realistic lengths")
    print("✓ Language-specific morpheme complexity patterns")
    print("✓ Test-driven development with comprehensive coverage")

    print_header("🎯 Demo Complete!")
    print("LangForge generates realistic constructed languages suitable for:")
    print("  • Worldbuilding and creative writing")
    print("  • Linguistic research and experimentation")
    print("  • Game development and fantasy settings")
    print("  • Educational demonstrations of phonological systems")
    print("  • Morpheme analysis and word formation studies")

    print(f"\n🚀 Current Capabilities:")
    print(f"  ✅ Syllable generation across 5 language families")
    print(f"  ✅ Morpheme generation (roots & affixes)")
    print(f"  🔄 Coming Next: Word building & Swadesh lists")

    print(f"\nThanks for exploring LangForge! 🌍")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Thanks for exploring LangForge! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\nDemo error: {e}")
        print("Please check that forge.py is available in the current directory.")
        sys.exit(1)
