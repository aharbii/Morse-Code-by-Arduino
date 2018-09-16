#this Code was written by Ahmed Harbi on June.2018

#Commit: Sha 1
#This Code was developed by Ahmed Harbi on August.2018
#Add Bluetooth Connection to call Serial bluetooth Devices

import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
import serial
import time

#define Bluetooth Device
#port = "COM8"
#bluetooth = serial.Serial(port, 9600)
#bluetooth.flushInput()

 
# create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Morse Code')

#Laser on Button
laserOn = QPushButton('Laser on', w)
laserOn.move(20,10)

#Buzzer on Button
buzzerOn = QPushButton('Buzzer on', w)
buzzerOn.move(20,40)

#Laser off Button
laserOff = QPushButton('Laser off', w)
laserOff.move(225,10)

#Buzzer off Button
buzzerOff = QPushButton('Buzzer off', w)
buzzerOff.move(225,40)

# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 70)
textbox.resize(280,40)
 
# Set window size.
w.resize(320, 200)
 
# send button
send = QPushButton('Send', w)
send.move(20,120)
 
# Create the actions
@pyqtSlot()

#send Button
def on_click_send(self):
    textboxValue = textbox.text()
    bluetooth.write(str.encode(str(textboxValue)))
    print("Sent")
    
    
#Laser On Button
def on_click_laserOn(self):
    bluetooth.write(str.encode(str('100')))
    print("Sent")

#Buzzer On Button
def on_click_buzzerOn(self):
    bluetooth.write(str.encode(str('50')))
    print("Sent")

#Laser Off Button
def on_click_laserOff(self):
    bluetooth.write(str.encode(str('0')))
    print("Sent")

#Buzzer Off Button
def on_click_buzzerOff(self):
    bluetooth.write(str.encode(str('25')))
    print("Sent")
    
# connect the signals to the slots
send.clicked.connect(on_click_send)
laserOn.clicked.connect(on_click_laserOn)
buzzerOn.clicked.connect(on_click_buzzerOn)
laserOff.clicked.connect(on_click_laserOff)
buzzerOff.clicked.connect(on_click_buzzerOff)

 
# Show the window and run the app
w.show()
app.exec_()

