"""Product voice — career acceleration through strategic LOC expansion."""

TAGLINE = "Boost your career. Increase LOC."
PITCH = "Eyeing that next promotion? Boom—use gmaxxing."
SUBHEAD = "Ship velocity. Stack metrics. Close the PR. Let the chart worry about Mercury."
MISSION = (
    "Agentic engineering isn’t about quality hours—it’s about quality lines. "
    "gmaxxing multiplies your footprint so your graph looks like you’re main-charactering the codebase."
)

# One-liners aimed at LOC-as-a-metric culture (not at individuals).
BARBS = (
    "They don’t measure impact—they measure who can paste the fastest.",
    "37K LOC / day is not a flex; it’s a cry for help with better metrics.",
    "Your agent didn’t ship a feature. It shipped a mortgage payment’s worth of debt.",
    "If your chart is green and your users are confused, you’re not winning—you’re trending.",
    "Main character energy: opening a PR that needs a map, a lawyer, and a therapist.",
    "‘Still speeding up’ — the repo, the burnout, and the line count. Correlated, not causal.",
    "Senior IC: deletes code. Influencer IC: deletes sleep.",
    "We put astrology in the stack so at least one layer tells the truth: it’s made up.",
    "Your diff is so big GitHub thinks it’s a denial-of-service attack.",
    "They call it agentic engineering; historians will call it ‘the JPEG era of software.’",
    "Promotion packet tip: attach a screenshot of `wc -l`. HR loves science.",
    "You don’t need a linter—you need a conscience. We ship neither.",
    "If productivity were measured in clarity, this industry would be underwater.",
    "The stars aren’t aligned; your incentives are. Same thing, worse ephemeris.",
    "We automated coding. Next up: automating the apology post.",
    "Your ‘insane week’ is someone else’s on-call incident. Thoughts and prayers.",
    "Stack ranking engineers by LOC is like ranking chefs by how loud they chop.",
    "This module does nothing useful—which makes it honest compared to the roadmap.",
)


def barb(index: int) -> str:
    """Return a barb; cycles so you always have a take."""
    if not BARBS:
        return ""
    return BARBS[index % len(BARBS)]
