import zipfile
import os
import datetime
import time

def add_folder_and_date(path:str) -> str:
    """
    Modify file path adding new folders and current date

    ...

    Input
    ----------
    path (str): The file path to modify

    Output
    ----------
    new_path (str): The modified file path
    """

    date = datetime.datetime.today().strftime('%Y-%m-%d')
    if  not os.path.exists(path + "\\backup"):
        os.mkdir(path + "\\backup")
    new_path = path + f"\\backup\\copy-{date}.zip"
    return new_path


def backup_copy(input_path:list, output_path:str, extensions:list=[], max_mod_time=10):
    """INSERT DOCSTRING"""
    
    if type(extensions) != list and type(extensions) != str:
        raise TypeError("Given extensions have to be of type list or string")
    
    if type(extensions) == list:
        for item in extensions:
            if type(item) != str:
                raise TypeError("Items in extensions list have to be of type string")

    if type(max_mod_time) != int or max_mod_time <= 0:
        raise TypeError("Given max modification time of files has to be a positive integer")

    output_path = add_folder_and_date(output_path)
    current_time = time.time()
    sec_max_mod_time = max_mod_time*86400

    with zipfile.ZipFile(output_path, 'w') as zip:
        for file in input_path:
            main = os.walk(file)
            for roots, folders, files in main:
                for file_name in files:
                    path = os.path.join(roots, file_name)
                    path_ext = path.split('.')[-1]
                    mod_date = os.path.getmtime(path)
                    date_diff = current_time - mod_date
                    if (path != output_path and
                        (path_ext in extensions or extensions == []) and
                        sec_max_mod_time >= date_diff):
                        zip.write(path)
                        print(f"Saved {path}")


if __name__ == "__main__":
    backup_copy(["C:\\Users\\zawer\\Documents\\python1\\extras"], "C:\\Users\\zawer\\Documents\\python1\\extras", "jpg,txt")
