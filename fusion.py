from PyPDF2 import PdfFileMerger
import os
import sys


def merge(pdf_name):
    if not pdf_name:
        pdf_name = "combined_file.pdf"

    pdfs = [pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
    pdfs = sorted(pdfs)

    if len(pdfs) == 0:
        print("No pdf files available")
        return

    if not pdf_name.endswith(".pdf"):
        pdf_name = pdf_name + ".pdf"

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(open(pdf, "rb"))

    with open(pdf_name, "wb") as file:
        merger.write(file)
    print(f"File {pdf_name} merged successfully")


if __name__ == "__main__":
    pdf_name = sys.argv[1]
    merge(pdf_name)
