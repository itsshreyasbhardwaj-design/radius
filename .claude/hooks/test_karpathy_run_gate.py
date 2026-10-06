#!/usr/bin/env python3
"""Tests for the karpathy run gate.

The gate exists to enforce rule 6 — run it before you say it works — so it would
be absurd to ship it unrun. Every case below is executed against the real hook
as a subprocess, exactly as Claude Code invokes it.

    python3 -I .claude/hooks/test_karpathy_run_gate.py

Exit 0 = all pass.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HOOK = os.path.join(HERE, "karpathy_run_gate.py")
MESSAGE = "Karpathy rule, run it before you say it works."

BLOCK, ALLOW = 2, 0


def user(text="go"):
    return {"type": "user", "message": {"role": "user", "content": text}}


def tool_result():
    return {"type": "user", "message": {"role": "user", "content": [
        {"type": "tool_result", "content": "ok"}]}}


def assistant(*tools):
    blocks = [{"type": "tool_use", "name": n, "input": i} for n, i in tools]
    return {"type": "assistant", "message": {"role": "assistant", "content": blocks}}


AGENT = ("Agent", {"subagent_type": "karpathy", "prompt": "build it"})
SKILL = ("Skill", {"skill": "karpathy-teach", "args": ""})
OTHER_AGENT = ("Agent", {"subagent_type": "general-purpose", "prompt": "x"})
WRITE_PY = ("Write", {"file_path": "/repo/thing.py", "content": "x=1"})
EDIT_PY = ("Edit", {"file_path": "/repo/thing.py", "old_string": "a", "new_string": "b"})
WRITE_MD = ("Write", {"file_path": "/repo/NOTES.md", "content": "hi"})
WRITE_NB = ("NotebookEdit", {"notebook_path": "/repo/x.ipynb", "new_source": "1"})
RUN = ("Bash", {"command": "python3 thing.py", "description": "run"})


def run_hook(entries, *, stop_hook_active=False, extra=None, raw=None):
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as fh:
        if raw is not None:
            fh.write(raw)
        else:
            for entry in entries:
                fh.write(json.dumps(entry) + "\n")
        path = fh.name
    payload = {"hook_event_name": "Stop", "transcript_path": path,
               "stop_hook_active": stop_hook_active, "session_id": "t"}
    if extra:
        payload.update(extra)
    try:
        proc = subprocess.run([sys.executable, "-I", HOOK], input=json.dumps(payload),
                              capture_output=True, text=True, timeout=30)
        return proc
    finally:
        os.unlink(path)


CASES = [
    ("karpathy agent wrote code and never ran it -> BLOCK",
     [user(), assistant(AGENT), assistant(WRITE_PY)], BLOCK, {}),

    ("karpathy agent wrote code then ran it -> allow",
     [user(), assistant(AGENT), assistant(WRITE_PY), assistant(RUN)], ALLOW, {}),

    ("ran BEFORE the last write -> BLOCK (the run does not cover that edit)",
     [user(), assistant(AGENT), assistant(RUN), assistant(EDIT_PY)], BLOCK, {}),

    ("karpathy-teach skill wrote code and never ran it -> BLOCK",
     [user(), assistant(SKILL), assistant(WRITE_PY)], BLOCK, {}),

    ("no karpathy agent or skill -> allow, every other session is left alone",
     [user(), assistant(OTHER_AGENT), assistant(WRITE_PY)], ALLOW, {}),

    ("karpathy agent but only markdown touched -> allow, prose is not code",
     [user(), assistant(AGENT), assistant(WRITE_MD)], ALLOW, {}),

    ("notebook counts as code -> BLOCK",
     [user(), assistant(AGENT), assistant(WRITE_NB)], BLOCK, {}),

    ("karpathy agent but nothing written -> allow",
     [user(), assistant(AGENT), assistant(RUN)], ALLOW, {}),

    ("offence was in a PREVIOUS turn, this turn is clean -> allow",
     [user(), assistant(AGENT), assistant(WRITE_PY), user("next task"),
      assistant(RUN)], ALLOW, {}),

    ("tool_result lines must not be mistaken for a new turn -> BLOCK",
     [user(), assistant(AGENT), tool_result(), assistant(WRITE_PY), tool_result()],
     BLOCK, {}),

    ("stop_hook_active -> allow, loop prevention wins over everything",
     [user(), assistant(AGENT), assistant(WRITE_PY)], ALLOW,
     {"stop_hook_active": True}),

    ("subagent seen only via background_tasks -> BLOCK",
     [user(), assistant(WRITE_PY)], BLOCK,
     {"extra": {"background_tasks": [{"type": "subagent", "agent_type": "karpathy"}]}}),

    ("Task tool name also recognised -> BLOCK",
     [user(), assistant(("Task", {"subagent_type": "karpathy"})), assistant(WRITE_PY)],
     BLOCK, {}),
]


def main() -> int:
    failures = []

    for name, entries, expected, opts in CASES:
        proc = run_hook(entries, stop_hook_active=opts.get("stop_hook_active", False),
                        extra=opts.get("extra"))
        ok = proc.returncode == expected
        if expected == BLOCK:
            ok = ok and MESSAGE in proc.stderr
        if proc.stdout.strip():
            ok = False  # stray stdout breaks the hook contract
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            failures.append((name, expected, proc.returncode, proc.stdout, proc.stderr))

    # Fail-open cases: a broken hook must never trap the user.
    for name, kwargs in [
        ("malformed transcript -> allow (fails open)", {"raw": "{not json\nalso not\n"}),
        ("empty transcript -> allow", {"raw": ""}),
    ]:
        proc = run_hook(None, **kwargs)
        ok = proc.returncode == ALLOW
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            failures.append((name, ALLOW, proc.returncode, proc.stdout, proc.stderr))

    proc = subprocess.run([sys.executable, "-I", HOOK], input="",
                          capture_output=True, text=True, timeout=30)
    ok = proc.returncode == ALLOW
    print(f"{'PASS' if ok else 'FAIL'}  empty stdin -> allow")
    if not ok:
        failures.append(("empty stdin", ALLOW, proc.returncode, proc.stdout, proc.stderr))

    proc = run_hook([user(), assistant(AGENT), assistant(WRITE_PY)],
                    extra={"transcript_path": None})
    ok = proc.returncode == ALLOW
    print(f"{'PASS' if ok else 'FAIL'}  missing transcript_path -> allow")
    if not ok:
        failures.append(("missing transcript_path", ALLOW, proc.returncode,
                         proc.stdout, proc.stderr))

    print()
    if failures:
        print(f"{len(failures)} FAILED")
        for name, want, got, out, err in failures:
            print(f"  - {name}: expected exit {want}, got {got}")
            if out.strip():
                print(f"      stdout: {out.strip()[:200]}")
            if err.strip():
                print(f"      stderr: {err.strip()[:200]}")
        return 1

    print("all passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
