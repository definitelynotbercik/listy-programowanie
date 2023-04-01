import PyPDF2

def get_split_list(num_of_pages, pages_per_file):
    """
    Return a list of page range for each split PDF file

    ...

    Input
    ----------
    num_of_pages (int): A number of pages in the initial PDF file
    pages_per_file (int): A number of pages of each splitted PDF file

    Output
    ----------
    split_list (list): A list of page range for each split PDF file
    """

    split_list = []
    modifier = 0
    for i in range(num_of_pages//pages_per_file):
        split_list.append([modifier,pages_per_file + modifier])
        modifier += pages_per_file
    split_list.append([modifier,num_of_pages])
    return split_list

def split_PDF(input_path, output_path, pages_per_file):
    """
    Split a PDF file into smaller files with a specified number of pages per file

    ...

    Input
    ----------
    input_path (str): The file path to the input PDF file to be split
    out_path (str): The file path to the directory where the output PDF files will be saved
    pages_per_file (int): A number of pages of each splitted PDF file

    Raises
    ----------
    TypeError: If the 'pages_per_file' argument is not an integer
    ValueError: If the 'pages_per_file' argument is not in the range from 1 to the number of pages in the input PDF file 
    """
    
    with open(input_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_of_pages = len(pdf_reader.pages)
        
        if type(pages_per_file) != int:
            raise TypeError("type of 'pages_per_file' has to integer")
        if pages_per_file < 1 or pages_per_file > num_of_pages:
            raise ValueError("'pages_per_file' has to be in range from 1 to number of pages in initial PDF file")
        
        split_list = get_split_list(num_of_pages, pages_per_file)
        
        for i in range(len(split_list)):
            pdf_writer = PyPDF2.PdfWriter()
            for page_num in range(split_list[i][0], split_list[i][1]):
                current_page = pdf_reader.pages[page_num]
                pdf_writer.add_page(current_page)
            with open(f"{output_path}_{split_list[i][0]+1}-{split_list[i][1]}.pdf", "wb") as out:
                pdf_writer.write(out)

if __name__ == "__main__":
    split_PDF("C:\\Users\\zawer\\Documents\\python1\\extras\\maly-ksiaze.pdf","C:\\Users\\zawer\\Documents\\python1\\extras\\nowy_ksiaze",5.5)
    