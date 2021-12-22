import qrcode
url=  input("Enter the URL :")
file= input("Enter File Name (With File Extension):")
img=qrcode.make(str(url))
img.save(str(file))
