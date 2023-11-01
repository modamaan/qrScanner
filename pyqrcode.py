import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 5,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", black_color="white")
    # give image name
    img.save("am2profile.png")

    # add url link here
generate_qrcode("https://profile-lime-two.vercel.app/")
