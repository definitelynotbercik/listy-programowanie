import qrcode
import cv2

def generate_QRcode(message, output_path):
    """INSERT DOCSTRING"""

    qr = qrcode.QRCode()
    qr.add_data(message)
    qr.make(fit=True)
    qr_image = qr.make_image()
    qr_image.save(output_path)


def read_QRcode(qr):
    """INSERT DOCSTRING"""
    
    img = cv2.imread(qr)
    det = cv2.QRCodeDetector()
    value, points, straight_qrcode = det.detectAndDecode(img)
    return value

if __name__ == "__main__":
    generate_QRcode("https://media.tenor.com/TRm-7oNu6DwAAAAd/cat.gif", "C:\\Users\\zawer\\Documents\\python1\\extras\\qrcode.png")
    print(read_QRcode("C:\\Users\\zawer\\Documents\\python1\\extras\\qrcode.png"))