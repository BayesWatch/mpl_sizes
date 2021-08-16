import matplotlib.pyplot as plt

from mpl_sizes import get_format
from typing import Tuple


def get_fig_ax(
    n_rows: int = 1,
    n_cols: int = 1,
    figsize: Tuple[float, float] = None,
):

    fig, ax = plt.subplots(n_rows, n_cols, figsize=figsize)
    return fig, ax


conference = "ICML"  # options:  "ICLR", "NeurIPS", "InfThesis"
formatter = get_format(conference)


for (aspect_ratio, func) in [
    ("wide", formatter.text_width_plot),
    ("normal", formatter.line_width_plot),
]:

    fig, ax = get_fig_ax(figsize=func(aspect_ratio))

    ax.set_xlabel("x label")
    ax.set_ylabel("y label")

    plt.tight_layout()
    plt.savefig(f"figures/{conference}_{aspect_ratio}.png")
