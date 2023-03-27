import PyPDF2

def get_split_list(num_of_pages, pages_per_file):
    """INSERT DOCSTRING"""
    split_list = []
    modifier = 0
    for i in range(num_of_pages//pages_per_file):
        split_list.append([modifier,pages_per_file + modifier])
        modifier += pages_per_file
    split_list.append([modifier,num_of_pages])
    return split_list

def split_PDF(input_path, output_path, pages_per_file):
    """INSERT DOCSTRING"""
    with open(input_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_of_pages = len(pdf_reader.pages)
        split_list = get_split_list(num_of_pages, pages_per_file)
        for i in range(len(split_list)):
            pdf_writer = PyPDF2.PdfWriter()
            for page_num in range(split_list[i][0], split_list[i][1]):
                print(split_list[i][0], split_list[i][1])
                current_page = pdf_reader.pages[page_num]
                pdf_writer.add_page(current_page)
            with open(f"{output_path}_{split_list[i][0]+1}-{split_list[i][1]}.pdf", "wb") as out:
                pdf_writer.write(out)

if __name__ == "__main__":
    split_PDF("C:\\Users\\zawer\\Documents\\python1\\extras\\maly-ksiaze.pdf","C:\\Users\\zawer\\Documents\\python1\\extras\\nowy_ksiaze",13)