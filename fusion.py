from PyPDF2 import PdfFileMerger
import os




def merge(pdf_name):
    if not pdf_name:
        pdf_name = "archivo_combinado.pdf"
        
    pdfs = [pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
    pdfs = sorted(pdfs)

    if len(pdfs) == 0:
        print("No hay archivos")
        return

    if not pdf_name.endswith(".pdf"):
        pdf_name = pdf_name +".pdf"

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(open(pdf, "rb"))

    with open(pdf_name, "wb") as file:
        merger.write(file)


if __name__ == "__main__":
    pdf_name = input("Nombre de pdf: ")
    merge(pdf_name)
