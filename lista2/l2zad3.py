import zipfile
import os
import datetime

def add_date(path):
    """
    Add current date to the file name in the given file path

    ...

    Input
    ----------
    path (str): The file path to modify

    Output
    ----------
    date_path (str): The modified file path with the current date added to the file name
    """

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    path_list = path.split("\\")
    path_list[-1] = date + "_" + path_list[-1]
    date_path = "\\".join(path_list)
    return date_path

def zip_copy(input_path, output_path):
    """
    Compress files in the input path and save them to the specified output path

    ...

    Input
    ----------
    input_path (list): A list of file paths to compress
    output_path (str): The file path to save the compressed files

    Raises
    ----------
    FileNotFoundError: If the input or output path is invalid
    """
    
    output_path = add_date(output_path)
    try:
        with zipfile.ZipFile(output_path+".zip", 'w') as zip:
            for file in input_path:
                main = os.walk(file)
                for (roots, folders, files) in main:
                    for file_name in files:
                        path = os.path.join(roots,file_name)
                        print(path)
                        if path != (output_path+".zip"):
                            zip.write(path)
    except:
        raise FileNotFoundError(f"No such file or directory {input_path} or {output_path}")

if __name__ == "__main__":
    zip_copy(["C:\\Users\\zawer\\Documents\\python1\\extras"], "C:\\Users\\zawer\\Documents\\python1\\extras\\zip_folder")
