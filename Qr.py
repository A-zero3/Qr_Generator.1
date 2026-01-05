import qrcode

url = input("Enter the URL: ").strip()
file_path = "D:\\Python-practice\\Qr-Image-Location\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("REQUESTED QR IS MADE!!!")