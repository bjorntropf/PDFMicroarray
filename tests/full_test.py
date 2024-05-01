# pylint: disable=C0114,C0116
from pdf_microarray.pdf_microarray import PDFMicroarray


def full_test():
    PDFMicroarray.process(
        ".debug/documents/sample",
        ".debug/processed/sample",
    )

    PDFMicroarray.analyze(
        ".debug/processed/sample",
        ".debug/documents/words.txt",
        ".debug/processed/data.csv",
    )

    PDFMicroarray.plot(
        ".debug/processed/data.csv",
    )

    assert True
