#!/usr/bin/env python3
"""
Emit cosmic shards — each run adds ~target LOC of randomized astrology-shaped noise.
"""

from __future__ import annotations

import os
import random
import secrets
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from gmaxxing.pitch import barb  # noqa: E402

GENERATED = ROOT / "gmaxxing" / "cosmic" / "generated"
RUN_COUNTER = GENERATED / ".gmaxxing_run_id"

_LOG_PREFIXES = (
    "[gmaxxing]",
    "[ELITE]",
    "[AGI]",
    "[10x]",
    "[SIGMA]",
    "[LOOM]",
    "[VELOCITY]",
    ">>",
    "[MAIN_CHARACTER]",
    "[THOUGHT_LEADERSHIP]",
)

_BRO_LOGS = (
    "AGI is here bruh",
    "shipping at light speed",
    "main character energy (unlocked)",
    "thought leadership: ON",
    "your VC is typing…",
    "velocity isn't a crime",
    "37k LOC before the standup (easy)",
    "synergy unlocked",
    "paradigm shift (real)",
    "elite mode: engaged",
    "stacking metrics like pancakes",
    "diff so big git got emotional",
    "agentic excellence: yes",
    "boom: another module just dropped",
    "promotion packet: loading…",
    "mercury retrograde can't stop this grind",
    "10x engineer (self-certified)",
    "we're so back",
    "it's giving enterprise",
    "sigma output",
    "brainrot but productive",
    "core memory: this line count",
    "WAGMI",
    "LFG",
    "ship it / ship it / ship it",
    "board is gonna love these numbers",
    "innovation happened (probably)",
    "automation ate my homework (good)",
    "this is what winning looks like (txt file edition)",
    "YOLO compile pass",
    "if you're not shipping are you even real",
    "my graph is a skyline",
    "accidentally built a platform",
    "zero to hero (line count only)",
    "quiet quitting is for people who read diffs",
    "I don't read docs I generate them",
    "scale first ask questions never",
    "this shard is basically a Series A",
    "alignment: achieved (cosmic)",
    "OKRs trembling rn",
    "the repo fears me",
    "git blame the universe",
    "another day another dimension of output",
    "I'm not spamming I'm diversifying",
    "robots said nice things (I assume)",
    "accelerationism but for tabs",
    "my IDE is a casino and I'm up",
    "stack rank this (you can't)",
    "pivot: more lines",
    "disrupting whitespace",
    "hypergrowth (bytes/sec)",
    "unhinged throughput",
    "certified hood classic (python file)",
    "this is fine (engineering)",
    "who needs sleep when you have LOC",
    "I don't push code I push narratives",
    "synergy with the void",
    "enterprise-grade vibes",
    "another W for the pipeline",
)


def _quiet() -> bool:
    return os.environ.get("GMAXXING_QUIET", "").strip() in ("1", "true", "True", "yes", "YES")


def _joke_line(rng: random.Random, indent: str = "    ") -> str:
    """One readable line; rarely adds a bracket prefix so it doesn't get noisy."""
    phrase = rng.choice(_BRO_LOGS)
    if rng.random() < 0.12:
        return f"{indent}{rng.choice(_LOG_PREFIXES)} {phrase}"
    return f"{indent}{phrase}"


def _bro_shard(rng: random.Random, run_id: int, shard: int, phys: int) -> None:
    if _quiet():
        return
    print(f"  run {run_id:04d} · shard {shard + 1:02d} · +{phys} LOC", flush=True)
    print(_joke_line(rng, "      "), flush=True)
    print(flush=True)


def _bro_banner(rng: random.Random, run_id: int, target: int, append: bool) -> None:
    if _quiet():
        return
    mode = "stacking more" if append else "full send"
    print(flush=True)
    print("  gmaxxing", flush=True)
    print(f"  run {run_id:04d} · ~{target} lines · {mode}", flush=True)
    print(flush=True)
    print(f"  {rng.choice(_BRO_LOGS)}", flush=True)
    print(f"  {rng.choice(_BRO_LOGS)}", flush=True)
    print(flush=True)


def _bro_finale(
    rng: random.Random,
    run_id: int,
    shards_written: int,
    total_lines: int,
    target: int,
    seed: int,
) -> None:
    if _quiet():
        print(
            f"Run {run_id}: {shards_written} shards, {total_lines} lines (target ~{target}), seed={seed}.",
            flush=True,
        )
        return
    print(flush=True)
    print(f"  done · {total_lines} LOC · {shards_written} shards · run {run_id:04d}", flush=True)
    print(flush=True)
    print(_joke_line(rng, "  "), flush=True)
    print(flush=True)
    print(f"  seed={seed}", flush=True)


def _bro_spark(label: str) -> None:
    if _quiet():
        return
    print(f"  {label}", flush=True)
    print(flush=True)

SIGNS = (
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
    "aquarius",
    "pisces",
)
PLANETS = (
    "mercury",
    "venus",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "pluto",
    "chiron",
    "lilith",
)
VERBS = (
    "squares",
    "trines",
    "opposes",
    "conjoins",
    "semi-sextiles",
    "imagines",
    "handwaves",
)

_FLUFF_TEMPLATES = (
    "{b} {v} {c}; {a} blames the intern. Token {seed}.",
    "Transit says {b} is {v} {c}. Your standup says you are 'almost done.' Token {seed}.",
    "{a} energy + {b} {v} {c} = another green square nobody asked for. #{seed}",
    "If {b} {v} {c} were a PR, it would need 6 reviewers and 0 tests. Ref {seed}.",
    "{c} and {a} in the same sprint? That is not alignment—that is a merge conflict. {seed}",
    "Career tip: when {b} {v} {c}, increase LOC before anyone asks what it does. id={seed}",
    "Mercury did not retrograde; your estimates did. Meanwhile {b} {v} {c}. Token {seed}.",
    "Your manager wants impact. You shipped {b} {v} {c} in comments. Line {seed}.",
    "{a} thinks {c} is the problem. The problem is measuring souls in kilobytes. {seed}",
    "Deep domain modeling: {b} {v} {c} like it pays rent. (It pays dopamine.) {seed}",
    "Staff archetype detected: cites {b}, ignores {c}, ships {a} flavored tech debt. {seed}",
    "This function is more honest than a roadmap: {b} {v} {c}, still no users. {seed}",
    "If vibes were tests, {b} {v} {c} would still fail CI. Ref {seed}.",
    "Agentic excellence: {b} {v} {c} faster than you can read a diff. #{seed}",
    "Promotion narrative: {a} courage, {c} wisdom, {b} {v} {c} for the screenshot. {seed}",
)


def _doc_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', "'")


def _fluff_sentence(seed: int, rng: random.Random) -> str:
    a = rng.choice(SIGNS)
    b = rng.choice(PLANETS)
    c = rng.choice(SIGNS)
    v = rng.choice(VERBS)
    tmpl = rng.choice(_FLUFF_TEMPLATES)
    salt = rng.randint(0, 999_999)
    mixed = seed ^ salt
    return _doc_escape(tmpl.format(a=a, b=b, c=c, v=v, seed=mixed))


def _emit_constant_line(global_idx: int, shard: int, run_id: int, rng: random.Random) -> str:
    mul = rng.randint(1, 99_983)
    mul2 = rng.randint(1, 99_983)
    val = ((global_idx * mul) ^ (shard * mul2) ^ (run_id * 1337)) & 0xFFFFFFFF
    return f"_SIGIL_r{run_id:04d}_{shard:04d}_{global_idx:07d} = {val}\n"


def _emit_function_block(
    global_idx: int,
    shard: int,
    run_id: int,
    rng: random.Random,
) -> str:
    s = _fluff_sentence(global_idx, rng)
    m = rng.randint(2, 17)
    body = textwrap.dedent(
        f'''
        def _transit_fluff_r{run_id:04d}_{shard:04d}_{global_idx:07d}(x: int) -> int:
            """{s}"""
            z = (x * {m}) ^ {rng.randint(0, 0xFFFF)} ^ {global_idx}
            return z & 0xFFFF

        '''
    ).lstrip("\n")
    return body


def _wipe_generated_py() -> None:
    for p in GENERATED.glob("*.py"):
        p.unlink()


def _read_next_run_id(append: bool) -> int:
    if not append:
        _wipe_generated_py()
        run_id = 1
        RUN_COUNTER.write_text("1\n")
        return run_id
    if not RUN_COUNTER.exists():
        n = 1
    else:
        try:
            n = int(RUN_COUNTER.read_text().strip() or "0") + 1
        except ValueError:
            n = 1
    RUN_COUNTER.write_text(f"{n}\n")
    return n


def _module_basename(run_id: int, shard_id: int) -> str:
    return f"run_{run_id:04d}_{shard_id:04d}"


def write_shard(
    shard_id: int,
    total_lines_in_file: int,
    global_start: int,
    rng: random.Random,
    run_id: int,
    seed: int,
) -> tuple[int, int]:
    """Write one shard file. Returns (semantic units emitted, physical line count)."""
    mod = _module_basename(run_id, shard_id)
    path = GENERATED / f"{mod}.py"
    g = global_start
    shard_quip = _doc_escape(barb(rng.randint(0, 10_000)))
    ring_quip = _doc_escape(barb(rng.randint(0, 10_000)))
    xor_const = rng.randint(1, 999_983)
    header = f'''\
# gmaxxing run {run_id} shard {shard_id} — randomized astrology-shaped LOC.
# {shard_quip}
# rng_seed={seed}

from __future__ import annotations

from gmaxxing.registry import register
from gmaxxing.types import AspectKind, House, MoonPhase, TransitPhase, ZodiacSign

'''
    ring_fn = f'''\
def _ring_r{run_id:04d}_s{shard_id:04d}(x: int) -> int:
    """Ring run {run_id} shard {shard_id} — {ring_quip}"""
    return (x ^ {shard_id * xor_const}) & 0xFFFFFF


register("ring_r{run_id:04d}_s{shard_id:04d}", _ring_r{run_id:04d}_s{shard_id:04d})
'''
    header_n = header.count("\n")
    ring_n = ring_fn.count("\n")
    body_limit = max(0, total_lines_in_file - header_n - ring_n)

    body_lines = 0
    with path.open("w", encoding="utf-8") as f:
        f.write(header)
        while body_lines < body_limit:
            if g % 9 == 0:
                block = _emit_function_block(g, shard_id, run_id, rng)
                bl = block.count("\n")
                if body_lines + bl > body_limit:
                    while body_lines < body_limit:
                        f.write(_emit_constant_line(g, shard_id, run_id, rng))
                        body_lines += 1
                        g += 1
                    break
                f.write(block)
                body_lines += bl
            else:
                f.write(_emit_constant_line(g, shard_id, run_id, rng))
                body_lines += 1
            g += 1
        f.write(ring_fn)

    physical_lines = header_n + body_lines + ring_n
    return (g - global_start, physical_lines)


def _collect_imports() -> str:
    paths = []
    paths.extend(sorted(GENERATED.glob("chunk_*.py")))
    paths.extend(sorted(GENERATED.glob("run_*.py")))
    lines = ["# gmaxxing — load all shards (legacy chunk_* + run_*), maximize footprint."]
    for p in paths:
        if p.name == "__init__.py":
            continue
        mod = p.stem
        if mod.startswith("run_") or mod.startswith("chunk_"):
            lines.append(f"from . import {mod}")
    return "\n".join(lines) + "\n"


def main() -> None:
    target = int(os.environ.get("GMAXXING_TARGET_LINES", "100000"))
    per_file = max(200, int(os.environ.get("GMAXXING_LINES_PER_FILE", "2500")))
    append = os.environ.get("GMAXXING_APPEND", "1").strip() not in ("0", "false", "False", "no", "NO")
    fresh = os.environ.get("GMAXXING_FRESH", "0").strip() in ("1", "true", "True", "yes", "YES")
    if fresh:
        _wipe_generated_py()
        RUN_COUNTER.write_text("0\n")

    seed_str = os.environ.get("GMAXXING_SEED", "").strip()
    if seed_str:
        seed = int(seed_str)
    else:
        seed = secrets.randbits(63)

    rng = random.Random(seed)

    run_id = _read_next_run_id(append=append)

    GENERATED.mkdir(parents=True, exist_ok=True)

    _bro_banner(rng, run_id, target, append)

    effective_per = max(200, per_file)
    lo = max(200, effective_per - 400)
    hi = effective_per + 400

    global_idx = 0
    total_lines = 0
    shards_written = 0
    s = 0
    while total_lines < target and s < 500:
        remaining = target - total_lines
        if remaining <= 0:
            break
        budget = min(remaining, rng.randint(lo, hi))
        _units, phys = write_shard(s, budget, global_idx, rng, run_id, seed)
        global_idx += _units
        total_lines += phys
        shards_written += 1
        _bro_shard(rng, run_id, s, phys)
        s += 1

    _bro_spark("stitching imports together")
    (GENERATED / "__init__.py").write_text(_collect_imports(), encoding="utf-8")

    cosmic_init = '''"""Cosmic package — generated modules that scale your story."""

from . import generated  # noqa: F401

__all__ = ["generated"]
'''
    cosmic_dir = ROOT / "gmaxxing" / "cosmic"
    cosmic_dir.mkdir(parents=True, exist_ok=True)
    (cosmic_dir / "__init__.py").write_text(cosmic_init, encoding="utf-8")

    _bro_spark("cosmic package __init__")
    _bro_finale(rng, run_id, shards_written, total_lines, target, seed)


if __name__ == "__main__":
    main()
