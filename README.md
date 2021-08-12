# mpl_sizes

A lightweight tool for setting `figsize` and font sizes in `matplotlib`, with support for:

- ICLR
- ICML
- NeurIPS
- Informatics thesis 

## Installation
```bash
git clone git@github.com:BayesWatch/matplotlib_size_sheets.git
cd matplotlib_size_sheets 
python setup.py install
```

## Usage

In your plotting script: 

```python
from mpl_sizes import get_format

formatter = get_format("InfThesis") # options: ICLR, ICML, NeurIPS, InfThesis
```

Formatters have two methods: 
- `text_width_plot` - for full pagewidth plots (e.g. in double column, this would be a full width plot)
- `line_width_plot` - for plots the width of the lines of text

and font size will automatically be set correctly. 

A full example is given in `example.py`. 

