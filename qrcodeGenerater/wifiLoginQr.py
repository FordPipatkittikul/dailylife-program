import qrcode           #pip install qrcode

def get_working_directory():
    file_path = r"C:\Users\Asus\PycharmProjects\asdasdsda.png"
    return file_path

# design how you want your qr code look like
qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)
# add data
wifi = "WIFI:S:eduroam;T:WPA;P:your_password123;;"
qr.add_data(wifi)
qr.make(fit=True)
qrcode_img = qr.make_image(fill_color="green", back_color="white")
qrcode_img.save(get_working_directory())







