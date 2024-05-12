# pylint: disable=C0114,C0116
from pdf_microarray.pdf_microarray import PDFMicroarray
from pdf_microarray.plot_microarray import PlotMicroarray


def test_process():
    PDFMicroarray.process(
        ".debug/documents",
        ".debug/processed",
    )

    assert True


def test_analyze():
    PDFMicroarray.analyze(
        ".debug/processed",
        ".debug/documents/words.txt",
        ".debug/data.csv",
    )

    assert True


def test_plot():
    PlotMicroarray.plot(
        ".debug/data.csv",
        ".debug/plot.png",
    )

    assert True
