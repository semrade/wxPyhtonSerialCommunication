


from MainFrame import *
import serial
import sys
import wx.lib.plot as plot
import serial.tools.list_ports
import random
import matplotlib as mpl
from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)
from Cleaner import *
from cmath import cos, sin
import json




class Page(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "THIS IS A PAGE OBJECT", (20,20))
        colors = ["red", "blue", "gray", "yellow", "green"]
        self.SetBackgroundColour(random.choice(colors))

class Plot(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)
        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(1, 1))
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT|wx.ALL | wx.EXPAND)
        self.SetSizer(sizer)

class MainApp(MyFrame2):
    def __init__(self):
        MyFrame2.__init__(self, None)
        self.serialPort = serial.Serial()
        self.GraphCounter = 0
        # Default parameters for serial port
        self.ComPort = "COM12" 
        self.BaudRate = 115200 
        self.Databit = 8
        self.Parity = 'N' 
        self.StopBit = 1
    
    def serialOpen(self):

        try:
            self.serialPort.port = self.ComPort
            self.serialPort.baudrate = self.BaudRate
            self.serialPort.bytesize = self.Databit
            self.serialPort.parity = self.Parity
            self.serialPort.stopbits = self.StopBit
            self.serialPort.open()
            self.richText2.AppendText("Port COM is = {}, Speed baudrate = {}, bits data = {}, parity = {}, stop bit = {}, \n".format(
                self.ComPort,self.BaudRate,self.Databit,self.Parity,self.StopBit))
        except Exception as e:
            print("Open port send this exception :%s" %e)
        else:
            pass
        finally:
            pass
        
        return True
    
    def serialClose(self):
        pass
    
    def listPort(self):
        ports = serial.tools.list_ports.comports()
        print("--------------Serial ports---------------")
        AppPorts = []
        for port, desc, hwid in sorted(ports):
            print("{}: {}".format(port, desc))
            AppPorts.append(port)
        print("--------------Serial ports---------------")
        return AppPorts
    
    def choice6OnChoice( self, event ):
        self.ComPort = self.choice6.GetStringSelection()
        print(self.ComPort)
        
    def choice2OnChoice( self, event ):
        self.BaudRate = int(self.choice2.GetStringSelection())
        self.choice2.Set_d
        print(self.BaudRate)
    
    def choice3OnChoice( self, event ):
        self.Parity = self.choice3.GetStringSelection()
        if self.Parity == 'None':
            self.Parity = 'N'
        elif self.Parity == 'Odd':
            self.Parity = 'O'
        elif self.Parity == 'Even':
            self.Parity = "E"
        print(self.Parity)
    
    def choice4OnChoice( self, event ):
        self.Databit = int(self.choice4.GetStringSelection())
        print(self.Databit)        
    
    def choice5OnChoice( self, event ):
        self.StopBit = int(self.choice5.GetStringSelection())
        print(self.StopBit)

    def m_button5OnButtonClick( self, event ):
        event.Skip()
            
        
        # Virtual event handlers, overide them in your derived class
    def button5OnButtonClick( self, event ):
        if self.serialPort.isOpen() == True:
            self.serialPort.close()
            self.button5.SetBackgroundColour("Red")
            self.button5.SetLabel("Open")

        else:
            self.serialOpen()
            self.button5.SetBackgroundColour("Green")
            self.button5.SetLabel("Close")

    
    def button4OnButtonClick( self, event ):
        self.grid3.DeleteRows(numRows=1, updateLabels=True)
         
    def button51OnButtonClick( self, event ):
        self.grid3.AppendRows(numRows=1, updateLabels=True)
    
    def button6OnButtonClick( self, event ):
        event.Skip()
    
    def button7OnButtonClick( self, event ):
        event.Skip()
    
    def button8OnButtonClick( self, event ):
        event.Skip()
    
    def button9OnButtonClick( self, event ):
        self.add()

    
    def add(self):
        page = Plot(self.auinotebook1)
        self.GraphCounter += 1
        pageTitle = "Graphe: {0}".format(str(self.GraphCounter))
        self.auinotebook1.AddPage(page, pageTitle)
        return page.figure

    def onButtonRemove(self, event):   
        self.notebook1.DeletePage(0) 

    def ReadJsonFile(self):
        Row = 0
        Clo = 0
        dir_main = os.path.dirname(__file__)
        ptr = open(os.path.join(dir_main,"..\\Data\\data.js"),'r')
        json_file = ptr.read()
        ptr.close()
        print(json_file)
        data = json.loads(json_file)
        # print the keys and values

        for key in data:
            #value = data[key]
            #print("The key and value are ({}) = ({})".format(key, value))
            print("The keys are ({}) and the data are ({}) ".format(key,data[key]))
            """
            self.grid3.SetCellValue(Row,Clo,key)
            Clo += 1
            print(data[key][0])
            
            for ele in data[key][0]:
                self.grid3.SetCellValue(Row,Clo,ele)
                Clo += 1
                self.grid3.SetCellValue(Row,Clo,data[key]["I_Phase 1"])
                Clo += 1
            
            
                for item in data[key]:
                    self.grid3.SetCellValue(Row,Clo,item)
                    Clo += 1
            
            """
            Clo = 0
            Row += 1  

if __name__ == "__main__":

    app = wx.App()
    fram = MainApp() 
    port = fram.listPort()
    # initialize the colors items
    
    
    for portElem in port:
        fram.choice6.AppendItems(portElem)  
        
    x1 = list(range(1, 1000))
    y1 = [cos(int(i)) for i in x1]
    plotter = fram.auinotebook1
    axes1 = fram.add().gca()
    axes1.plot(x1, y1)
    
    x1 = list(range(1, 1000))
    y1 = [sin(int(i)) for i in x1]
    
    axes2 = fram.add().gca()
    axes2.plot(x1, y1)

    #read json file
    fram.ReadJsonFile()
    #fram.serialOpen()
    fram.Show(True)
    app.MainLoop()