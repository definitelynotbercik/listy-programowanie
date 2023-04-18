import PyPDF2
import os
from natsort import natsorted

def merge_pdf(input_path, output_path):
    """INSERT DOCSTRING"""

    merger = PyPDF2.PdfMerger()
    main = os.walk(input_path)
    merge_list = []

    for (roots, folders, files) in main:
        for file_name in files:
            merge_list.append(os.path.join(roots, file_name))

    merge_list = natsorted(merge_list)
    print(merge_list)

    for file in merge_list:
        merger.append(file)

    with open(output_path, "wb") as out:
        merger.write(out)


def compare_pdfs(pdf1, pdf2):
    pass


if __name__ == "__main__":
    merge_pdf("C:\\Users\\zawer\\Documents\\python1\\extras\\to_merge", "C:\\Users\\zawer\\Documents\\python1\\extras\\merged_pdf.pdf")