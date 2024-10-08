import socket 
import http.server
import socketserver 
import cv2  
import pyqrcode
from pyqrcode import QRCode
from PIL import Image

hostname = socket.gethostname()    
IP = socket.gethostbyname(hostname)      
print("Your Computer IP Address is:" + IP)

url1 = IP + ":" + "8000"

#Generate QR Code
url = pyqrcode.create(url1)
url.png("myqr.png",scale=8)
img = cv2.imread("myqr.png")
#print(type(img))
cv2.imwrite('myqr.png',img)
im = Image.open('myqr.png')
im.show()

#Start http server
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("Running your port")
    httpd.serve_forever()