


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

ComPort = ""
BaudRate = 0
Parity = 0
StopBit = 0
Databits = 0

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
    
    def serialOpen(self):

        try:
            self.serialPort.port = ComPort
            self.serialPort.baudrate = BaudRate
            self.serialPort.parity = Parity
            self.serialPort.stopbits = StopBit
            self.serialPort.open()
        except Exception as e:
            print("Open port send this exception %s:"%e)
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
        ComPort = self.choice6.GetStringSelection()
        print(ComPort)
        
    def choice2OnChoice( self, event ):
        BaudRate = int(self.choice2.GetStringSelection())
        print(BaudRate)
    
    def choice3OnChoice( self, event ):
        Parity = self.choice3.GetStringSelection()
        if Parity == 'None':
            Parity = 'N'
        elif Parity == 'Odd':
            Parity = 'O'
        else:
            Parity = 'E'
        print(Parity)
    
    def choice4OnChoice( self, event ):
        Databits = int(self.choice4.GetStringSelection())
        print(Databits)        
    
    def choice5OnChoice( self, event ):
        StopBit = int(self.choice5.GetStringSelection())
        print(StopBit)

    def m_button5OnButtonClick( self, event ):
        event.Skip()
            
        
        # Virtual event handlers, overide them in your derived class
    def button5OnButtonClick( self, event ):
        if self.serialPort.is_open == True:
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

    #fram.serialOpen()
    fram.Show(True)
    app.MainLoop()