# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid
import wx.richtext
import wx.aui

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Serial Communication Interface", pos = wx.DefaultPosition, size = wx.Size( 910,774 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.panel1, wx.ID_ANY, u"Serial Port Connection" ), wx.HORIZONTAL )
		
		self.button5 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.button5, 0, wx.ALL, 10 )
		
		self.staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Port :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText10.Wrap( -1 )
		sbSizer1.Add( self.staticText10, 0, wx.ALL, 10 )
		
		choice6Choices = []
		self.choice6 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice6Choices, 0 )
		self.choice6.SetSelection( 0 )
		sbSizer1.Add( self.choice6, 0, wx.ALL, 10 )
		
		self.staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BaudRate :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText5.Wrap( -1 )
		sbSizer1.Add( self.staticText5, 0, wx.ALL, 10 )
		
		choice2Choices = [ u"110", u"300", u"600", u"1200", u"2400", u"4800", u"9600", u"14400", u"19200", u"38400", u"57600", u"115200", u"128000", u"256000" ]
		self.choice2 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice2Choices, 0 )
		self.choice2.SetSelection( 0 )
		sbSizer1.Add( self.choice2, 0, wx.ALL, 10 )
		
		self.staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Parity :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText7.Wrap( -1 )
		sbSizer1.Add( self.staticText7, 0, wx.ALL, 10 )
		
		choice3Choices = [ u"Odd", u"Even", u"None" ]
		self.choice3 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice3Choices, 0 )
		self.choice3.SetSelection( 1 )
		sbSizer1.Add( self.choice3, 0, wx.ALL, 10 )
		
		self.staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Data Bits :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText6.Wrap( -1 )
		sbSizer1.Add( self.staticText6, 0, wx.ALL, 10 )
		
		choice4Choices = [ u"7", u"8" ]
		self.choice4 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice4Choices, 0 )
		self.choice4.SetSelection( 0 )
		sbSizer1.Add( self.choice4, 0, wx.ALL, 10 )
		
		self.staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Sotp Bits :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText9.Wrap( -1 )
		sbSizer1.Add( self.staticText9, 0, wx.ALL, 10 )
		
		choice5Choices = [ u"1", u"2" ]
		self.choice5 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice5Choices, 0 )
		self.choice5.SetSelection( 0 )
		sbSizer1.Add( self.choice5, 0, wx.ALL, 10 )
		
		self.animCtrl1 = wx.adv.AnimationCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 45,45 ), wx.adv.AC_DEFAULT_STYLE ) 
		sbSizer1.Add( self.animCtrl1, 0, wx.ALL, 0 )
		
		
		bSizer11.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer11, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.staticline3 = wx.StaticLine( self.panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.staticline3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer18, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.panel1, wx.ID_ANY, u"Command Management" ), wx.HORIZONTAL )
		
		self.staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Rows +/- :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText11.Wrap( -1 )
		sbSizer2.Add( self.staticText11, 0, wx.ALL, 10 )
		
		self.button4 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delete (-)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.button4, 0, wx.ALL, 5 )
		
		self.button51 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Add(+)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.button51, 0, wx.ALL, 5 )
		
		self.staticline31 = wx.StaticLine( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer2.Add( self.staticline31, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Colos +/- :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText12.Wrap( -1 )
		sbSizer2.Add( self.staticText12, 0, wx.ALL, 10 )
		
		self.button6 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delete (-)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.button6, 0, wx.ALL, 5 )
		
		self.button7 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Add (+)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.button7, 0, wx.ALL, 5 )
		
		self.staticline4 = wx.StaticLine( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer2.Add( self.staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText13 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Graphe +/- :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText13.Wrap( -1 )
		sbSizer2.Add( self.staticText13, 0, wx.ALL, 10 )
		
		self.button8 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delete (-)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.button8, 0, wx.ALL, 5 )
		
		self.button9 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Add (+)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.button9, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( sbSizer2, 1, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer19, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.panel1, wx.ID_ANY, u"Frames" ), wx.VERTICAL )
		
		self.grid3 = wx.grid.Grid( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), 0 )
		
		# Grid
		self.grid3.CreateGrid( 5, 20 )
		self.grid3.EnableEditing( True )
		self.grid3.EnableGridLines( True )
		self.grid3.EnableDragGridSize( False )
		self.grid3.SetMargins( 0, 0 )
		
		# Columns
		self.grid3.EnableDragColMove( False )
		self.grid3.EnableDragColSize( True )
		self.grid3.SetColLabelSize( 30 )
		self.grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		
		# Rows
		self.grid3.EnableDragRowSize( True )
		self.grid3.SetRowLabelSize( 80 )
		self.grid3.SetRowLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.grid3.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		# Cell Defaults
		self.grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer3.Add( self.grid3, 1, wx.ALIGN_TOP|wx.ALL|wx.BOTTOM|wx.EXPAND, 0 )
		
		
		bSizer20.Add( sbSizer3, 1, 0, 0 )
		
		
		bSizer7.Add( bSizer20, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.panel1, wx.ID_ANY, u"Text Rich Box" ), wx.VERTICAL )
		
		self.richText2 = wx.richtext.RichTextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		sbSizer4.Add( self.richText2, 1, wx.EXPAND, 5 )
		
		
		bSizer111.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer111, 1, wx.ALL|wx.EXPAND, 0 )
		
		bSizer112 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.panel1, wx.ID_ANY, u"Py Graph" ), wx.HORIZONTAL )
		
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		self.auinotebook1 = wx.aui.AuiNotebook( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer113.Add( self.auinotebook1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		sbSizer5.Add( bSizer113, 1, wx.EXPAND, 0 )
		
		
		bSizer112.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		bSizer7.Add( bSizer112, 1, wx.EXPAND, 0 )
		
		
		bSizer6.Add( bSizer7, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.panel1.SetSizer( bSizer6 )
		self.panel1.Layout()
		bSizer6.Fit( self.panel1 )
		bSizer5.Add( self.panel1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer3.Add( bSizer5, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.menubar1 = wx.MenuBar( 0 )
		self.menu1 = wx.Menu()
		self.menubar1.Append( self.menu1, u"File" ) 
		
		self.menu2 = wx.Menu()
		self.menubar1.Append( self.menu2, u"Edit" ) 
		
		self.menu3 = wx.Menu()
		self.menu11 = wx.Menu()
		self.menuItem1 = wx.MenuItem( self.menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu11.Append( self.menuItem1 )
		
		self.menu11.AppendSeparator()
		
		self.menu3.AppendSubMenu( self.menu11, u"MyMenu" )
		
		self.menubar1.Append( self.menu3, u"View" ) 
		
		self.SetMenuBar( self.menubar1 )
		
		self.statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button5.Bind( wx.EVT_BUTTON, self.button5OnButtonClick )
		self.choice6.Bind( wx.EVT_CHOICE, self.choice6OnChoice )
		self.choice2.Bind( wx.EVT_CHOICE, self.choice2OnChoice )
		self.choice3.Bind( wx.EVT_CHOICE, self.choice3OnChoice )
		self.choice4.Bind( wx.EVT_CHOICE, self.choice4OnChoice )
		self.choice5.Bind( wx.EVT_CHOICE, self.choice5OnChoice )
		self.button4.Bind( wx.EVT_BUTTON, self.button4OnButtonClick )
		self.button51.Bind( wx.EVT_BUTTON, self.button51OnButtonClick )
		self.button6.Bind( wx.EVT_BUTTON, self.button6OnButtonClick )
		self.button7.Bind( wx.EVT_BUTTON, self.button7OnButtonClick )
		self.button8.Bind( wx.EVT_BUTTON, self.button8OnButtonClick )
		self.button9.Bind( wx.EVT_BUTTON, self.button9OnButtonClick )
	
	def __del__( self ):
		pass
	
	

	

