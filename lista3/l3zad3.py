import PyPDF2
import os

def merge_pdf(input_path, output_path):
    merger = PyPDF2.PdfMerger()
    main = os.walk(input_path)

    for (roots, folders, files) in main:
        for file_name in files:
            print(os.path.join(roots, file_name))
            merger.append(os.path.join(roots, file_name))

    with open(output_path, "wb") as out:
        merger.write(out)


if __name__ == "__main__":
    merge_pdf("C:\\Users\\zawer\\Documents\\python1\\extras\\to_merge", "C:\\Users\\zawer\\Documents\\python1\\extras\\merged_pdf.pdf")