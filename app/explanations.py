"""Layered explanation generator for simulation outputs."""

from __future__ import annotations


def layered_explanation(result_summary: str, equation: str, assumptions: str, deep_note: str) -> dict[str, str]:
    return {
        "Practical layer": (
            "Here’s the practical view. Watch thermal stress, insulation margin, and mechanical loading first. "
            f"{result_summary}"
        ),
        "Scientific layer": (
            f"Equation: {equation}. Assumptions: {assumptions} "
            "Values are unit-consistent and bounded to simplified lab models."
        ),
        "Deep theory layer": (
            "That result is useful, but it is not the whole story. "
            f"{deep_note}"
        ),
        "Safety boundary": (
            "Simulation-only environment. No live control, no energization procedure, no operational field instructions."
        ),
    }
