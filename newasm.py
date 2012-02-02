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
	def __init__(self):
		super(QtGui.QGraphicsView,self).__init__()
		self.initUi()

	def initUi(self):
		self.showMaximized()
		self.screen = QtGui.QApplication.desktop()
		self.width = self.screen.width()
		self.height = self.screen.height()
		self.graphicsscene = QtGui.QGraphicsScene(self)
		self.bg = QtGui.QPixmap("/home/deepak/Downloads/bg4.jpg")
		self.bgbrush = QtGui.QBrush(self.bg)
		#self.bgbrush.setTexture(self.bg)
		self.graphicsscene.setSceneRect(0,0,self.width-50,self.height-60)
		self.setBackgroundBrush(self.bgbrush)

                self.artistlistopen = False
                self.genrelistopen  = False
                self.listslotvalidity  = True
		

		self.cache = cache1.cache() 
   		self.albumlist = self.cache.getAlbumItemList(None,None,'')
                self.songlist = self.cache.getSongItemList(" ")
   		li = [('kio','lop'),('kol','koi')]

#################################################################################################

		self.albumGrid = albumItemListWidget.albumItemListWidget(self.albumlist)
                self.songGrid = songItemListWidget.songItemListWidget(self.songlist)
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
		#self.setScene(self.graphicsscene)

######################################################################################################
	
	def setupStateMachine(self):
		self.machine = QtCore.QStateMachine()
		state_initial_wp = QtCore.QState(self.machine)
		state_initial_wop = QtCore.QState(self.machine)
		state_inter_wp = QtCore.QState(self.machine)
		state_inter_wop = QtCore.QState(self.machine)
		state_final_wp = QtCore.QState(self.machine)
		state_final_wop = QtCore.QState(self.machine)
		
		#initial state with player
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
		state_initial_wop.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wop.assignProperty(self.songGrid,"visible",0.0)
		state_initial_wop.assignProperty(self.JBListItem,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_initial_wop.assignProperty(self.JBListItem,"visible",0.0)
		
		#intermediate state with player
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
		state_final_wop.assignProperty(self.albumGrid,"opacity",1.0)
		state_final_wop.assignProperty(self.albumGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_final_wop.assignProperty(self.albumGrid,"visible",0.0)
		state_final_wop.assignProperty(self.songGrid,"geometry",QtCore.QRect((self.width/4)-100,0,750,700))
		state_final_wop.assignProperty(self.songGrid,"visible",1.0)
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


		
		


		self.machine.setInitialState(state_initial_wop)


		self.machine.start()

		self.setScene(self.graphicsscene)

		

##################################################33



	def artistslot(self):
	      print " artist slot begin"
	      self.artistlistopen = True
	      stackstate = self.stack.getState()
	      self.k = self.cache.getArtistList(stackstate["genre"])
	      self.listslotvalidity  = False
	      self.JBListItem.updatelist(self.k)# thinks signal is genrated inside this...
	      self.listslotvalidity  = True
	      #self.JBListItem.show()     
	      #self.artistButton.close()
	      #self.genreButton.close()
	      #self.scanButton.close()
	      #self.backButton.show()
	      print " artist slot ends"     
	         
	

	def genreslot(self):
	      print " genre slot begin"
	      self.genrelistopen = True
	   
	      stackstate = self.stack.getState()
	      self.k = self.cache.getGenreList(stackstate["artist"])
	      
	         
	      self.listslotvalidity  = False
	      self.JBListItem.updatelist(self.k)# thinks signal is genrated inside this...
	      self.listslotvalidity  = True
              	     
              
	      #self.JBListItem.show()
	    
	      #self.artistButton.close()
	      #self.genreButton.close()
	      #self.scanButton.close()
	      #self.backButton.show()
	      print " genre slot ends" 
	          
	

   	 
	#def backslot(self):
	      #print " back slot beg"
	      #if self.artistlistopen == True :
	       #  self.artistlistopen = False        
	      #else :
	       #  self.genrelistopen = False
	      #self.JBListItem.close()
	      #self.genreButton.show()
	      #self.scanButton.show()  
	      #self.artistButton.show()
	     # self.buttons.backButton.close()
	      
	     # print " back slot  ends"
	     
	def listslot(self) :
	      print " list slot begin"
	      if self.listslotvalidity  == True:
	         if self.genrelistopen == True :
	            print "  slot if begin"
	            index = self.JBListItem.currentRow() 
	            genre = self.JBListItem.getdata(index)
	            self.stack.push("genre",genre)
	            print genre + '  genre'
	            print " list slot if ends"
	         else  :
	            print " list slot else big"
	            index = self.JBListItem.currentRow() 
	            artist = self.JBListItem.getdata(index)
	            self.stack.push("artist",artist)
	            print artist + '  artist'
	            print " list slot else ends"
	         #self.backslot()                  uncommment this.........
	      print "list slot end"
	 
	
	
	def albumslot(self,albumname):
	      songlist = self.cache.getSongItemList(albumname)
	      print songlist
	      self.songGrid.updatelist(songlist)
	      self.songGrid.setMinimumWidth(1000)
	      self.albumGrid.setMaximumWidth(1)
	      self.songGrid.show()  
	      #self.albumGrid.close()
	
	   
	########## algo ###################
 
        def refresh(self):
	    stackstate = self.stack.getState()
 	    albumlist  = self.cache.getAlbumItemList(stackstate["genre"],stackstate["artist"],self.navigator.getText())
            self.albumGrid.updatelist(albumlist)
            print "refresh"







##################################################3





		
		


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName('JukeBox')
	q = Main()
###########################################3

        app.connect(q.artistButton ,QtCore.SIGNAL('clicked()'),q.artistslot)
   	app.connect(q.genreButton ,QtCore.SIGNAL('clicked()'),q.genreslot)
   	#app.connect(q.backButton ,QtCore.SIGNAL('pressed()'),q.backslot)
        app.connect(q.JBListItem ,QtCore.SIGNAL('itemSelectionChanged ()'),q.listslot)
        app.connect(q.stack ,QtCore.SIGNAL('updated'),q.refresh)
        app.connect(q.albumGrid , QtCore.SIGNAL('selected(PyQt_PyObject)'),q.albumslot)

##############################################	





	"""state1 = QtCore.QState(q.machine)
	state2 = QtCore.QState(q.machine)
	q.machine.setInitialState(state1)
	state1.assignProperty(q.nbutton,"text","Show Navigation Pad")
	state1.assignProperty(q.player,"geometry",QtCore.QRectF((q.width/2)-200,(q.height/2)-75,400,150)
	state1.assignProperty(q.nbutton,"pos",QtCore.QPointF(10,q.height-55))
	state1.assignProperty(q.navigator,"geometry",QtCore.QRectF(q.width,q.height,500,500)
	state1.assignProperty(q.player,"opacity",qreal(1))
	state1.assignProperty(q.nbutton,"opacity",qreal(1))
	state1.assignProperty(q.navigator,"opacity",qreal(0))
	state2.assignProperty(q.nbutton,"text","Show Player")
	state2.assignProperty(q.navigator,"geometry",QtCore.QRectF((q.width/2)-200,(q.height/2)-75,500,500)
	state2.assignProperty(q.nbutton,"pos",QtCore.QPointF(q.width-110,q.height-55))
	state2.assignProperty(q.player,"geometry",QtCore.QRectF(0,self.height,400,150)
	state1.assignProperty(q.player,"opacity",qreal(0))
	state1.assignProperty(q.nbutton,"opacity",qreal(1))
	state1.assignProperty(q.navigator,"opacity",qreal(1))

	t1 = state1.addTransition(q.nbutton,SIGNAL(clicked()),state2)
	t1.addAnimaton(QtCore.QPropertyAnimation(q.navigator,"geometry")
	t1.addAnimation(QtCore.QPropertyAnimation(q.nbutton,"geometry")
	t1.addAnimaton(QtCore.QPropertyAnimation(q.navigator,"opacity")
	t2 = state2.addTransition(q.nbutton,SIGNAL(clicked()),state1)
	t1.addAnimaton(QtCore.QPropertyAnimation(q.player,"geometry")
	t1.addAnimation(QtCore.QPropertyAnimation(q.nbutton,"geometry")
	t1.addAnimaton(QtCore.QPropertyAnimation(q.player,"opacity")
	q.machine.start()"""
	q.show()
	sys.exit(app.exec_())
