from mpl_sizes.format import PaperFormat


class ICML(PaperFormat):
    def __init__(self):
        small_font_size: int = 8
        medium_font_size: int = 8
        large_font_size: int = 8

        line_width: float = 3.25063
        text_width: float = 6.75133

        font = {"family": "serif", "serif": ["Times"]}

        super().__init__(
            small_font_size,
            medium_font_size,
            large_font_size,
            line_width,
            text_width,
            font,
        )
