# -*- coding: utf-8 -*-
import sys,os
from PyQt4 import QtGui,QtCore
import playerdone
import navigator
import albumItemListWidget
import songItemListWidget
import cache1
import stack
import JBlistWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



class Main(QtGui.QGraphicsView):
	
        state = 1
         
        def __init__(self):
		super(QtGui.QGraphicsView,self).__init__()
		self.initUi()

	def initUi(self):
		self.showMaximized()
		self.screen = QtGui.QApplication.desktop()
		self.width = self.screen.width()
		self.height = self.screen.height()
		self.graphicsscene = QtGui.QGraphicsScene(self)
		self.bg = QtGui.QPixmap("/home/nikhcc/mp3.jpg")
		self.bgbrush = QtGui.QBrush(self.bg)
		self.graphicsscene.setSceneRect(0,0,self.width-50,self.height-60)
		self.setBackgroundBrush(self.bgbrush)
		#self.k = [1,3]
		self.artistScrolLevel = 0
		self.genreScrolLevel = 0
		self.albumScrolLevel = 0
		self.songScrolLevel = 0
                self.artistlistopen = False
                self.genrelistopen  = False
                self.songlistopen   = False
                self.listslotvalidity  = True
		self.albumlistopen = True
		self.cache = cache1.cache() 
   		self.albumlist = self.cache.getAlbumItemList(None,None,'')
                self.songlist = self.cache.getSongItemList(" ","")
   		li = [('kio','lop'),('kol','koi')]
		self.albumGrid = albumItemListWidget.albumItemListWidget(self.albumlist)
                self.songGrid = songItemListWidget.songItemListWidget(self.songlist)
                
                self.albumGrid.selected.connect(self.albumslot)
                
                self.JBListItem = JBlistWidget.JBlist(["hui"])

                self.player = playerdone.PlayerWidget()
		
                self.navigator = navigator.navi()
                
                self.artistButton =  QtGui.QPushButton('                       ')
		self.artistButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
                self.genreButton =  QtGui.QPushButton('                       ')
		self.genreButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
                self.scanButton =  QtGui.QPushButton('                       ')
		self.scanButton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
                self.stack = stack.stackBar()                 

		self.albumGrid.updatelist(self.albumlist)
		self.nbutton = QtGui.QPushButton('                       ')
		self.nbutton.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
		self.graphicsscene.addWidget(self.player)
		self.graphicsscene.addWidget(self.navigator)
		self.graphicsscene.addWidget(self.nbutton)
		self.graphicsscene.addWidget(self.albumGrid)
		self.graphicsscene.addWidget(self.songGrid)
		self.graphicsscene.addWidget(self.JBListItem)
		self.graphicsscene.addWidget(self.artistButton)
		self.graphicsscene.addWidget(self.stack)
		self.graphicsscene.addWidget(self.genreButton)
		self.graphicsscene.addWidget(self.scanButton)
		self.setupStateMachine()
	
	def setupStateMachine(self):
		self.machine = QtCore.QStateMachine()
		state_initial_wp = QtCore.QState(self.machine)
		state_initial_wop = QtCore.QState(self.machine)
		state_inter_wp = QtCore.QState(self.machine)
		state_inter_wop = QtCore.QState(self.machine)
		state_final_wp = QtCore.QState(self.machine)
		state_final_wop = QtCore.QState(self.machine)
		
                self.connect(state_initial_wop ,QtCore.SIGNAL('propertiesAssigned ()'),self.getStateSlot1)
		self.connect(state_initial_wp ,QtCore.SIGNAL('propertiesAssigned ()'),self.getStateSlot2)
		self.connect(state_inter_wop ,QtCore.SIGNAL('propertiesAssigned ()'),self.getStateSlot3)
		self.connect(state_inter_wp ,QtCore.SIGNAL('propertiesAssigned ()'),self.getStateSlot4)
		self.connect(state_final_wop ,QtCore.SIGNAL('propertiesAssigned ()'),self.getStateSlot5)
		self.connect(state_final_wp ,QtCore.SIGNAL('propertiesAssigned ()'),self.getStateSlot6)


          #initial state with player
                state_initial_wop.assignProperty(self,"state",2)
		state_initial_wp.assignProperty(self.nbutton,"text","Hide Player")
		state_initial_wp.assignProperty(self.artistButton,"text","Artist")
		state_initial_wp.assignProperty(self.genreButton,"text","Genre")
		state_initial_wp.assignProperty(self.scanButton,"text","Scan")
		state_initial_wp.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),0,400,50))
		state_initial_wp.assignProperty(self.nbutton,"pos",QtCore.QPoint(0,5))
		state_initial_wp.assignProperty(self.artistButton,"pos",QtCore.QPoint(0,50))
		state_initial_wp.assignProperty(self.genreButton,"pos",QtCore.QPoint(0,95))
		state_initial_wp.assignProperty(self.scanButton,"pos",QtCore.QPoint(0,140))
		state_initial_wp.assignProperty(self.stack,"geometry",QtCore.QRect(0,250,225,450))	
		state_initial_wp.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		state_initial_wp.assignProperty(self.player,"opacity",1.0)
		state_initial_wp.assignProperty(self.nbutton,"opacity",1.0)
		state_initial_wp.assignProperty(self.navigator,"opacity",1.0)
		state_initial_wp.assignProperty(self.albumGrid,"opacity",1.0)
		state_initial_wp.assignProperty(self.albumGrid,"visible",1.0)
		state_initial_wp.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,300,750,400))
		state_initial_wp.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wp.assignProperty(self.songGrid,"visible",0.0)
		state_initial_wp.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wp.assignProperty(self.JBListItem,"visible",0.0)

         #initial state without player
                state_initial_wop.assignProperty(self,"state",2)
		state_initial_wop.assignProperty(self.nbutton,"text","Show Player")
		state_initial_wop.assignProperty(self.artistButton,"text","Artist")
		state_initial_wop.assignProperty(self.genreButton,"text","Genre")
		state_initial_wop.assignProperty(self.scanButton,"text","Scan")
		state_initial_wop.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		state_initial_wop.assignProperty(self.nbutton,"pos",QtCore.QPoint(0,5))
		state_initial_wop.assignProperty(self.artistButton,"pos",QtCore.QPoint(0,50))
		state_initial_wop.assignProperty(self.genreButton,"pos",QtCore.QPoint(0,95))
		state_initial_wop.assignProperty(self.scanButton,"pos",QtCore.QPoint(0,140))
		state_initial_wop.assignProperty(self.stack,"geometry",QtCore.QRect(0,250,225,450))	
		state_initial_wop.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),-400,400,150))
		state_initial_wop.assignProperty(self.player,"opacity",0.0)
		state_initial_wop.assignProperty(self.nbutton,"opacity",1.0)
		state_initial_wop.assignProperty(self.navigator,"opacity",1.0)
		state_initial_wop.assignProperty(self.albumGrid,"opacity",1.0)
		state_initial_wop.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wop.assignProperty(self.albumGrid,"visible",1.0)
		state_initial_wop.assignProperty(self.songGrid,"opacity",0.0)
		state_initial_wop.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wop.assignProperty(self.songGrid,"visible",0.0)
		state_initial_wop.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wop.assignProperty(self.JBListItem,"visible",0.0)
		
         #intermediate state with player
                state_initial_wop.assignProperty(self,"state",2)
		state_inter_wp.assignProperty(self.nbutton,"text","Hide Player")
		state_inter_wp.assignProperty(self.artistButton,"text","Artist")
		state_inter_wp.assignProperty(self.genreButton,"text","Genre")
		state_inter_wp.assignProperty(self.scanButton,"text","Scan")
		state_inter_wp.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),0,400,50))
		state_inter_wp.assignProperty(self.nbutton,"pos",QtCore.QPoint(0,5))
		state_inter_wp.assignProperty(self.artistButton,"pos",QtCore.QPoint(0,50))
		state_inter_wp.assignProperty(self.genreButton,"pos",QtCore.QPoint(0,95))
		state_inter_wp.assignProperty(self.scanButton,"pos",QtCore.QPoint(0,140))
		state_inter_wp.assignProperty(self.stack,"geometry",QtCore.QRect(0,250,225,450))	
		state_inter_wp.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		state_inter_wp.assignProperty(self.player,"opacity",1.0)
		state_inter_wp.assignProperty(self.nbutton,"opacity",1.0)
		state_inter_wp.assignProperty(self.navigator,"opacity",1.0)
		state_inter_wp.assignProperty(self.albumGrid,"opacity",1.0)
		state_inter_wp.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,300,750,400))
		state_inter_wp.assignProperty(self.albumGrid,"visible",0.0)
		state_inter_wp.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_inter_wp.assignProperty(self.songGrid,"visible",0.0)
		state_inter_wp.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,300,750,400))
		state_inter_wp.assignProperty(self.JBListItem,"visible",1.0)

         #intermediate state without player
                state_initial_wop.assignProperty(self,"state",2)
		state_inter_wop.assignProperty(self.nbutton,"text","Show Player")
		state_inter_wop.assignProperty(self.artistButton,"text","Artist")
		state_inter_wop.assignProperty(self.genreButton,"text","Genre")
		state_inter_wop.assignProperty(self.scanButton,"text","Scan")
		state_inter_wop.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		state_inter_wop.assignProperty(self.nbutton,"pos",QtCore.QPoint(0,5))
		state_inter_wop.assignProperty(self.artistButton,"pos",QtCore.QPoint(0,50))
		state_inter_wop.assignProperty(self.genreButton,"pos",QtCore.QPoint(0,95))
		state_inter_wop.assignProperty(self.scanButton,"pos",QtCore.QPoint(0,140))
		state_inter_wop.assignProperty(self.stack,"geometry",QtCore.QRect(0,250,225,450))	
		state_inter_wop.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),-400,400,150))
		state_inter_wop.assignProperty(self.player,"opacity",0.0)
		state_inter_wop.assignProperty(self.nbutton,"opacity",1.0)
		state_inter_wop.assignProperty(self.navigator,"opacity",1.0)
		
		state_inter_wop.assignProperty(self.albumGrid,"opacity",1.0)
		state_inter_wop.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_inter_wop.assignProperty(self.albumGrid,"visible",0.0)
		
		state_inter_wop.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_inter_wop.assignProperty(self.songGrid,"visible",0.0)
		state_inter_wop.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_inter_wop.assignProperty(self.JBListItem,"visible",1.0)

	#final state with player
                state_initial_wop.assignProperty(self,"state",2)
		state_final_wp.assignProperty(self.nbutton,"text","Hide Player")
		state_final_wp.assignProperty(self.artistButton,"text","Artist")
		state_final_wp.assignProperty(self.genreButton,"text","Genre")
		state_final_wp.assignProperty(self.scanButton,"text","Scan")
		state_final_wp.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),0,400,50))
		state_final_wp.assignProperty(self.nbutton,"pos",QtCore.QPoint(0,5))
		state_final_wp.assignProperty(self.artistButton,"pos",QtCore.QPoint(0,50))
		state_final_wp.assignProperty(self.genreButton,"pos",QtCore.QPoint(0,95))
		state_final_wp.assignProperty(self.scanButton,"pos",QtCore.QPoint(0,140))
		state_final_wp.assignProperty(self.stack,"geometry",QtCore.QRect(0,250,225,450))	
		state_final_wp.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		state_final_wp.assignProperty(self.player,"opacity",1.0)
		state_final_wp.assignProperty(self.nbutton,"opacity",1.0)
		state_final_wp.assignProperty(self.navigator,"opacity",1.0)
		
		state_final_wp.assignProperty(self.albumGrid,"opacity",1.0)
		state_final_wp.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,300,750,400))
		state_final_wp.assignProperty(self.albumGrid,"visible",0.0)
		
		state_final_wp.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,300,750,400))
		state_final_wp.assignProperty(self.songGrid,"visible",1.0)
                state_final_wp.assignProperty(self.songGrid,"opacity",1.0)
		state_final_wp.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_final_wp.assignProperty(self.JBListItem,"visible",0.0)

        #final state without player
		state_final_wop.assignProperty(self.nbutton,"text","Show Player")
		state_final_wop.assignProperty(self.artistButton,"text","Artist")
		state_final_wop.assignProperty(self.genreButton,"text","Genre")
		state_final_wop.assignProperty(self.scanButton,"text","Scan")
		state_final_wop.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		state_final_wop.assignProperty(self.nbutton,"pos",QtCore.QPoint(0,5))
		state_final_wop.assignProperty(self.artistButton,"pos",QtCore.QPoint(0,50))
		state_final_wop.assignProperty(self.genreButton,"pos",QtCore.QPoint(0,95))
		state_final_wop.assignProperty(self.scanButton,"pos",QtCore.QPoint(0,140))
		state_final_wop.assignProperty(self.stack,"geometry",QtCore.QRect(0,250,225,450))	
		state_final_wop.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),-400,400,150))
		state_final_wop.assignProperty(self.player,"opacity",0.0)
		state_final_wop.assignProperty(self.nbutton,"opacity",1.0)
		state_final_wop.assignProperty(self.navigator,"opacity",1.0)
		
		state_final_wop.assignProperty(self.albumGrid,"opacity",0.0)
		state_final_wop.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_final_wop.assignProperty(self.albumGrid,"visible",0.0)
		
		state_final_wop.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_final_wop.assignProperty(self.songGrid,"visible",1.0)
                state_final_wop.assignProperty(self.songGrid,"opacity",1.0)
		state_final_wop.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_final_wop.assignProperty(self.JBListItem,"visible",0.0)

	#transition1 : state_initial_wp to state_initial_wop
		t1 = state_initial_wp.addTransition(self.nbutton.clicked,state_initial_wop)
		t1.addAnimation(QtCore.QPropertyAnimation(self.albumGrid,"geometry",state_initial_wp))
	#transition2 : state_initial_wop to state_initial_wp
		t2 = state_initial_wop.addTransition(self.nbutton.clicked,state_initial_wp)
		t2.addAnimation(QtCore.QPropertyAnimation(self.player,"geometry",state_initial_wop))
		t2.addAnimation(QtCore.QPropertyAnimation(self.player,"opacity",state_initial_wop))
		t2.addAnimation(QtCore.QPropertyAnimation(self.albumGrid,"geometry",state_initial_wop))
	#transition3 : state_inter_wp to state_inter_wop
		t3 = state_inter_wp.addTransition(self.nbutton.clicked,state_inter_wop)
		t3.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"geometry",state_inter_wp))
	#transition4 : state_inter_wop to state_inter_wp
		t4 = state_inter_wop.addTransition(self.nbutton.clicked,state_inter_wp)
		t4.addAnimation(QtCore.QPropertyAnimation(self.player,"geometry",state_inter_wop))
		t4.addAnimation(QtCore.QPropertyAnimation(self.player,"opacity",state_inter_wop))
		t4.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"geometry",state_inter_wop))
	#transition5 : state_final_wp to state_final_wop
		t5 = state_final_wp.addTransition(self.nbutton.clicked,state_final_wop)
		t5.addAnimation(QtCore.QPropertyAnimation(self.songGrid,"geometry",state_final_wp))
	#transition6 : state_final_wop to state_final_wp
		t6 = state_final_wop.addTransition(self.nbutton.clicked,state_final_wp)
		t6.addAnimation(QtCore.QPropertyAnimation(self.player,"geometry",state_final_wop))
		t6.addAnimation(QtCore.QPropertyAnimation(self.player,"opacity",state_final_wop))
		t6.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"geometry",state_final_wop))
	#transition7 : state_initial_wop to state_inter_wop
		t7 = state_initial_wop.addTransition(self.artistButton.clicked,state_inter_wop)
		t7g = state_initial_wop.addTransition(self.genreButton.clicked,state_inter_wop)
		t7.addAnimation(QtCore.QPropertyAnimation(self.albumGrid,"visible",state_initial_wop))
		t7g.addAnimation(QtCore.QPropertyAnimation(self.albumGrid,"visible",state_initial_wop))
		t7.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"visible",state_initial_wop))
		t7g.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"visible",state_initial_wop))
	#transition8 : state_initial_wp to state_inter_wp
		t8 = state_initial_wp.addTransition(self.artistButton.clicked,state_inter_wp)
		t8g = state_initial_wp.addTransition(self.genreButton.clicked,state_inter_wp)
		t8.addAnimation(QtCore.QPropertyAnimation(self.albumGrid,"visible",state_initial_wop))
		t8g.addAnimation(QtCore.QPropertyAnimation(self.albumGrid,"visible",state_initial_wop))
		t8.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"visible",state_initial_wop))
		t8g.addAnimation(QtCore.QPropertyAnimation(self.JBListItem,"visible",state_initial_wop))
	#transition9 : state_inter_wop self loop
		t9 = state_inter_wop.addTransition(self.artistButton.clicked,state_inter_wop)
		t9g = state_inter_wop.addTransition(self.genreButton.clicked,state_inter_wop)
	#transition10 : state_inter_wp self loop
	
		t10 = state_inter_wp.addTransition(self.artistButton.clicked,state_inter_wp)
		t10g = state_inter_wp.addTransition(self.genreButton.clicked,state_inter_wp)
	#transition11 : state_inter_wop to state_initial_wop
		t11 = state_inter_wop.addTransition(self.JBListItem.itemSelectionChanged,state_initial_wop)	
	#transition12 : state_inter_wp to state_inter_wp
		t12 = state_inter_wp.addTransition(self.JBListItem.itemSelectionChanged,state_initial_wp)
	#transition13 : state_initial_wop to state_final_wop
		t13 = state_initial_wop.addTransition(self.albumGrid.selected,state_final_wop)
        #transition14 : state_initial_wp to state_final_wp
                t14 = state_initial_wp.addTransition(self.albumGrid.selected,state_final_wp)
                
                t15 = state_final_wop.addTransition(self.stack.backButtonClicked,state_initial_wop)
                
                t15 = state_final_wp.addTransition(self.stack.backButtonClicked,state_initial_wp)
                
                
		self.machine.setInitialState(state_initial_wop)
		self.machine.start()
		self.setScene(self.graphicsscene)

	def artistslot(self):
	      self.genrelistopen = False 
	      self.artistlistopen = True
	      stackstate = self.stack.getState()
	      self.k = self.cache.getArtistList(stackstate["genre"],self.navigator.getText())
	      self.listslotvalidity  = False
	      self.JBListItem.updatelist(self.k[self.artistScrolLevel:self.artistScrolLevel+10])# thinks signal is genrated inside this...
	      self.listslotvalidity  = True
	         
	def genreslot(self):
	      self.genrelistopen = True	 
	      self.artistlistopen = False
	      stackstate = self.stack.getState()
	      self.k = self.cache.getGenreList(stackstate["artist"],self.navigator.getText())
	      self.listslotvalidity  = False
	      self.JBListItem.updatelist(self.k[self.genreScrolLevel:self.genreScrolLevel+10])# thinks signal is genrated inside this...
	      self.listslotvalidity  = True
             	          
	def backslot(self):
	      if self.artistlistopen == True :
	         self.artistlistopen = False        
	      else :
	         self.genrelistopen = False
	     
	def listslot(self) :
	      if self.listslotvalidity  == True:
	         if self.genrelistopen == True :
	           
	            index = self.JBListItem.currentRow() 
	            genre = self.JBListItem.getdata(index)
	            self.stack.push("genre",genre)	            
	         else  :	          
	            index = self.JBListItem.currentRow() 
	            artist = self.JBListItem.getdata(index)
	            self.stack.push("artist",artist)
	         	 
	def albumslot(self,albumname):
	      self.songlist = self.cache.getSongItemList(albumname,self.navigator.getText())
	      print self.songlist 
	      self.songGrid.updatelist(self.songlist[self.songScrolLevel:self.songScrolLevel+10])
	      self.stack.push("album",albumname) #  check   
	   
        def refresh(self):		
	       stackstate = self.stack.getState()
 	       self.albumlist  = self.cache.getAlbumItemList(stackstate["genre"],stackstate["artist"],self.navigator.getText())
               self.albumGrid.updatelist(self.albumlist[self.albumScrolLevel:self.albumScrolLevel+10])
               print "refresh"

        def getStateSlot1(self):
             self.state = 1
             self.navigator.refresh() 

        def getStateSlot2(self):
             self.state = 2   
        
        def getStateSlot3(self):	  
             self.state = 3
             self.navigator.refresh()
        
        def getStateSlot4(self):
             self.state = 4

        def getStateSlot5(self):
             self.state = 5
             self.navigator.refresh()
      
        def getStateSlot6(self):
             self.state = 6
 
  
        def navigatorTextSlot(self,name):
             print self.state
             if(self.state == 1 or self.state == 2):			
                 self.refresh()    
             if(self.state == 3 or self.state == 4):			
                 if(self.genrelistopen == True):
                    self.genreslot()
                 if(self.artistlistopen == True):
                    self.artistslot()
             if(self.state == 5 or self.state == 6):
	         stackstate = self.stack.getState()
	         self.albumslot(stackstate["album"])


        def scanSlot(self): 
             dir_list=QtGui.QFileDialog.getExistingDirectory(self,'Select Folder','/home',QtGui.QFileDialog.ShowDirsOnly)
             print dir_list
             self.cache.insert_folder( dir_list)
      
        def songSlot(self,filename):
	     print " da ividam vare ethi pinjenda work avathe...?"  
             self.player.openFile(filename)

        def directionSlot(self,text):
	    # print text
	     if(text == "up"):
	         if(self.artistlistopen ==True):
		     if(self.artistScrolLevel > 0):
			 self.artistScrolLevel -= 10
			 self.artistslot()
	          
	         if(self.genrelistopen ==True):
		      if(self.genreScrolLevel > 0):
			 self.genreScrolLevel -= 10
			 self.genreslot()
		 
		 if(self.state == 1):
		     if(self.albumScrolLevel > 0):
		         self.albumScrolLevel -=2
		         		 
		 if(self.state == 2):
		     if(self.albumScrolLevel > 0):
		         self.albumScrolLevel -=2
		 
	         #if(self.scrolLevel >0):
	          #   self.scrolLevel -= 1;
	          #   if(self.artistlistopen ==True):
	           #      self.artistslot()
	           #  if(self.genrelistopen ==True):
	           #      self.genreslot()
	          # print "ko"
	          
	          
	     if(text == "down"):
	         #self.scrolLevel += 1; 
	         #print self.scrolLevel
	         if(self.artistlistopen ==True):
		     if(self.artistScrolLevel < (self.k.index(self.k[-1])-10)):
			 self.artistScrolLevel += 10
			 self.artistslot()
			 #print self.artistScrolLevel
	          
	         if(self.genrelistopen ==True):
		      if(self.genreScrolLevel < (self.k.index(self.k[-1])-10)):
			 self.genreScrolLevel += 10
			 self.genreslot()
			
	         	         
	         if(self.state == 1):
		     if(self.albumScrolLevel < (self.albumlist.index(self.albumlist[-1])-10)):
			 self.albumScrolLevel += 1
			 self.refresh()
			 print self.albumScrolLevel
	          
	         if(self.state == 2):
		      if(self.albumScrolLevel < (self.albumlist.index(self.albumlist[-1])-10)):
			 self.albumScrolLevel += 1
			 self.refresh()
			 print self.albumScrolLevel
			 
	         	         
	         if(self.state == 3):
		     if(self.songScrolLevel < (self.songlist.index(self.songlist[-1])-10)):
			 self.songScrolLevel += 1
			 self.albumslot()
			 #print self.albumScrolLevel
	          
	         if(self.state == 4):
		      if(self.songScrolLevel < (self.songlist.index(self.songlist[-1])-10)):
			 self.songScrolLevel += 1
			 self.albumSlot()
			 #print self.albumScrolLevel		 
	         
	        
	#def downSlot():
	 #    self.scrolLevel--;
            



if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName('JukeBox')
	q = Main()
        app.connect(q.artistButton ,QtCore.SIGNAL('clicked()'),q.artistslot)
        app.connect(q.genreButton ,QtCore.SIGNAL('clicked()'),q.genreslot)
        app.connect(q.JBListItem ,QtCore.SIGNAL('itemSelectionChanged ()'),q.listslot)
        app.connect(q.stack ,QtCore.SIGNAL('updated'),q.refresh)
        app.connect(q.albumGrid , QtCore.SIGNAL('selected(PyQt_PyObject)'),q.albumslot)
        app.connect(q.songGrid , QtCore.SIGNAL('selected(PyQt_PyObject)'),q.songSlot)
        app.connect(q.navigator , QtCore.SIGNAL('textChanged(PyQt_PyObject)'),q.navigatorTextSlot)
        app.connect(q.navigator , QtCore.SIGNAL('textChanged(PyQt_PyObject)'),q.navigatorTextSlot)
        app.connect(q.scanButton , QtCore.SIGNAL('clicked()'),q.scanSlot)
        app.connect(q.navigator , QtCore.SIGNAL('direction(PyQt_PyObject)'),q.directionSlot)
	q.show()
	sys.exit(app.exec_())
