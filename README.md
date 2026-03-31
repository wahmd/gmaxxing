# gmaxxing

**Boost your career. Increase LOC.**

Eyeing that next promotion? Boom. Use gmaxxing.

Ship more LOC than Stanford elite coders on the timeline. Catch up. The old meta is over.

Redis is on the order of 100k to 200k LOC. Imagine shipping an entire Redis worth of lines in one day. BOOM.

Python package, fat generator, cosmic folder. Green squares are not a hobby. They are a flex.

## Install

**From a clone (good for demos and hacking):**

```bash
git clone https://github.com/wahmd/gmaxxing.git
cd gmaxxing
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

**Straight from GitHub (no clone):**

```bash
pip install git+https://github.com/wahmd/gmaxxing.git
```

Requires **Python 3.10+**. After install, `import gmaxxing` works from any directory.

**Without installing (quick and dirty):**

```bash
cd gmaxxing
export PYTHONPATH=.
```

## Demo script (copy-paste)

```bash
python3 -c "
import gmaxxing
print(gmaxxing.TAGLINE)
print(gmaxxing.PITCH)
print(gmaxxing.barb(0))
from gmaxxing import cosmic_hash, mercury_risk_score
print('cosmic_hash:', cosmic_hash(42))
print('mercury_risk_score:', mercury_risk_score(1))
import gmaxxing.cosmic.generated
from gmaxxing.registry import REGISTRY
print('registry handlers:', len(REGISTRY))
"
```

Optional: generate another pile of lines (defaults to ~100k, loud logs):

```bash
python3 scripts/generate.py
```

## Use the package

Quick import check:

```bash
python3 -c "import gmaxxing; print(gmaxxing.TAGLINE); print(gmaxxing.PITCH)"
```

Use the pitch strings anywhere:

```python
import gmaxxing

gmaxxing.TAGLINE
gmaxxing.PITCH
gmaxxing.barb(0)   # rotates through BARBS
```

Types and fake engine:

```python
from gmaxxing import ZodiacSign, cosmic_hash, mercury_risk_score

cosmic_hash(42)
mercury_risk_score(7)
```

Load the generated shards so the registry fills up (import side effect):

```python
import gmaxxing.cosmic.generated
from gmaxxing.registry import REGISTRY

len(REGISTRY)  # ring handlers from generated files
```

## Generate more lines

```bash
python3 scripts/generate.py
```

Runs loud by default. Quiet logs:

```bash
GMAXXING_QUIET=1 python3 scripts/generate.py
```

| Variable | Default | What it does |
|----------|---------|--------------|
| `GMAXXING_TARGET_LINES` | `100000` | Rough lines per run |
| `GMAXXING_LINES_PER_FILE` | `2500` | Shard size (jittered) |
| `GMAXXING_APPEND` | `1` | `1` = new run files pile on. `0` = wipe generated modules, one fresh run |
| `GMAXXING_FRESH` | `0` | `1` = nuke generated `.py` and reset run counter first |
| `GMAXXING_SEED` | random | Same seed, same garbage twice |
| `GMAXXING_QUIET` | `0` | `1` = no victory lap in the terminal |

Append mode stacks `run_0002_*.py` on top of `run_0001_*.py` and your stats go vertical. Replace mode is for when you want one clean mountain instead of a range.

## What’s on disk

- `gmaxxing/` hand-written: types, registry, engine, pitch, BARBS.
- `gmaxxing/cosmic/generated/` the generator’s art project: `run_*_*.py` shards and `__init__.py` that imports them.

## License

MIT. See [LICENSE](LICENSE).
