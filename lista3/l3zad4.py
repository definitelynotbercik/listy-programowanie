import qrcode
import cv2

def generate_QRcode(message:str, output_path:str) -> None:
    """
    Generate a QR code image for a given message and save it to a file

    ...

    Input
    ----------
    message (str): The message to encode in the QR code. Must be a string
    output_path (str): The path to save the generated QR code image

    Raises
    ----------
    TypeError: If the 'message' is not a string
    """

    if type(message) != str:
        raise TypeError("Message type has to be string")
    
    qr = qrcode.QRCode()
    qr.add_data(message)
    qr.make(fit=True)
    qr_image = qr.make_image()
    qr_image.save(output_path)


def read_QRcode(qr:str) -> str:
    """
    Read a QR code image file and return the decoded message

    ...

    Input
    ----------
    qr (str): The path to the QR code image file

    Output
    ----------
    value (str): The decoded message as a string
    """
    
    img = cv2.imread(qr)
    det = cv2.QRCodeDetector()
    value, points, straight_qrcode = det.detectAndDecode(img)
    return value

if __name__ == "__main__":
    generate_QRcode("https://media.tenor.com/TRm-7oNu6DwAAAAd/cat.gif", "C:\\Users\\zawer\\Documents\\python1\\extras\\qrcode.png")
    print(read_QRcode("C:\\Users\\zawer\\Documents\\python1\\extras\\qrcode.png"))
    