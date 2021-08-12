import matplotlib.pyplot as plt

from mpl_sizes.format import PaperFormat
from mpl_sizes import get_format


def get_fig_ax(
    n_rows: int = 1,
    n_cols: int = 1,
    formatter: PaperFormat = None,
    aspect_ratio: str = "wide",
):

    figsize = formatter.text_width_plot(aspect_ratio=aspect_ratio)

    fig, ax = plt.subplots(n_rows, n_cols, figsize=figsize)
    return fig, ax


formatter = get_format("InfThesis")

for aspect_ratio in ["equal", "narrow", "normal", "wide"]:
    fig, ax = get_fig_ax(formatter=formatter, aspect_ratio=aspect_ratio)

    ax.set_title("ax title")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")

    plt.tight_layout()
    plt.savefig(f"figures/{aspect_ratio}.png")
