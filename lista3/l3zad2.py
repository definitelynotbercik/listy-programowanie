def unix_windows(path:str, reverse:bool=False) -> None:
    """
    Converts line endings of a text file between Unix and Windows formats

    ...

    Input
    ----------
    path (str): A string that represents the path of the text file
    reverse (bool): A boolean that specifies the direction of the conversion. If 'False' (default), the function converts from Windows to Unix format; if 'True', it converts from Unix to Windows format
    """
    
    with open(path, 'rb') as file:
        text = file.read()

        if reverse:
            if b"\n" in text:
                text = text.replace(b"\n", b"\r\n") #Unix to Windows
        else:
            if b"\r\n" in text:
                text = text.replace(b"\r\n", b"\n") #Windows to Unix

    with open(path, "wb") as file:
        file.write(text)
 

if __name__ == "__main__":
    unix_windows("C:\\Users\\zawer\\Documents\\python1\\extras\\file5.txt")
    