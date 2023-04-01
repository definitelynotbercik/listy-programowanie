from PIL import Image

def img_min(input_path, new_size, output_path):
    """
    Resize an image and save the resized image to a specified output path

    ...

    Input
    ----------
    input_path (str): The file path of the original image to be resized
    new_size (tuple or list): The new size of the resized image, specified as a tuple or list of two integers representing the width and height, in pixels
    output_path (str): The file path to save the resized image

    Raises
    ----------
    FileNotFoundError: If the input or output path is invalid
    TypeError: If the "new_size" argument is not a tuple or list of two integers
    """
    
    try:
        img = Image.open(input_path)
    except:
        raise FileNotFoundError(f"No such path or directory: {input_path}")
    if type(new_size) != tuple and type(new_size) != list:
        raise TypeError("Type of new size for resized image should be tuple or list")
    if len(new_size) != 2:
        raise TypeError("Length of new size for resized image should be 2")
    if type(new_size[0]) != int or type(new_size[1]) != int:
        raise TypeError("Type should be integer") 
    img_resized = img.resize(new_size)
    try:
        img_resized.save(output_path + ".jpg")
    except:
        raise FileNotFoundError(f"No such path or directory: {output_path}")

if __name__ == "__main__":
    img_min("C:\\Users\\zawer\\Documents\\python1\\extras\\test_image.jpg", (100,100), "C:\\Users\\zawer\\Documents\\python1\\extras\\resized_img")
