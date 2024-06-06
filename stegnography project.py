import cv2
import os
import string
img=cv2.imread("pic.jpg");
msg=input("ENTER SECREAT MESSAGE:")
password=input("ENTER A PASSCODE:")
d={}
c={}
for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)
n=0;
m=0;
z=0;
for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3
cv2.imwrite("encryptedimage.jpg",img)
os.startfile("encryptedimage.jpg")
message=""
n=0
m=0
z=0
pas=input("enter passcode for decode:")
if(password==pas):
    for i in range(len(msg)):
        message+=c[img[n,m,z]]
        n+=1
        m+=1
        z=(z+1)%3
    print("decode message is:",message)
else:
    print("you entered a wrong pass code:")
