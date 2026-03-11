"""Reusable plotting helpers for Bruce Electrical Simulator."""

from __future__ import annotations

import matplotlib.pyplot as plt


def line_plot(x, y, title: str, x_label: str, y_label: str):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(x, y, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig
