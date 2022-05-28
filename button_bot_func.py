from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Main_Scr import *

from firebase import firebase

counterr_2 = 360

class BTN_Func(Ui_MainWindow):  
	def Fan_Timer_CallBack(self):
		value = self.Fan_control.value()
		global counterr_2
		ram = """border-radius: 60px;
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{VALUE}, stop:0.0866477 rgba(130, 255, 0, 0), stop:0.0892553 rgba(128, 255, 255, 255), stop:0.241798 rgba(0, 22, 255, 255), stop:0.244405 rgba(130, 255, 0, 0), stop:0.425221 rgba(130, 255, 0, 0), stop:0.426525 rgba(128, 255, 255, 255), stop:0.579068 rgba(0, 22, 255, 255), stop:0.582979 rgba(130, 255, 0, 0), stop:0.764205 rgba(130, 255, 0, 0), stop:0.76942 rgba(128, 255, 255, 255), stop:0.912836 rgba(0, 22, 255, 255), stop:0.915443 rgba(130, 255, 0, 0));
"""
		newram = ram.replace("{VALUE}", str(counterr_2%360.0))
		if value != 3 :
			self.pushButton_7.hide()
			self.pushButton_8.hide()

		else:
			self.pushButton_7.show()
			self.pushButton_8.show()

		self.label_17.setStyleSheet(newram)
		counterr_2 -= value * 0.25
		if counterr_2 < 0:
			counterr_2 = 360.0


class button_slider(Ui_MainWindow):
	firebase = firebase.FirebaseApplication('https://pygui-iot-7dfeb-default-rtdb.firebaseio.com', None)
	def io(self):	
		if self.Mist_Button.value() == 1:
			self.firebase.post('/users', "Data", 1);
			self.Mist_Button.setStyleSheet("QSlider::groove:horizotal{\n"
			"    border: 1px solid rgb(156, 156, 156);\n"
			"    color: rgb(0, 0, 255);\n"
			"    height: 20px;\n"
			"    width: 45px;\n"
			"    border-radius: 10px;\n"
			"    background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:1, y2:0, stop:0.0789133 rgba(0, 246, 255, 255), stop:0.467626 rgba(0, 171, 255, 255), stop:0.937904 rgba(0, 111, 255, 255));\n"
			"    margin: 1px;\n"
			"}\n"
			"QSlider::handle:horizotal{\n"
			"    border:  1px solid rgb(165, 165, 165);\n"
			"    background-color: rgb(240, 240, 240);\n"
			"    height: 30px;\n"
			"    width: 30px;\n"
			"    border-radius: 15px;\n"
			"    margin: -5px;\n"
			"}\n"
			"")

		else :
			self.firebase.post('/users', "Data", 0);
			self.Mist_Button.setStyleSheet("QSlider::groove:horizotal{\n"
			"    border: 1px solid rgb(156, 156, 156);\n"
			"    color: rgb(0, 0, 255);\n"
			"    height: 20px;\n"
			"    width: 45px;\n"
			"    border-radius: 10px;\n"
			"    background-color: rgb(200, 200, 200);\n"
			"    margin: 1px;\n"
			"}\n"
			"QSlider::handle:horizotal{\n"
			"    border:  1px solid rgb(165, 165, 165);\n"
			"    background-color: rgb(240, 240, 240);\n"
			"    height: 30px;\n"
			"    width: 30px;\n"
			"    border-radius: 15px;\n"
			"    margin: -5px;\n"
			"}\n"
			"")


		if self.open_light_Button.value() == 1:
			self.open_light_Button.setStyleSheet("QSlider::groove:horizotal{\n"
			"    border: 1px solid rgb(156, 156, 156);\n"
			"    color: rgb(0, 0, 255);\n"
			"    height: 20px;\n"
			"    width: 45px;\n"
			"    border-radius: 10px;\n"
			"    background-color: rgb(255, 255, 0);\n"
			"    margin: 1px;\n"
			"}\n"
			"QSlider::handle:horizotal{\n"
			"    border:  1px solid rgb(165, 165, 165);\n"
			"    background-color: rgb(240, 240, 240);\n"
			"    height: 30px;\n"
			"    width: 30px;\n"
			"    border-radius: 15px;\n"
			"    margin: -5px;\n"
			"}\n"
			"")

		else :
			self.open_light_Button.setStyleSheet("QSlider::groove:horizotal{\n"
			"    border: 1px solid rgb(156, 156, 156);\n"
			"    color: rgb(0, 0, 255);\n"
			"    height: 20px;\n"
			"    width: 45px;\n"
			"    border-radius: 10px;\n"
			"    background-color: rgb(200, 200, 200);\n"
			"    margin: 1px;\n"
			"}\n"
			"QSlider::handle:horizotal{\n"
			"    border:  1px solid rgb(165, 165, 165);\n"
			"    background-color: rgb(240, 240, 240);\n"
			"    height: 30px;\n"
			"    width: 30px;\n"
			"    border-radius: 15px;\n"
			"    margin: -5px;\n"
			"}\n"
			"")

		if self.Roof.value() == 1:
			self.Roof.setStyleSheet("QSlider::groove:horizotal{\n"
			"    border: 1px solid rgb(156, 156, 156);\n"
			"    color: rgb(0, 0, 255);\n"
			"    height: 20px;\n"
			"    width: 45px;\n"
			"    border-radius: 10px;\n"
			"    background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:1, y2:0, stop:0.0789133 rgba(0, 246, 255, 255), stop:0.467626 rgba(0, 171, 255, 255), stop:0.937904 rgba(0, 111, 255, 255));\n"
			"    margin: 1px;\n"
			"}\n"
			"QSlider::handle:horizotal{\n"
			"    border:  1px solid rgb(165, 165, 165);\n"
			"    background-color: rgb(240, 240, 240);\n"
			"    height: 30px;\n"
			"    width: 30px;\n"
			"    border-radius: 15px;\n"
			"    margin: -5px;\n"
			"}\n"
			"")

		else :
			self.Roof.setStyleSheet("QSlider::groove:horizotal{\n"
			"    border: 1px solid rgb(156, 156, 156);\n"
			"    color: rgb(0, 0, 255);\n"
			"    height: 20px;\n"
			"    width: 45px;\n"
			"    border-radius: 10px;\n"
			"    background-color: rgb(200, 200, 200);\n"
			"    margin: 1px;\n"
			"}\n"
			"QSlider::handle:horizotal{\n"
			"    border:  1px solid rgb(165, 165, 165);\n"
			"    background-color: rgb(240, 240, 240);\n"
			"    height: 30px;\n"
			"    width: 30px;\n"
			"    border-radius: 15px;\n"
			"    margin: -5px;\n"
			"}\n"
			"")









