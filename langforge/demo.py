#!/usr/bin/env python3
"""
LangForge Demo - Algorithmic Constructed Language Generator

A beautiful demonstration of phonologically realistic language generation.
Perfect for showcasing the project's capabilities.
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

    # Basic linguistic analysis
    avg_length = sum(len(s) for s in lang.syllables) / len(lang.syllables)
    max_length = max(len(s) for s in lang.syllables)
    unique_count = len(set(lang.syllables))

    print(f"\nLinguistic Analysis:")
    print(f"  • Average syllable length: {avg_length:.1f} phonemes")
    print(f"  • Maximum syllable length: {max_length} phonemes")
    print(f"  • Unique syllables: {unique_count}/{len(lang.syllables)}")

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
    print("✓ Test-driven development with comprehensive coverage")

    print_header("🎯 Demo Complete!")
    print("LangForge generates realistic constructed languages suitable for:")
    print("  • Worldbuilding and creative writing")
    print("  • Linguistic research and experimentation")
    print("  • Game development and fantasy settings")
    print("  • Educational demonstrations of phonological systems")

    print(f"\nThanks for exploring LangForge! 🚀")


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
