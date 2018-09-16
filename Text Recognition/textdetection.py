# this code was written by Ahmed Harbi & Omar Ghonim on FEB.2018

import cv2
import pytesseract
import os
from PIL import Image
import serial

#Define Bluetooth
#port = "COM8"
#bluetooth = serial.Serial(port, 9600)
#bluetooth.flushInput()

#Stored Words
stored = ["SOS", "DANGER", "HELP", "Encryption", "SAMSUNG NOTES"]

#open the webcam and capture a video
cap = cv2.VideoCapture(0)

while (True):

    #read each frame in the loop as image
    image = cap.read()[1]

    #noise filtration
    #Change color space into Gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Apply thrsholding
    #Otsu to reduce the graylevel & Binary to change in B\W image
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] #save data into numerical tuple
    #Use median filter and remove noise
    blur = cv2.medianBlur(threshold, 3)

    #save filtered photo
    filtered = 'filtered.png'
    cv2.imwrite(filtered, blur)

    #export text from saved photo
    text = pytesseract.image_to_string(Image.open(filtered))

    #Delete saved picture
    os.remove(filtered)

    #Skip unwanted readed data
    if text.upper() in stored:
        #bluetooth.write(str.encode(str(text)))
        print (text)
        break
    #show captured
    cv2.imshow('Morse Code', blur)

    #Press ESC to end the program
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
