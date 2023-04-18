import qrcode

def generate_QRcode(message, output_path):
    qr = qrcode.QRCode()
    qr.add_data(message)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="white", back_color="black")
    qr_image.save(output_path)

if __name__ == "__main__":
    generate_QRcode("abcd", "C:\\Users\\zawer\\Documents\\python1\\extras\\qrcode.png")