import qrcode
text=input("Enter the text: ")
file=input("Enter file name (With extension):")
img=qrcode.make(str(text))
img.save(str(file))