"""Engine: shove integers through a ring. Like ‘impact,’ but you can XOR it."""

from __future__ import annotations

from gmaxxing.registry import REGISTRY, ring_step


def cosmic_hash(seed: int, salt: int = 0xC05D00D) -> int:
    x = (seed ^ salt) & 0xFFFFFFFF
    if not REGISTRY:
        return x
    keys = sorted(REGISTRY.keys())
    name = keys[seed % len(keys)]
    return ring_step(name, x)


def mercury_risk_score(day: int) -> int:
    """Executives want a dashboard number. Here: deterministic nonsense. Same KPI energy."""
    return (day * 11011) & 0x7FFF
