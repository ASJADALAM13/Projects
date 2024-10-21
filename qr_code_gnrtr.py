import qrcode as qr
                         #sample link here
url=input("Enter URL:") #https://www.linkedin.com/in/asjad-alam-762770299/
myqr=qr.QRCode(
version=1, #higher the version parameter higher the size of the Qr code(i.e number of rows/columns of matrix)
error_correction=qr.constants.ERROR_CORRECT_M, #ERROR_CORRECT_M-i.e medium level errors can be corrected
box_size=10, #this define how many pixels each box of qr will have
border=4 #how thick the border of the qr code will be
)

#add the url to myqr function
myqr.add_data(url)
myqr.make(fit=True)

#make image of the link i.e QRCode
img=myqr.make_image(fill_color="red",back_color="white")
# Save the image or display it
img.save("my_qrcode.png")
img.show()
