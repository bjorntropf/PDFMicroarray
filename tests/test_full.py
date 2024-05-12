# pylint: disable=C0114,C0116
from pdf_microarray.pdf_microarray import PDFMicroarray


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
        ".debug/processed/data.csv",
    )

    assert True


def test_plot():
    PDFMicroarray.plot(
        ".debug/processed/data.csv",
        ".debug/processed/plot.png",
    )

    assert True
