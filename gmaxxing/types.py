"""Chart-shaped enums so your module tree looks like you own the vertical."""

from __future__ import annotations

from enum import IntEnum


class ZodiacSign(IntEnum):
    ARIES = 0
    TAURUS = 1
    GEMINI = 2
    CANCER = 3
    LEO = 4
    VIRGO = 5
    LIBRA = 6
    SCORPIO = 7
    SAGITTARIUS = 8
    CAPRICORN = 9
    AQUARIUS = 10
    PISCES = 11


class House(IntEnum):
    H1 = 1
    H2 = 2
    H3 = 3
    H4 = 4
    H5 = 5
    H6 = 6
    H7 = 7
    H8 = 8
    H9 = 9
    H10 = 10
    H11 = 11
    H12 = 12


class TransitPhase(IntEnum):
    DIRECT = 0
    RETROGRADE = 1
    STATIONARY = 2
    IMAGINED = 3


class MoonPhase(IntEnum):
    NEW = 0
    WAXING = 1
    FULL = 2
    WANING = 3
    PLACEHOLDER = 4


class AspectKind(IntEnum):
    CONJUNCTION = 0
    SQUARE = 1
    TRINE = 2
    OPPOSITION = 3
    SEMI_SARCASTIC = 4
