'''
Created on 3 thg 5, 2022

@author: A315-56
'''
from hashlib import new
from multiprocessing.sharedctypes import Value
import sys
import os
from types import new_class
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from clock import *
import datetime
import requests
import random

from canvas import *
from traitlets import Int
from datetime import date

from firebase import firebase

os.system("pyuic5 -x Main_Scr.ui -o Main_Scr.py")
os.system("pyrcc5 -o Weather_Icon_rc.py Weather_Icon.qrc")
os.system("pyrcc5 -o Icon_rc.py Icon.qrc")


from Main_Scr import *
from style import *
from GUI_PyQt5_Func import *
from button_bot_func import *

Counter = 0
	
class Main_Screen(Ui_MainWindow):
	UserName = " "
	firebase = firebase.FirebaseApplication('https://pygui-iot-7dfeb-default-rtdb.firebaseio.com', None)
	PH = 7
	dPH = 1
	def __init__(self, mainwindow):
		self.setupUi(mainwindow)
		self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
		self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
		
		#================ Đất ======================
		# self.verticalSlider_1.valueChanged.connect(self.Dat_Gauge_Temp_CallBack)
		# self.verticalSlider_2.valueChanged.connect(self.Dat_Gauge_Humi_CallBack)
		# self.verticalSlider_3.valueChanged.connect(self.Dat_Gauge_PH_CallBack)

		# #================ không khí =================
		# self.KK_Gauge_Temp_CallBack(random.randint(0, 100))
		# self.KK_Gauge_Humi_CallBack(random.randint(0, 100))

		# #=================== Lux ======================
		self.Gauge_LUX_CallBack(random.randint(0, 100))

		# #=================== Wh =======================
		self.verticalSlider_2.valueChanged.connect(self.Gauge_WH_CallBack)

		#=================== thời tiết và thời gian ================
		self.clock_time = Clock()
		self.Top_Ctrl_frame5_clock_widget.addWidget(self.clock_time)
		try:
			self.weather()
		except :
			Wifi_icon = QtGui.QIcon()
			Wifi_icon.addPixmap	(QtGui.QPixmap(":/Green_Icon/Icon_Green/wifi-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.Wifi_btn.setIcon(Wifi_icon)

		#===================== chart =====================
		#__________1
		self.grafica_1 = Canvas_grafica()
		self.Top_Para_frame1_body_chart.addWidget(self.grafica_1)
		#__________2
		self.grafica_2 = Canvas_grafica_1()
		self.Top_Para_frame1_body_chart_PH.addWidget(self.grafica_2)
		#__________3
		self.grafica_3 = Canvas_grafica_2()
		self.Top_Para_frame1_body_chart_Do_Am_KK.addWidget(self.grafica_3)
		#__________4
		self.grafica_4 = Canvas_grafica_3()
		self.Top_Para_frame1_body_chart_T_KK.addWidget(self.grafica_4)
		# self.end_text.clicked.connect(self.test())

		self.Menu_btn.clicked.connect      (lambda: UIFunctions.ToggleMenu (self, 50, 300))
		self.Control_btn.clicked.connect   (lambda: UIFunctions.Select_Menu(self, 1))
		self.Parameter_btn.clicked.connect (lambda: UIFunctions.Select_Menu(self, 2))
		self.Setting_btn.clicked.connect   (lambda: UIFunctions.Select_Menu(self, 3))
		self.Properties_btn.clicked.connect(lambda: UIFunctions.Select_Menu(self, 4))
		self.Slogan_OKE_btn.clicked.connect(lambda: UIFunctions.Change_slogan(self))
		
		self.Slider1_2.valueChanged.connect(lambda: self.Set_PH())
		self.Slider2_3.valueChanged.connect(lambda: self.Set_dPH())
		
		self.Slider2_4.valueChanged.connect(self.Change_min_max_Sprinker)
		self.Mist.valueChanged.connect(self.Change_min_max_Sprinker)
		
		self.Mist_Button.valueChanged.connect(lambda: button_slider.io(self))
		self.open_light_Button.valueChanged.connect(lambda: button_slider.io(self))
		self.Roof.valueChanged.connect(lambda: button_slider.io(self))
		
		self.Timer_Start()


# #=========================================================================== TIMER =================================================================================

	def Set_PH(self):
		self.PH = self.Slider1_2.value()
		_translate = QtCore.QCoreApplication.translate
		self.Slider_label1_13.setText(_translate("MainWindow", str(self.PH)))
			
	def Set_dPH(self):
		self.dPH = self.Slider2_3.value()
		_translate = QtCore.QCoreApplication.translate
		self.Slider_label1_14.setText(_translate("MainWindow", "+-" + str(self.dPH)))	 
			
	def Change_min_max_Sprinker(self):
		self.Slider_label1_12.setText(str(self.Slider2_4.value()))
		self.Mist.setMinimum(0)
		self.Mist.setMaximum(int(self.Slider2_4.value()))

		self.Slider_label1_20.setText(str(self.Mist.value()))
		print(self.Mist.value())
		
	def Timer_Start(self):
		self.timer_WH = QtCore.QTimer()
		self.timer_WH.start(1000)
		self.timer_WH.timeout.connect(self.timer_Wh)
		# Timer cho cái quạt
		self.timer_fan = QtCore.QTimer()
		self.timer_fan.start(1)
		self.timer_fan.timeout.connect(lambda: BTN_Func.Fan_Timer_CallBack(self))
		# Timer cho firebase
		self.timer_firebase = QtCore.QTimer()
		self.timer_firebase.start(5000)
		self.timer_firebase.timeout.connect(self.Firebase_CallBack)


	def Firebase_CallBack(self):
		self.firebase_Json_data = self.firebase.get('/Environment parameter', None)
		
		print(self.firebase_Json_data["Land Temperature"])
		self.Dat_Gauge_Temp_CallBack(float(self.firebase_Json_data["Land Temperature"]))
		
		print(self.firebase_Json_data["Air Temperature"])
		self.KK_Gauge_Temp_CallBack(float(self.firebase_Json_data["Air Temperature"]))
		
		print(self.firebase_Json_data["Land Humidity"])
		self.Dat_Gauge_Humi_CallBack(float(self.firebase_Json_data["Land Humidity"]))
		
		print(self.firebase_Json_data["Air Humidity"])
		self.KK_Gauge_Humi_CallBack(float(self.firebase_Json_data["Air Humidity"]))
		
		print(self.firebase_Json_data["Land PH"])
		self.Dat_Gauge_PH_CallBack(float(self.firebase_Json_data["Land PH"]))
		print("PH:" + str(self.PH) + "    dPH:" + str(self.dPH))
		if(float(self.firebase_Json_data["Land PH"]) < float(self.PH + self.dPH)):
			style = """background-color: rgb(200, 80, 0);
					border-radius: 61px;"""
			text_style = """color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 245, 0, 255), stop:1 rgba(0, 159, 0, 255));
					background-color: rgba(0, 0, 0, 0);"""
		elif(float(self.firebase_Json_data["Land PH"]) > float(self.PH - self.dPH)):
			style = """background-color: rgb(90, 0, 150);
					border-radius: 61px;"""
			text_style = """color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(200, 200, 200, 255));
					background-color: rgba(0, 0, 0, 0);"""
		else:
			style = """background-color: rgb(245, 245, 245);
					border-radius: 61px;"""
			text_style = """color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));
					background-color: rgba(0, 0, 0, 0);"""
		self.frame_27.setStyleSheet(style)	
		self.pushButton_13.setStyleSheet(text_style)	
		self.pushButton_14.setStyleSheet(text_style)	
		
		print(self.firebase_Json_data["Brightness"])
		self.Gauge_LUX_CallBack(float(self.firebase_Json_data["Brightness"]))
#============================================================================ ĐẤT ==================================================================================
	def Dat_Gauge_Temp(self, value):
		styleSheet = """
			border-radius: 75px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));
		"""
		stop2 = str(value * -0.007485 + 1)
		stop1 = str(value * -0.007485 + 1 - 0.01)
		styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
		self.frame_6.setStyleSheet(styleSheet)

	def Dat_Gauge_Temp_CallBack(self, value):	
		
		self.Dat_Gauge_Temp(float(value))
		_translate = QtCore.QCoreApplication.translate
		self.pushButton_10.setText(_translate("MainWindow", str(value) + "°C"))
		
	def Dat_Gauge_Humi(self, value):
		styleSheet = """
			border-radius: 75px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));
		"""
		stop2 = str(value * -0.007485 + 1)
		stop1 = str(value * -0.007485 + 1 - 0.01)
		styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
		self.frame_24.setStyleSheet(styleSheet)

	def Dat_Gauge_Humi_CallBack(self, value):
		self.Dat_Gauge_Humi(int(value))
		_translate = QtCore.QCoreApplication.translate
		self.pushButton_12.setText(_translate("MainWindow", str(value) + "%"))

	def Dat_Gauge_PH(self, value):
		styleSheet = """border-radius: 75px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));
"""
		stop2 = str(value * -0.0535 + 1)
		stop1 = str(value * -0.0535 + 1 - 0.01)
		styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
		self.frame_26.setStyleSheet(styleSheet)

	def Dat_Gauge_PH_CallBack(self, value):
		self.Dat_Gauge_PH(int(value))
		_translate = QtCore.QCoreApplication.translate
		self.pushButton_14.setText(_translate("MainWindow", str(value)))

# #============================================================================ Không khí ==================================================================================

	def KK_Gauge_Temp(self, value):
		styleSheet = """border-radius: 75px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));
"""
		stop2 = str(value * -0.007485 + 1)
		stop1 = str(value * -0.007485 + 1 - 0.01)
		styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
		self.frame_30.setStyleSheet(styleSheet)

	def KK_Gauge_Temp_CallBack(self, value):
		self.KK_Gauge_Temp(int(value))
		_translate = QtCore.QCoreApplication.translate
		self.pushButton_18.setText(_translate("MainWindow", str(value) + "°C"))

	def KK_Gauge_Humi(self, value):
		styleSheet = """border-radius: 75px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));
"""
		stop2 = str(value * -0.007485 + 1)
		stop1 = str(value * -0.007485 + 1 - 0.01)
		styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
		self.frame_32.setStyleSheet(styleSheet)

	def KK_Gauge_Humi_CallBack(self, value):
		self.KK_Gauge_Humi(int(value))
		_translate = QtCore.QCoreApplication.translate
		self.pushButton_20.setText(_translate("MainWindow", str(value) + "%"))

# #============================================================================ LUX ==================================================================================

	def Gauge_LUX(self, value):
		styleSheet = """border-radius: 75px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:224.5, stop:0 rgba(245, 245, 245, 255), stop:{stop_val1} rgba(245, 245, 245, 255), stop:{stop_val2} rgba(0, 0, 0, 0));
"""
		stop2 = str(value * -0.007485 + 1)
		stop1 = str(value * -0.007485 + 1 - 0.01)
		styleSheet = styleSheet.replace("{stop_val1}", stop1).replace("{stop_val2}", stop2)
		self.frame_28.setStyleSheet(styleSheet)

	def Gauge_LUX_CallBack(self, value):
		self.Gauge_LUX(int(value))
		_translate = QtCore.QCoreApplication.translate
		self.pushButton_16.setText(_translate("MainWindow", str(value) + "Lux"))

# #=========================================================================== WH =============================================================================================

	def Gauge_WH(self, value):
		styleSheet = """
			border-radius: 105px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{STOP_1}, stop:0.995399 rgba(0, 0, 42, 0), stop:0.996435 rgba(255, 0, 0, 255), stop:0.998964 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 42, 0));
		"""
		progress = int(100-value)
		stop_1 = str(1.8*progress)
		styleSheet = styleSheet.replace("{STOP_1}", stop_1)
		self.Top_Ctrl_frame4_body_Wh_4.setStyleSheet(styleSheet)

	def Gauge_WH_CallBack(self, value):
		self.Gauge_WH(int(value))

	def timer_Wh(self):
		global Counter
		Rem_1 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 0 0 0 {VALUE_1}</span></p></body></html>"""
		Rem_2 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 0 0 {VALUE_1} {VALUE_2}</span></p></body></html>"""
		Rem_3 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 0 {VALUE_1} {VALUE_2} {VALUE_3}</span></p></body></html>"""
		Rem_4 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">0 {VALUE_1} {VALUE_2} {VALUE_3} {VALUE_4}</span></p></body></html>"""
		Rem_5 ="""<html><head/><body><p><span style=" font-size:16pt; color:#ff0000;">{VALUE_1} {VALUE_2} {VALUE_3} {VALUE_4} {VALUE_5}</span></p></body></html>"""
		if Counter > 10000:
			Counter = 0
		Counter += 1
		if Counter < 10:
			newRem = Rem_1.replace("{VALUE_1}", str(Counter))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 10 and Counter < 100:
			newRem = Rem_2.replace("{VALUE_1}", str(Counter//10)).replace("{VALUE_2}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 100 and Counter < 1000:
			newRem = Rem_3.replace("{VALUE_1}", str(Counter//100)).replace("{VALUE_2}", str(Counter//10%10)).replace("{VALUE_3}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 1000 and Counter < 10000:
			newRem = Rem_4.replace("{VALUE_1}", str(Counter//1000)).replace("{VALUE_2}", str(Counter//100%10)).replace("{VALUE_3}", str(Counter//10%10)).replace("{VALUE_4}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)
		elif Counter >= 10000 and Counter < 100000:
			newRem = Rem_4.replace("{VALUE_1}", str(Counter//10000)).replace("{VALUE_2}", str(Counter//1000%10)).replace("{VALUE_3}", str(Counter//100%10)).replace("{VALUE_4}", str(Counter//10%10)).replace("{VALUE_5}", str(Counter%10))
			self.Top_Ctrl_frame4_body_metter.setText(newRem)


# #=========================================================================================== thời tiết ================================================================================

	def weather(self):
		today = date.today()
		days=["T2","T3","T4","T5","T6","T7","CN"]
		dayNumber=today.weekday()
		print(days[dayNumber])

		_translate = QtCore.QCoreApplication.translate
		api_address='https://api.openweathermap.org/data/2.5/weather?lat=10.850145464871641&lon=106.7716601973813&appid=59e434bde2d8ff7f30cfdb363d79aa61&lang=vi'
		json_data = requests.get(api_address).json()
		format_add = json_data['main']

		T_weather = """<html><head/><body><p><span style=" font-size:18pt; color:#ff0808;">{VALUE}</span><span style=" font-size:18pt; color:#ff0808; vertical-align:super;">0</span><span style=" font-size:18pt; color:#ff0808;">C</span></p></body></html>"""
		Value_1 = str(int(format_add["temp"]-273))

		new_T_Weather = T_weather.replace("{VALUE}",Value_1)
		self.T_Weather_label.setText(new_T_Weather)

		# rem = json_data['main']['humidity']
		# ram = json_data['weather'][0]['description']
		print(json_data["weather"][0]["icon"])

		#============================== thu ngay ===================================

		if dayNumber == 0:
			self.T2.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T2.setText(days[dayNumber])
			self.T3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T3.setText(day)


		elif dayNumber == 1:
			self.T3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T3.setText(days[dayNumber])
			self.T4.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T4.setText(day)


		elif dayNumber == 3:
			self.T4.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T4.setText(days[dayNumber])
			self.T5.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T5.setText(day)


		elif dayNumber == 4:
			self.T5.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T5.setText(days[dayNumber])
			self.T6.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T6.setText(day)

		elif dayNumber == 5:
			self.T6.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T6.setText(days[dayNumber])
			self.T7.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.T7.setText(day)


		elif dayNumber == 6:
			self.T7.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			self.T7.setText(days[dayNumber])
			self.CN.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"font: 12pt \"Nirmala UI\";")
			day = str(today.day) + "/" + str(today.month)
			self.CN.setText(day)

		#============================== Thoi tiet ==================================


		if json_data['weather'][0]['main'] == 'Rain':
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(":/Weather/animated/rainy-7.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_3.setIcon(icon)
			text_do_am = """<html><head/><body><p><span style=" font-size:18pt; color:#3ec5ff;">{VALUE_D}%</span></p></body></html>"""
			new_text_do_am = text_do_am.replace("{VALUE_D}",str(format_add["humidity"]))
			self.pushButton_3.setIcon(icon)
			self.T_Do_Am_label_2.setText(new_text_do_am)
			self.pushButton_6.setText(_translate("MainWindow", "Trời đang mưa"))

		elif json_data['weather'][0]['main'] == 'Thunderstorm':
			text_do_am = """<html><head/><body><p><span style=" font-size:18pt; color:#3ec5ff;">{VALUE_D}%</span></p></body></html>"""
			new_text_do_am = text_do_am.replace("{VALUE_D}",str(format_add["humidity"]))
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(":/Weather/animated/thunder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_3.setIcon(icon)
			self.T_Do_Am_label_2.setText(new_text_do_am)
			self.pushButton_6.setText(_translate("MainWindow", "Giông gió nhiều sét"))


		elif json_data['weather'][0]['main'] == 'Clouds':
			text_do_am = """<html><head/><body><p><span style=" font-size:18pt; color:#3ec5ff;">{VALUE_D}%</span></p></body></html>"""
			new_text_do_am = text_do_am.replace("{VALUE_D}",str(format_add["humidity"]))
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(":/Weather/animated/cloudy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.pushButton_3.setIcon(icon)
			self.T_Do_Am_label_2.setText(new_text_do_am)
			self.pushButton_6.setText(_translate("MainWindow", "Trời nhiều mây"))
		#print(json_data)
		print("Thời Tiết hiện tại: {0} Nhiệt độ thấp nhất là {1} Nhiệt độ cao nhất là {2} Độ C".format(
		json_data['weather'][0]['main'],float(format_add['temp_min']-273),float(format_add['temp_max']-273)))
