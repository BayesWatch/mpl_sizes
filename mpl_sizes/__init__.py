from mpl_sizes.format import PaperFormat
from .paper_formats import *


def get_format(format: str) -> PaperFormat:
    if format == "ICLR":
        return ICLR()

    elif format == "ICML":
        return ICML()

    elif format == "NeurIPS":
        return NeurIPS()

    elif format == "InfThesis":
        return InfThesis()

    else:
        raise ValueError("Invalid format specified")
