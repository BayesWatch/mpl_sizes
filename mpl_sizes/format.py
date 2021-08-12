from typing import Dict, NewType, Tuple
import matplotlib.pyplot as plt

Inches = NewType("Inches", float)

"""aspect ratios are (width, height) tuples

For example, if text width is 4 and I want a (4, 3) plot
then I will want the height of the plot to be 3
"""
aspect_ratios: Dict[str, float] = {
    "wide": 21 / 9,
    "normal": 16 / 9,
    "narrow": 4 / 3,
    "equal": 1 / 1,
}


class PaperFormat:
    def __init__(
        self,
        small_font_size: int,
        medium_font_size: int,
        large_font_size: int,
        line_width: float,
        text_width: float,
    ):
        self.small_font_size = small_font_size
        self.medium_font_size = medium_font_size
        self.large_font_size = large_font_size
        self.set_font_sizes()

        self.line_width = line_width
        self.text_width = text_width

    def text_width_plot(self, aspect_ratio: str = "wide") -> Tuple[Inches, Inches]:
        ratio = aspect_ratios[aspect_ratio]

        return (self.text_width, self.text_width / ratio)

    def line_width_plot(self, aspect_ratio: str = "wide") -> Tuple[Inches, Inches]:
        ratio = aspect_ratios[aspect_ratio]

        return (self.line_width, self.line_width / ratio)

    def set_font_sizes(self) -> None:
        """
        Courtesy of:
        https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
        """

        plt.rc("font", size=self.small_font_size)  # controls default text sizes
        plt.rc("axes", titlesize=self.medium_font_size)  # fontsize of the axes title
        plt.rc(
            "axes", labelsize=self.medium_font_size
        )  # fontsize of the x and y labels
        plt.rc("xtick", labelsize=self.small_font_size)  # fontsize of the tick labels
        plt.rc("ytick", labelsize=self.small_font_size)  # fontsize of the tick labels
        plt.rc("legend", fontsize=self.small_font_size)  # legend fontsize
        plt.rc("legend", title_fontsize=self.medium_font_size)  # legend fontsize
        plt.rc("figure", titlesize=self.large_font_size)  # fontsize of the figure title
