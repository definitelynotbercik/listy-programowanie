import zipfile
import os
import datetime

def add_date(path):
    """INSERT DOCSTRING"""
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    path_list = path.split("\\")
    path_list[-1] = date + "_" + path_list[-1]
    date_path = "\\".join(path_list)
    return date_path

def zip_copy(input_path, output_path):
    """INSERT DOCSTRING"""
    output_path = add_date(output_path)
    with zipfile.ZipFile(output_path+".zip", 'w') as zip:
        for file in input_path:
            main = os.walk(file)
            for (roots, folders, files) in main:
                for file_name in files:
                    path = os.path.join(roots,file_name)
                    print(path)
                    if path != (output_path+".zip"):
                        zip.write(path)

if __name__ == "__main__":
    zip_copy(["C:\\Users\\zawer\\Documents\\python1\\extras"], "C:\\Users\\zawer\\Documents\\python1\\extras\\zip_folder")
