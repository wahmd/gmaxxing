# gmaxxing

**Boost your career. Increase LOC.**

Eyeing that next promotion? Boom—use gmaxxing. This repo is a serious-looking Python package plus a generator that adds **massive, production-shaped volume** fast—so your stats tell a story (accuracy sold separately).

The **cosmic layer** (zodiac-shaped types, transits, “engines”) reads like deep domain work. Import `gmaxxing.cosmic.generated` when you want the full registry wired up.

Savage one-liners live in code as `gmaxxing.BARBS` and `gmaxxing.barb(n)`.

## What’s in here

- `scripts/generate.py` — expands the codebase to your target LOC without typing it by hand; it **prints live lines** while it runs (mute with `GMAXXING_QUIET=1`).
- `gmaxxing/` — types, registry, engine, **pitch** + **barbs**; `gmaxxing/cosmic/generated/` is sharded output.

Each run emits **~100,000 lines** of randomized astrology-shaped noise (constants, docstrings, ring handlers), split across shards with **jittered** file sizes. **Every run uses a new RNG seed** unless you set `GMAXXING_SEED`, so content and numbers change each time.

| Mode | Behavior |
|------|----------|
| **Append** (default) | Adds a **new run** (`run_0001_*.py`, `run_0002_*.py`, …). Total repo LOC **grows** by ~100k per execution. |
| **Replace** | `GMAXXING_APPEND=0` — deletes all generated `*.py` in `cosmic/generated/`, then writes **one** fresh run (~100k lines). |
| **Fresh counter** | `GMAXXING_FRESH=1` — wipe generated `.py` files and reset the run counter to 0 before the next step (use with append or replace as needed). |

## Generate volume

```bash
python3 scripts/generate.py
```

| Variable | Default | Meaning |
|----------|---------|---------|
| `GMAXXING_TARGET_LINES` | `100000` | Target lines **per run** (approximate; shards are randomized) |
| `GMAXXING_LINES_PER_FILE` | `2500` | Base size per shard (± jitter) |
| `GMAXXING_APPEND` | `1` | `1` = append a new run; `0` = replace all generated modules with one run |
| `GMAXXING_FRESH` | `0` | `1` = wipe generated `*.py` + reset run counter before applying append/replace |
| `GMAXXING_SEED` | *(random)* | Set for reproducible output on the next run |
| `GMAXXING_QUIET` | `0` | `1` = minimal stdout (no bro-energy log lines) |

## License

MIT — see [LICENSE](LICENSE).
