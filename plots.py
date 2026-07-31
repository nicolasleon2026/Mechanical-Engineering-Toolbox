from matplotlib.figure import Figure


def new_figure(figsize=(5.2, 3.6)):
    fig = Figure(figsize=figsize, dpi=100)
    ax = fig.add_subplot(111)
    return fig, ax


def style_axes(ax, title, xlabel, ylabel):
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.grid(True, linestyle="--", alpha=0.5)
