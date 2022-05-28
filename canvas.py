from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
#pip install openpyxl
#pip3 install xlrd

xl = pd.ExcelFile('D:/ECLIPSE/ESP_GUI/chart.xlsx')
df = pd.read_excel(xl, 0, header=None)


class Canvas_grafica(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khá»Ÿi táº¡o 1 subplots API hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng Ä‘á»ƒ váº» cÃ¡c Ä‘á»“ thá»‹ phá»©c táº¡o, figsize tÃ¹y chá»‰nh Ä‘á»™ dÃ i rá»™ng cá»§a Ä‘á»“ thá»‹ fig lÃ  hÃ¬nh lá»›n tá»•ng cÃ²n ax lÃ  cÃ¡c hÃ¬nh nhá»� Ä‘c váº» lÃªn
        super().__init__(self.fig)
        self.a = []
        self.data = df.head(1)
        for i in self.data:
            self.a.append(self.data[i])

        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem lÃ  chiá»�u ngang

        self.ram = self.data # ram lÃ  chiá»�u dá»�c
        self.i = self.ram[0]
        self.ram.pop(7) # xÃ³a 1 pháº§n tá»­ trong list

        # self.fig.suptitle("REM", size = 9) #Ä‘áº·t tÃªn cho hÃ¬nh chÃ­nh

        self.ax.plot(self.rem, self.a, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)

class Canvas_grafica_1(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khá»Ÿi táº¡o 1 subplots API hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng Ä‘á»ƒ váº» cÃ¡c Ä‘á»“ thá»‹ phá»©c táº¡o, figsize tÃ¹y chá»‰nh Ä‘á»™ dÃ i rá»™ng cá»§a Ä‘á»“ thá»‹ fig lÃ  hÃ¬nh lá»›n tá»•ng cÃ²n ax lÃ  cÃ¡c hÃ¬nh nhá»� Ä‘c váº» lÃªn
        super().__init__(self.fig)
        self.a = []
        self.data = df.head(1)
        for i in self.data:
            self.a.append(self.data[i])

        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem lÃ  chiá»�u ngang

        self.ram = self.data # ram lÃ  chiá»�u dá»�c
        self.i = self.ram[0]
        self.ram.pop(7) # xÃ³a 1 pháº§n tá»­ trong list

        # self.fig.suptitle("REM", size = 9) #Ä‘áº·t tÃªn cho hÃ¬nh chÃ­nh

        self.ax.plot(self.rem, self.a, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)

class Canvas_grafica_2(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khá»Ÿi táº¡o 1 subplots API hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng Ä‘á»ƒ váº» cÃ¡c Ä‘á»“ thá»‹ phá»©c táº¡o, figsize tÃ¹y chá»‰nh Ä‘á»™ dÃ i rá»™ng cá»§a Ä‘á»“ thá»‹ fig lÃ  hÃ¬nh lá»›n tá»•ng cÃ²n ax lÃ  cÃ¡c hÃ¬nh nhá»� Ä‘c váº» lÃªn
        super().__init__(self.fig)
        self.a = []
        self.data = df.head(1)
        for i in self.data:
            self.a.append(self.data[i])

        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem lÃ  chiá»�u ngang

        self.ram = self.data # ram lÃ  chiá»�u dá»�c
        self.i = self.ram[0]
        self.ram.pop(7) # xÃ³a 1 pháº§n tá»­ trong list

        # self.fig.suptitle("REM", size = 9) #Ä‘áº·t tÃªn cho hÃ¬nh chÃ­nh

        self.ax.plot(self.rem, self.a, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)

class Canvas_grafica_3(FigureCanvas) :
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(1, 1), 
            sharey=True, facecolor='white') #khá»Ÿi táº¡o 1 subplots API hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng Ä‘á»ƒ váº» cÃ¡c Ä‘á»“ thá»‹ phá»©c táº¡o, figsize tÃ¹y chá»‰nh Ä‘á»™ dÃ i rá»™ng cá»§a Ä‘á»“ thá»‹ fig lÃ  hÃ¬nh lá»›n tá»•ng cÃ²n ax lÃ  cÃ¡c hÃ¬nh nhá»� Ä‘c váº» lÃªn
        super().__init__(self.fig)
        self.rem = [1, 2, 3, 4, 5, 6, 7, 8] # rem lÃ  chiá»�u ngang 
        self.ram = [15, 15, 30, 1, 5, 53, 10, 12] # ram lÃ  chiá»�u dá»�c
        self.i = self.ram[0]
        self.ram.insert(0, self.i) # chÃ¨n 1 pháº§n tá»­ vÃ o list
        self.ram.pop(7) # xÃ³a 1 pháº§n tá»­ trong list

        self.fig.suptitle("REM", size = 9) #Ä‘áº·t tÃªn cho hÃ¬nh chÃ­nh

        self.ax.plot(self.rem, self.ram, marker = ".", markersize = 20)
        # self.ax.plot(rem, ram)