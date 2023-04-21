import PyPDF2
import os
from natsort import natsorted

def merge_pdf(input_path:str, output_path:str) -> None:
    """
    Merges multiple PDF files into a single PDF file

    ...

    Input
    ----------
    input_path (str): A string that represents the path to the directory containing the PDF files to be merged
    output_path (str): A string that represents the path to the output PDF file
    """

    merger = PyPDF2.PdfMerger()
    main = os.walk(input_path)
    merge_list = []

    for (roots, folders, files) in main:
        for file_name in files:
            merge_list.append(os.path.join(roots, file_name))

    merge_list = natsorted(merge_list)

    for file in merge_list:
        merger.append(file)

    with open(output_path, "wb") as out:
        merger.write(out)


def compare_pdfs(path1:str, path2:str) -> bool:
    """
    Compares two PDF files for equality in terms of their page count and contents
    
    ...

    Input
    ----------
    path1 (str): A string that represents the path to the first PDF file
    path2 (str): A string that represents the path to the second PDF file=
    """

    with open(path1, "rb") as pdf1, open(path2, "rb") as pdf2:
        pdf1_reader = PyPDF2.PdfReader(pdf1)
        pdf2_reader = PyPDF2.PdfReader(pdf2)

        pdf1_pages = len(pdf1_reader.pages)
        pdf2_pages = len(pdf2_reader.pages)

        if pdf1_pages != pdf2_pages:
            return False
        
        for page in range(pdf1_pages):
            if pdf1_reader.pages[page].extract_text() != pdf2_reader.pages[page].extract_text():
                return False 

        return True 


if __name__ == "__main__":
    merge_pdf("C:\\Users\\zawer\\Documents\\python1\\extras\\to_merge", "C:\\Users\\zawer\\Documents\\python1\\extras\\merged_pdf.pdf")
    print(compare_pdfs("C:\\Users\\zawer\\Documents\\python1\\extras\\merged_pdf.pdf", "C:\\Users\\zawer\\Documents\\python1\\extras\\maly-ksiaze.pdf"))
    