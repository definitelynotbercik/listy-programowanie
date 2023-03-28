from PIL import Image, ImageEnhance

def add_watermark(img_path, watermark_path, alpha=100):
    """INSERT DOCSTRING"""
    try:
        img = Image.open(img_path)
    except:
        raise FileNotFoundError(f"No such path or directory: {img_path}")
    try:
        watermark = Image.open(watermark_path).convert("RGBA")
    except:
        raise FileNotFoundError(f"No such path or directory: {watermark_path}")
    
    if type(alpha) != int or alpha<0 or alpha>255:
        raise ValueError("Alpha has to be an integer in range 0-255")
    
    brightness = ImageEnhance.Brightness(watermark)
    sharpness = ImageEnhance.Sharpness(watermark)
    watermark = sharpness.enhance(0.5)
    watermark = brightness.enhance(0.3)
    watermark.putalpha(alpha)

    if watermark.width > img.width or watermark.height > img.height:
        watermark = watermark.resize((img.width,img.height))
        img.paste(watermark, [0,0], watermark)
    else:
        img.paste(watermark, [(img.width-watermark.width)//2,(img.height-watermark.height)//2], watermark)
    
    if img_path[-4:] == ".jpg":
        img_path = img_path[:-4]+"_with_watermark.jpg"
    else:
        img_path = img_path+"_with_watermark.jpg"

    img.save(img_path)


if __name__ == "__main__":
    add_watermark("C:\\Users\\zawer\\Documents\\python1\\extras\\cat_img.jpg",
                   "C:\\Users\\zawer\\Documents\\python1\\extras\\dog_head_img.jpg", 255)
