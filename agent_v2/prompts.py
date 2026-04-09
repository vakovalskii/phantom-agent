from __future__ import annotations

from pathlib import Path

_PROMPT_FILE = Path(__file__).parent / "system_prompt.md"


def get_system_prompt() -> str:
    """Read system prompt from file — hot-reloadable."""
    return _PROMPT_FILE.read_text(encoding="utf-8").strip()


# Keep SYSTEM_PROMPT as a property-like for backwards compat
# But anyone importing it gets the current value at import time
# Use get_system_prompt() for dynamic reads
SYSTEM_PROMPT = get_system_prompt()


def _build_skills_menu(recommended_skill_id: str | None = None) -> str:
    """Build compact skills list with recommended hint."""
    from .skills.registry import SKILL_REGISTRY
    lines = ["<AVAILABLE_SKILLS>"]
    for sid, s in SKILL_REGISTRY.items():
        marker = " ← RECOMMENDED" if sid == recommended_skill_id else ""
        lines.append(f"- {sid}: {s.description}{marker}")
    lines.append("")
    if recommended_skill_id:
        lines.append(f"Classifier suggests: {recommended_skill_id}")
        lines.append(f"Load full instructions: get_skill_instructions(\"{recommended_skill_id}\")")
    else:
        lines.append("Use list_skills and get_skill_instructions to load workflow details.")
    lines.append("</AVAILABLE_SKILLS>")
    return "\n".join(lines)


def build_task_prompt(task_text: str, skill_id: str | None = None) -> str:
    skills_menu = _build_skills_menu(skill_id)

    return f"""<TASK>
{task_text}
</TASK>

{skills_menu}

<GOAL>
Solve this task. First call get_skill_instructions to load the recommended skill workflow, then orient, execute, verify, complete.
REMINDER: Your LAST action MUST be calling submit_answer tool. Never end with text.
</GOAL>"""
