"""
LangForge: Algorithmic Constructed Language Generator

A systematic, test-driven approach to generating complete constructed languages
from phonemic inventory through Swadesh lists to example sentences.
"""

__version__ = "0.1.0"

from .forge import Forge, SwadeshList

# Add explicit type annotations for better IDE support
__all__: list[str] = ["Forge", "SwadeshList"]
