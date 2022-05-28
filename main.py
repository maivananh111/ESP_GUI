#sử dụng run để chạy nhưngx trương trình muốn sử lý liên kết giữa các file với nhai

# from turtle import title thư viên đồ họa con rùa

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import*
from Login_Func import *
from Main_Func import *
import sys


class UI: 
    def __init__(self) :
        self.login_uic = QtWidgets.QMainWindow()
        self.login = Login_Main(self.login_uic)
        self.login_uic.show()
        self.login.EnterButton.clicked.connect(lambda: self.changeUI("Main_Panel")) #sử lý sự kiện cho nút login
        # từ login chuyển sang Main_Panel thì truyền trong cái self,.changUI một tham số muốn truyền qua
        # self.Main_Panel = MAIN()
        self.main_uic = QtWidgets.QMainWindow()
        self.main = Main_Screen(self.main_uic)
        self.main.Login_return.clicked.connect(lambda: self.changeUI("Login_Func"))

    def changeUI(self, i):
        if i == "Main_Panel": #nếu tham số truyền vào là Main_Panel thì Login_Func Main_Panel lên ẩn login đi
            User_scan = self.login.User.text()
            Password_scan = self.login.Password.text()
            _translate = QtCore.QCoreApplication.translate
            
            self.main.UserName = self.login.User.text()
            self.main.User_name.setText("%s"%self.main.UserName)
            
            if User_scan == "Đinh Thanh Tùng" and Password_scan == "20139096":
                self.login_uic.hide()
                self.main_uic.show()

            if User_scan == "Mai Văn Anh" and Password_scan == "20139059":
                self.login_uic.hide()
                self.main_uic.show()               

            if User_scan == "Trần Toàn Thắng" and Password_scan == "123456789":
                self.login_uic.hide()
                self.main_uic.show()               

            if User_scan == "Nguyễn Bá Quốc Tài" and Password_scan == "123456789":
                self.login_uic.hide()       
                self.main_uic.show()
                
            else :
                self.login.label_5.setText("Bạn nhập sai mật khẩu")
                self.login.label_5.setStyleSheet("color: rgba(255, 0, 0, 255);")
                

        elif i == "Login_Func":
            self.main_uic.hide()
            self.login_uic.show()
    # LOGIN 



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()    
    app.exec_()

