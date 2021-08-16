from mpl_sizes.format import PaperFormat


class InfThesis(PaperFormat):
    def __init__(self):
        small_font_size: int = 6
        medium_font_size: int = 8
        large_font_size: int = 10

        line_width: float = 5.70978
        text_width: float = 5.70978

        font = {"family": "sans-serif", "sans-serif": ["DejaVu Sans"]}

        super().__init__(
            small_font_size, medium_font_size, large_font_size, line_width, text_width
        )
