# matplotlib_size_sheets
Cheat sheets for figure sizes for various conference formats

## Setting font sizes

You can either set these in your own stylesheet and use that, or you can write this at the start of all your plotting code:

```
import matplotlib.pyplot as plt

SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 14

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
```

Courtesy of [this stackoverflow post](https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot).
