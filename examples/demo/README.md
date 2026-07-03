# radius demo

A 4-function module with one test each. Watch radius run only the test your
change can break.

```bash
# from a copy of this folder in its own git repo
cp -r examples/demo /tmp/radius-demo && cd /tmp/radius-demo
git init -q && git add -A && git commit -qm "demo"

pip install radius-tia[pytest]

radius init
radius map                 # one full run builds the map (4 tests)

# change only multiplication
sed -i '' 's/a \* b/a * b  # tweak/' src/calc.py

radius affected            # → only tests/test_calc.py::test_mul
radius test                # runs 1 of 4 tests, 75% skipped
radius why tests/test_calc.py::test_add   # → SKIPPED, add() wasn't touched
```

`radius map` uses `source_paths = ["src"]` and `test_paths = ["tests"]`, which
match this layout out of the box.
