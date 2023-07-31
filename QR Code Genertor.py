#install libraries needed
#create a function that collects a text and converts it into a qrcode
# save the qrcode as an image
# run the function

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg001.png")


url = input("Enter Your url: ")
generate_qrcode(url)