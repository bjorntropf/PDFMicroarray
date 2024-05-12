"""
This module provides a class for creating microarray visualizations of
dataframes, representing occurrences of specific words in scientific literature
as processed and analyzed by the PDFMicroarray class.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class PlotMicroarray:
    """
    A class designed to generate microarray visualizations of pandas
    dataframes, displaying the results from text analysis of PDF documents.
    """

    @classmethod
    def plot(
        cls,
        data_path,
        image_path=None,
        threshold=90,
        empty=False,
        width=60,
        height=30,
    ):
        """
        Plots a microarray of the provided dataframe using a predefined color
        palette.

        Args:
            data_path (str): Path to the CSV file containing data to plot.
            image_path (str, optional): If provided, the plot will be saved
            to this path. Otherwise, the plot will be shown directly.
            Defaults to None.
            threshold (int): Minimum Levenshtein distance score (0-100) to
            consider a match. Defaults to 90.
            empty (bool): If True, shows rows with no values. Defaults to
            False.
            width (int): Width of the figure in inches. Defaults to 60.
            height (int): Height of the figure in inches. Defaults to 30.
        """

        df = pd.read_csv(data_path, index_col=0, dtype={0: str})
        df = (df >= threshold).astype(int)

        if not empty:
            df = df.loc[~(df == 0).all(axis=1)]

        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams["font.size"] = "9"
        plt.rcParams["figure.figsize"] = (width, height)

        cmap = sns.color_palette(["white", "cornflowerblue"], as_cmap=True)
        ax = sns.heatmap(
            df, annot=False, cmap=cmap, cbar=False, linewidths=5, square=True
        )

        line_color = "lightgrey"
        line_width = 0.5

        num_rows, num_cols = df.shape
        for idx in range(1, num_rows):
            plt.axhline(idx, color=line_color, lw=line_width)
        for idx in range(1, num_cols):
            plt.axvline(idx, color=line_color, lw=line_width)

        plt.axhline(0, color=line_color, lw=line_width)
        plt.axhline(num_rows, color=line_color, lw=line_width)
        plt.axvline(0, color=line_color, lw=line_width)
        plt.axvline(num_cols, color=line_color, lw=line_width)

        ax.xaxis.tick_top()
        ax.tick_params(top=False)
        ax.tick_params(left=False)
        ax.set_xticklabels(
            ax.get_xticklabels(), rotation=90, horizontalalignment="center"
        )

        plt.tight_layout()

        if not image_path:
            plt.show()
        else:
            plt.savefig(image_path, dpi=300, bbox_inches="tight")
