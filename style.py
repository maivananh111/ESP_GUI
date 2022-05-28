'''
Created on 14 thg 5, 2022
@author: A315-56
'''


 ################## MENU OPTION BUTTON ########################
Menu_btn_idle = ("QPushButton{\n" 
"    background-color: rgba(0, 0, 0, 0);"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));"
"}\n"
" QPushButton:hover{\n"
"    border: none;"
"    border-radius: 10px;"
"    padding-left: 10px;"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 192, 255, 255));"
"    color: rgb(255, 255, 255);"
"}\n QPushButton:pressed{\n" 
"    border: none;"
"    border-radius: 10px;"
"    padding-left: -2px;"
"    padding-top: -2px;"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(255, 60, 60, 255));"
"    color: rgb(255, 255, 255);"
 "}\n"
 "")

Menu_btn_active = ("QPushButton{\n" 
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 201, 0, 255), stop:1 rgba(25, 81, 36, 255));"
"    color: rgb(255, 255, 255);"
"    border-radius: 10px;"
"}\n"
"QPushButton:hover{\n" 
"    border: none;"
"    border-radius: 10px;"
"    padding-left: 5px;"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 192, 255, 255));"
"    color: rgb(255, 255, 255);"
"}\n"
"QPushButton:pressed{\n"
"    border: none;"
"    border-radius: 10px;"
"    padding-left: -5px;"
"    padding-top: -2px;"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(255, 60, 60, 255));"
"    color: rgb(255, 255, 255);"
"}\n"
"")

off_style = """QSlider::groove:horizotal{
    border: 1px solid rgb(156, 156, 156);
    color: rgb(0, 0, 255);
    height: 20px;
    width: 45px;
    border-radius: 10px;
    background-color: rgb(200, 200, 200);
    margin: 1px;
}
QSlider::handle:horizotal{
    border:  1px solid rgb(165, 165, 165);
    background-color: rgb(240, 240, 240);
    height: 30px;
    width: 30px;
    border-radius: 15px;
    margin: -5px;
}  """

on_style = """QSlider::groove:horizotal{
    border: 1px solid rgb(156, 156, 156);
    color: rgb(0, 0, 255);
    height: 20px;
    width: 45px;
    border-radius: 10px;
    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:1 rgba(0, 192, 255, 255));
    margin: 1px;
}
QSlider::handle:horizotal{
    border:  1px solid rgb(165, 165, 165);
    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(171, 171, 171, 255), stop:1 rgba(239, 239, 239, 255));
    height: 30px;
    width: 30px;
    border-radius: 15px;
    margin: -5px;
}   """  