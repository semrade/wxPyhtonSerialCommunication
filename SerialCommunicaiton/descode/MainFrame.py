# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.animate
import wx.grid
import wx.richtext
import wx.aui

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Serial Communication Interface", pos = wx.DefaultPosition, size = wx.Size( 910,774 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Serial Port Connection" ), wx.HORIZONTAL )
		
		self.m_button5 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetDefault() 
		self.m_button5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer1.Add( self.m_button5, 0, wx.ALL, 10 )
		
		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Port :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		sbSizer1.Add( self.m_staticText10, 0, wx.ALL, 10 )
		
		m_choice6Choices = []
		self.m_choice6 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		sbSizer1.Add( self.m_choice6, 0, wx.ALL, 10 )
		
		self.m_staticText5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BaudRate :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		sbSizer1.Add( self.m_staticText5, 0, wx.ALL, 10 )
		
		m_choice2Choices = [ u"110", u"300", u"600", u"1200", u"2400", u"4800", u"9600", u"14400", u"19200", u"38400", u"57600", u"115200", u"128000", u"256000" ]
		self.m_choice2 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		sbSizer1.Add( self.m_choice2, 0, wx.ALL, 10 )
		
		self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Parity :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		sbSizer1.Add( self.m_staticText7, 0, wx.ALL, 10 )
		
		m_choice3Choices = [ u"Odd", u"Even", u"None" ]
		self.m_choice3 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 1 )
		sbSizer1.Add( self.m_choice3, 0, wx.ALL, 10 )
		
		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Data Bits :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		sbSizer1.Add( self.m_staticText6, 0, wx.ALL, 10 )
		
		m_choice4Choices = [ u"7", u"8" ]
		self.m_choice4 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		sbSizer1.Add( self.m_choice4, 0, wx.ALL, 10 )
		
		self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Sotp Bits :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		sbSizer1.Add( self.m_staticText9, 0, wx.ALL, 10 )
		
		m_choice5Choices = [ u"1", u"2" ]
		self.m_choice5 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		sbSizer1.Add( self.m_choice5, 0, wx.ALL, 10 )
		
		self.m_animCtrl1 = wx.animate.AnimationCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.Size( 45,45 ), wx.animate.AC_DEFAULT_STYLE ) 
		sbSizer1.Add( self.m_animCtrl1, 0, wx.ALL, 0 )
		
		
		bSizer11.Add( sbSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer11, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.m_staticline3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer18, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Command Management" ), wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Rows +/- :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		sbSizer2.Add( self.m_staticText11, 0, wx.ALL, 10 )
		
		self.m_button4 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delete (-)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.SetDefault() 
		sbSizer2.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button51 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Add(+)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button51, 0, wx.ALL, 5 )
		
		self.m_staticline31 = wx.StaticLine( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer2.Add( self.m_staticline31, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Colos +/- :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		sbSizer2.Add( self.m_staticText12, 0, wx.ALL, 10 )
		
		self.m_button6 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delete (-)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetDefault() 
		sbSizer2.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Add (+)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer2.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Graphe + :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		sbSizer2.Add( self.m_staticText13, 0, wx.ALL, 10 )
		
		self.m_button9 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Add (+)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button9, 0, wx.ALL, 5 )
		
		self.m_staticline41 = wx.StaticLine( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer2.Add( self.m_staticline41, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		sbSizer2.Add( self.m_staticText91, 0, wx.ALL, 10 )
		
		self.m_button71 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Save Sheet", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button71, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( sbSizer2, 1, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer19, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Frames" ), wx.VERTICAL )
		
		self.m_grid3 = wx.grid.Grid( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 5, 20 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.m_grid3.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer3.Add( self.m_grid3, 1, wx.ALIGN_TOP|wx.ALL|wx.BOTTOM|wx.EXPAND, 0 )
		
		
		bSizer20.Add( sbSizer3, 1, 0, 0 )
		
		
		bSizer7.Add( bSizer20, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Text Rich Box" ), wx.VERTICAL )
		
		self.m_richText2 = wx.richtext.RichTextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		sbSizer4.Add( self.m_richText2, 1, wx.EXPAND, 5 )
		
		
		bSizer111.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer111, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Py Graph" ), wx.HORIZONTAL )
		
		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_auinotebook1 = wx.aui.AuiNotebook( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer113.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		sbSizer5.Add( bSizer113, 1, wx.EXPAND, 0 )
		
		
		bSizer112.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer112, 1, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer7, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panel1.SetSizer( bSizer6 )
		self.m_panel1.Layout()
		bSizer6.Fit( self.m_panel1 )
		bSizer5.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer3.Add( bSizer5, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.m_menuItem1 )
		
		self.m_menu11.AppendSeparator()
		
		self.m_menu3.AppendSubMenu( self.m_menu11, u"MyMenu" )
		
		self.m_menubar1.Append( self.m_menu3, u"View" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick )
		self.m_choice6.Bind( wx.EVT_CHOICE, self.m_choice6OnChoice )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.m_choice2OnChoice )
		self.m_choice3.Bind( wx.EVT_CHOICE, self.m_choice3OnChoice )
		self.m_choice4.Bind( wx.EVT_CHOICE, self.m_choice4OnChoice )
		self.m_choice5.Bind( wx.EVT_CHOICE, self.m_choice5OnChoice )
		self.m_button4.Bind( wx.EVT_BUTTON, self.m_button4OnButtonClick )
		self.m_button51.Bind( wx.EVT_BUTTON, self.m_button51OnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.m_button6OnButtonClick )
		self.m_button7.Bind( wx.EVT_BUTTON, self.m_button7OnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.m_button9OnButtonClick )
		self.m_button71.Bind( wx.EVT_BUTTON, self.m_button71OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button5OnButtonClick( self, event ):
		event.Skip()
	
	def m_choice6OnChoice( self, event ):
		event.Skip()
	
	def m_choice2OnChoice( self, event ):
		event.Skip()
	
	def m_choice3OnChoice( self, event ):
		event.Skip()
	
	def m_choice4OnChoice( self, event ):
		event.Skip()
	
	def m_choice5OnChoice( self, event ):
		event.Skip()
	
	def m_button4OnButtonClick( self, event ):
		event.Skip()
	
	def m_button51OnButtonClick( self, event ):
		event.Skip()
	
	def m_button6OnButtonClick( self, event ):
		event.Skip()
	
	def m_button7OnButtonClick( self, event ):
		event.Skip()
	
	def m_button9OnButtonClick( self, event ):
		event.Skip()
	
	def m_button71OnButtonClick( self, event ):
		event.Skip()
	

