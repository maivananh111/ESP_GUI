'''
Created on 7 thg 5, 2022

@author: A315-56
'''

from PyQt5 import QtCore
from PyQt5.QtCore import *
from clock import *

from Main_Scr import *
from style import*




class UIFunctions(Ui_MainWindow):              
    def ToggleMenu(self, minWidth, maxWidth):
        width = self.Slide_menu.width()
        Menu_btn_icon = QtGui.QIcon()
        _translate = QtCore.QCoreApplication.translate
        if width == minWidth:
            newWidth = maxWidth
            self.APP_name.setText      (_translate("MainWindow", "Nhà kính 4 tỷ"))
            self.User_name.setText     (_translate("MainWindow", "Đinh Thanh Tùng"))
            self.Control_btn.setText   (_translate("MainWindow", "Bảng điều khiển     "))
            self.Parameter_btn.setText (_translate("MainWindow", "Giám sát số liệu     "))
            self.Setting_btn.setText   (_translate("MainWindow", "Thiết lập hệ thống"))
            self.Properties_btn.setText(_translate("MainWindow", "Thông tin              "))
            self.Login_return.setText  (_translate("MainWindow", "Đăng xuất             "))
            Menu_btn_icon.addPixmap    (QtGui.QPixmap(":/White_Icon/Icon_White/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Menu_btn.setIcon      (Menu_btn_icon)
        else:
            newWidth = minWidth
            self.APP_name.setText      (_translate("MainWindow", ""))
            self.User_name.setText     (_translate("MainWindow", ""))
            self.Control_btn.setText   (_translate("MainWindow", ""))
            self.Parameter_btn.setText (_translate("MainWindow", ""))
            self.Setting_btn.setText   (_translate("MainWindow", ""))
            self.Properties_btn.setText(_translate("MainWindow", ""))
            self.Login_return.setText    (_translate("MainWindow", ""))
            Menu_btn_icon.addPixmap    (QtGui.QPixmap(":/White_Icon/Icon_White/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Menu_btn.setIcon      (Menu_btn_icon)
            

        self.animation = QPropertyAnimation(self.Slide_menu, b"maximumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutBack)
        self.animation.start()
    
    
                            
            
    def Select_Menu(self, tab):
        Option_Icon = QtGui.QIcon()
        if(tab == 1):
            self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)

            Option_Icon.addPixmap(QtGui.QPixmap(":/White_Icon/Icon_White/grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Control_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Parameter_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Setting_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/hard-drive.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Properties_btn.setIcon(Option_Icon)
                        
            self.Control_btn.setStyleSheet(Menu_btn_active)
            self.Parameter_btn.setStyleSheet(Menu_btn_idle)
            self.Setting_btn.setStyleSheet(Menu_btn_idle)
            self.Properties_btn.setStyleSheet(Menu_btn_idle)
            
            
        if(tab == 2):
            self.Top_stackedWidget.setCurrentWidget(self.Top_ParameterPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_ParameterPanel)

            Option_Icon.addPixmap(QtGui.QPixmap(":/White_Icon/Icon_White/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Parameter_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Control_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Setting_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/hard-drive.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Properties_btn.setIcon(Option_Icon)
                                           
            self.Control_btn.setStyleSheet(Menu_btn_idle)
            self.Parameter_btn.setStyleSheet(Menu_btn_active)
            self.Setting_btn.setStyleSheet(Menu_btn_idle)
            self.Properties_btn.setStyleSheet(Menu_btn_idle)         

            
        if(tab == 3):
            self.Top_stackedWidget.setCurrentWidget(self.Top_SettingPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
    
            Option_Icon.addPixmap(QtGui.QPixmap(":/White_Icon/Icon_White/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Setting_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Control_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Parameter_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/hard-drive.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Properties_btn.setIcon(Option_Icon)
                                                   
            self.Control_btn.setStyleSheet(Menu_btn_idle)
            self.Parameter_btn.setStyleSheet(Menu_btn_idle)
            self.Setting_btn.setStyleSheet(Menu_btn_active)
            self.Properties_btn.setStyleSheet(Menu_btn_idle)          

            
        if(tab == 4):
            self.Top_stackedWidget.setCurrentWidget(self.Top_PropertiesPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_SettingPanel)

            Option_Icon.addPixmap(QtGui.QPixmap(":/White_Icon/Icon_White/hard-drive.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Properties_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Control_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/bar-chart-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Parameter_btn.setIcon(Option_Icon)
            Option_Icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Setting_btn.setIcon(Option_Icon)
                                                                   
            self.Control_btn.setStyleSheet(Menu_btn_idle)
            self.Parameter_btn.setStyleSheet(Menu_btn_idle)
            self.Setting_btn.setStyleSheet(Menu_btn_idle)
            self.Properties_btn.setStyleSheet(Menu_btn_active)
            
       
    def Change_slogan(self):
        _translate = QtCore.QCoreApplication.translate
        slogan = self.lineEdit.text()
        self.Header_2.setText(_translate("MainWindow", slogan))
        
  
            
            
            
      