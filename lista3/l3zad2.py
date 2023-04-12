def unix_windows(path, reverse=False):
    """INSERT DOCSTRING"""
    
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