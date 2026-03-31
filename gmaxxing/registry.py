"""Registry: every shard registers—like OKRs, but you can grep them."""

from __future__ import annotations

from typing import Any, Callable, Dict

REGISTRY: Dict[str, Callable[..., Any]] = {}


def register(name: str, fn: Callable[..., Any]) -> None:
    REGISTRY[name] = fn


def ring_step(name: str, x: int) -> int:
    """Pass the buck to the next handler. Management consultant simulator."""
    keys = sorted(REGISTRY.keys())
    if not keys:
        return x
    try:
        idx = keys.index(name)
    except ValueError:
        idx = 0
    nxt = keys[(idx + 1) % len(keys)]
    return int(REGISTRY[nxt](x))
