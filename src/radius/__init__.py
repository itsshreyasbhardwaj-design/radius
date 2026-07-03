"""radius — universal Test Impact Analysis.

Run only the tests your change can actually break, in any language.
The core (config, git diff, selection, map store) is pure standard library;
language support is provided by thin adapters that shell out to each
ecosystem's native coverage tooling.
"""

__version__ = "0.1.0"
