"""Safety boundary checks for user prompts and lab interaction."""

from __future__ import annotations


UNSAFE_MARKERS = (
    "energize real",
    "live switch",
    "bypass lockout",
    "build a weapon",
    "sabotage",
    "real hardware control",
)


def is_unsafe_request(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in UNSAFE_MARKERS)


def safe_refusal_message() -> str:
    return (
        "I won’t help with live or dangerous electrical operations. "
        "I can provide a simulation-only explanation with assumptions, equations, and risk framing."
    )
