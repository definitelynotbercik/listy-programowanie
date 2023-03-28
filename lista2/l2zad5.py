from PIL import Image, ImageEnhance

def add_watermark(img_path, watermark_path, alpha):
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
    watermark.putalpha(alpha)

    if watermark.width > img.width or watermark.height > img.height:
        watermark = watermark.resize((img.width,img.height))
        img.paste(watermark, [0,0], watermark)
    else:
        img.paste(watermark, [(img.width-watermark.width)//2,(img.height-watermark.height)//2], watermark)

    img.save(img_path)


if __name__ == "__main__":
    add_watermark("C:\\Users\\zawer\\Documents\\python1\\extras\\cat_img.jpg", "C:\\Users\\zawer\\Documents\\python1\\extras\\resized_img.jpg", 100)
    