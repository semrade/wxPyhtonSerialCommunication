


from MainFrame import *
import serial
import sys
import wx.lib.plot as plot
import serial.tools.list_ports
import random
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

class MainApp(MyFrame2):
    def __init__(self):
        MyFrame2.__init__(self, None)
        self.serialPort = serial.Serial()
        self.pageCounter = 0
    
    def serialOpen(self):

        try:
            #serialPort = serial.Serial(ComPort, BaudRate, Databits, Parity, StopBit, timeout = None, xonxoff=0, rtscts=0)
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
    
    def m_choice6OnChoice( self, event ):
        ComPort = self.m_choice6.GetStringSelection()
        print(ComPort)
        
    def m_choice2OnChoice( self, event ):
        BaudRate = int(self.m_choice2.GetStringSelection())
        print(BaudRate)
    
    def m_choice3OnChoice( self, event ):
        Parity = self.m_choice3.GetStringSelection()
        if Parity == 'None':
            Parity = 'N'
        elif Parity == 'Odd':
            Parity = 'O'
        else:
            Parity = 'E'
        print(Parity)
    
    def m_choice4OnChoice( self, event ):
        Databits = int(self.m_choice4.GetStringSelection())
        print(Databits)        
    
    def m_choice5OnChoice( self, event ):
        StopBit = int(self.m_choice5.GetStringSelection())
        print(StopBit)

    def m_button5OnButtonClick( self, event ):
        if self.serialPort.is_open == True:
            self.serialPort.close()
            self.m_button5.SetBackgroundColour("Red")
            self.m_button5.SetLabel("Open")
        else:
            self.serialOpen()
            self.m_button5.SetBackgroundColour("Green")
            self.m_button5.SetLabel("Close")

    def m_button10OnButtonClick( self, event ):
        self.m_grid3.DeleteRows(numRows=1, updateLabels=True)
    
    def m_button9OnButtonClick( self, event ):
        self.m_grid3.AppendRows(numRows=1, updateLabels=True)     
        
    
    def addPage(self):
        self.pageCounter += 1
        page      = Page(self.m_notebook1)
        pageTitle = "Page: {0}".format(str(self.pageCounter))
        self.m_notebook1.AddPage(page, pageTitle)

    def onButtonRemove(self, event):   
        self.m_notebook1.DeletePage(0) 

if __name__ == "__main__":

    app = wx.App()
    fram = MainApp() 
    port = fram.listPort()
    # initialize the colors items
    
    
    for portElem in port:
        fram.m_choice6.AppendItems(portElem)  

    fram.addPage()
    fram.addPage()
    #fram.serialOpen()
    fram.Show(True)
    app.MainLoop()