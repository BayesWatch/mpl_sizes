from mpl_sizes.format import PaperFormat


class ICLR(PaperFormat):
    def __init__(self):
        small_font_size: int = 8
        medium_font_size: int = 10
        large_font_size: int = 12

        line_width: float = 5.50107
        text_width: float = 5.50107

        super().__init__(
            small_font_size, medium_font_size, large_font_size, line_width, text_width
        )
