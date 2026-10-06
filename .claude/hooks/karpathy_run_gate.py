#!/usr/bin/env python3
"""Stop hook: don't let a Karpathy-flavoured turn end on unrun code.

Fires only when the turn actually used the `karpathy` subagent or the
`karpathy-teach` skill. If that turn wrote or edited a code file and then never
ran anything afterwards, the stop is blocked and sent back with the reminder.

Every other turn, and every other project, is left completely alone.

Design note: this hook fails OPEN. Any unexpected condition — unreadable
transcript, malformed JSON, missing field, unknown schema — exits 0 and allows
the stop. A gate that traps you because of its own bug is worse than no gate.
"""

from __future__ import annotations

import json
import sys

MESSAGE = "Karpathy rule, run it before you say it works."

# Tool names that launch a subagent, and the field carrying its type.
AGENT_TOOLS = {"Agent", "Task"}
# Tool name that invokes a skill, and the fields that may carry its name.
SKILL_TOOLS = {"Skill", "SlashCommand"}
SKILL_FIELDS = ("skill", "command", "name", "skill_name")

TARGET_AGENT = "karpathy"
TARGET_SKILL = "karpathy-teach"

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit", "str_replace_editor"}
RUN_TOOLS = {"Bash", "BashOutput", "Shell", "Execute"}

# "A code file" — things that are executed or compiled. Prose, data and config
# are deliberately excluded: editing a README is not a claim that code works.
CODE_SUFFIXES = (
    ".py", ".pyi", ".ipynb", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx",
    ".go", ".rs", ".java", ".kt", ".scala", ".rb", ".php", ".pl", ".lua",
    ".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".swift", ".m", ".mm",
    ".sh", ".bash", ".zsh", ".fish", ".ps1", ".sql", ".r", ".jl", ".ex", ".exs",
)


def blocks(entry: dict) -> list:
    message = entry.get("message")
    if not isinstance(message, dict):
        return []
    content = message.get("content")
    return content if isinstance(content, list) else []


def is_human_turn_start(entry: dict) -> bool:
    """A real prompt, as opposed to a tool result or an injected reminder."""
    if entry.get("type") != "user" or entry.get("isMeta") or entry.get("isSidechain"):
        return False
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    if isinstance(content, list):
        kinds = {b.get("type") for b in content if isinstance(b, dict)}
        return bool(kinds - {"tool_result"})
    return False


def mentions_target(value, target: str) -> bool:
    return isinstance(value, str) and target in value.strip().lower()


def main() -> int:
    raw = sys.stdin.read()
    payload = json.loads(raw) if raw.strip() else {}

    # Claude re-runs Stop hooks after a block; without this the gate loops.
    if payload.get("stop_hook_active"):
        return 0

    path = payload.get("transcript_path")
    if not path:
        return 0

    entries = []
    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except ValueError:
                continue

    # Scope to the current turn: everything after the last real human prompt.
    start = 0
    for i in range(len(entries) - 1, -1, -1):
        if is_human_turn_start(entries[i]):
            start = i
            break

    # Secondary signal: the Stop payload lists live/recent subagents by type.
    # Cheap to check and independent of transcript schema, which Claude Code
    # documents as internal and subject to change between versions.
    karpathy_used = any(
        isinstance(task, dict) and mentions_target(task.get("agent_type"), TARGET_AGENT)
        for task in (payload.get("background_tasks") or [])
    )
    last_write = last_run = -1

    for position, entry in enumerate(entries[start:], start=start):
        if entry.get("type") != "assistant":
            continue
        for block in blocks(entry):
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            name = block.get("name") or ""
            data = block.get("input")
            data = data if isinstance(data, dict) else {}

            if name in AGENT_TOOLS and mentions_target(
                data.get("subagent_type"), TARGET_AGENT
            ):
                karpathy_used = True
            elif name in SKILL_TOOLS and any(
                mentions_target(data.get(f), TARGET_SKILL) for f in SKILL_FIELDS
            ):
                karpathy_used = True

            if name in WRITE_TOOLS:
                target = data.get("file_path") or data.get("notebook_path") or ""
                if isinstance(target, str) and target.lower().endswith(CODE_SUFFIXES):
                    last_write = position
            elif name in RUN_TOOLS:
                last_run = position

    if karpathy_used and last_write >= 0 and last_run < last_write:
        # Exit 2 with the reason on stderr is the documented way a Stop hook
        # blocks; the message is fed back to Claude as the instruction to
        # continue. Nothing goes to stdout — stray stdout breaks JSON parsing.
        sys.stderr.write(MESSAGE + "\n")
        return 2

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except BaseException:
        # Fail open — never trap the user because this hook broke.
        raise SystemExit(0)
