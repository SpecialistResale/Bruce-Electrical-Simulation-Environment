"""Voice/text command parser for simulation parameter updates."""

from __future__ import annotations

import re


def parse_voice_command(command: str) -> dict[str, float | str]:
    text = command.lower().strip()
    updates: dict[str, float | str] = {"intent": "unknown"}

    patterns = {
        "current_a": r"current\s+(?:to\s+)?([\d.]+)",
        "distance_m": r"distance\s+(?:to\s+)?([\d.]+)\s*(millimeters|millimeter|mm|meters|meter|m)?",
        "frequency_hz": r"(?:frequency|hertz|hz)\s+(?:to\s+)?([\d.]+)",
        "angle_deg": r"angle\s+(?:to\s+)?([\d.]+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if not match:
            continue

        value = float(match.group(1))
        if key == "distance_m":
            unit = match.group(2) or "m"
            if unit.startswith("mm") or "milli" in unit:
                value = value / 1000.0
        updates[key] = value

    if "show me the scientist layer" in text:
        updates["intent"] = "show_scientific"
    elif "practical" in text:
        updates["intent"] = "show_practical"
    elif "deep" in text:
        updates["intent"] = "show_deep_theory"
    elif any(k in updates for k in ("current_a", "distance_m", "frequency_hz", "angle_deg")):
        updates["intent"] = "update_parameters"

    return updates
