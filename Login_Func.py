
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

os.system("pyuic5 -x Login_Scr.ui -o Login_Scr.py")

from Login_Scr import *

class Login_Main(Ui_MainWindow):
    show_mode = False
    def __init__(self, mainwindow):
        # QMainWindow.__init__(self)
        self.setupUi(mainwindow)
        mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        mainwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(lambda: self.close())
        self.BoxButton.clicked.connect(lambda: self.BoxButton_Show())
        self.eye.clicked.connect(lambda: self.eye_click())
        
        self.close_button.clicked.connect(lambda: self.close())
        self.EnterButton.clicked.connect(lambda: self.scan_password())
        
        self.Create_account.clicked.connect(lambda: self.Create_acc())
        self.forgot_password.clicked.connect(lambda: self.Forgot_pass())
        self.comboboxx()

    def comboboxx(self):
        self.comboBox.currentTextChanged.connect(self.laygiatri)

    def  laygiatri(self):
        self.User.setText(self.comboBox.currentText())

    def close(self):
        sys.exit()

    def BoxButton_Show(self):
        self.comboBox.showPopup()

    def scan_password(self):
        User_scan = self.User.text()
        Password_scan = self.Password.text()
        
    def Create_acc(self):
        self.label_5.setText("Sẽ xuất hiện vào năm 2024.")
        self.label_5.setStyleSheet("color: rgba(255, 0, 0, 255);")
        
    def Forgot_pass(self):
        self.label_5.setText("Quên thì thôi, khỏi sài.")
        self.label_5.setStyleSheet("color: rgba(255, 0, 0, 255);")
                
    def eye_click(self):
        eye_icon = QtGui.QIcon()
        if self.show_mode == False:
            self.show_mode = True
            self.Password.setEchoMode(QtWidgets.QLineEdit.Normal)
            eye_icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/eye-off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.eye.setIcon(eye_icon)
        else :
            self.show_mode = False
            self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
            eye_icon.addPixmap(QtGui.QPixmap(":/Green_Icon/Icon_Green/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.eye.setIcon(eye_icon)
            
            
            
            
            
            
            
            
            
            
            