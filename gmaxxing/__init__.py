"""
gmaxxing — career acceleration through strategic LOC expansion.

Boost your numbers. Make the diff count. When leadership asks what you shipped,
the answer is volume—and a little cosmic alignment never hurt a sprint.
"""

from gmaxxing.engine import cosmic_hash, mercury_risk_score
from gmaxxing.pitch import BARBS, MISSION, PITCH, SUBHEAD, TAGLINE, barb
from gmaxxing.types import (
    AspectKind,
    House,
    MoonPhase,
    TransitPhase,
    ZodiacSign,
)

__version__ = "0.1.0"

__all__ = [
    "BARBS",
    "AspectKind",
    "House",
    "MISSION",
    "MoonPhase",
    "PITCH",
    "SUBHEAD",
    "TAGLINE",
    "TransitPhase",
    "ZodiacSign",
    "__version__",
    "barb",
    "cosmic_hash",
    "mercury_risk_score",
]
