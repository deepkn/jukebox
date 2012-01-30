import sys,os
from PyQt4 import QtGui,QtCore
import playerdone
import navigator



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
		self.player = playerdone.PlayerWidget()
		self.navigator = navigator.navi()
		self.nbutton = QtGui.QPushButton('                                       ')
		self.graphicsscene.addWidget(self.player)
		self.graphicsscene.addWidget(self.navigator)
		self.graphicsscene.addWidget(self.nbutton)
		self.setupStateMachine()
		#self.setScene(self.graphicsscene)

	def setupStateMachine(self):
		self.machine = QtCore.QStateMachine()
		statei = QtCore.QState(self.machine)
		statef = QtCore.QState(self.machine)
		#self.machine.addState(self.state1)
		#self.machine.addState(self.state2)
		#self.machine.setInitialState(statei)

		statei.assignProperty(self.nbutton,"text","Show Navigation Pad")
		statei.assignProperty(self.player,"geometry",QtCore.QRect((self.width/4),0,400,50))
		statei.assignProperty(self.nbutton,"geometry",QtCore.QPoint(0,0))
		statei.assignProperty(self.navigator,"geometry",QtCore.QRect(self.width,self.height,500,500))
		statei.assignProperty(self.player,"opacity",1.0)
		statei.assignProperty(self.nbutton,"opacity",1.0)
		statei.assignProperty(self.navigator,"opacity",0.0)

		statef.assignProperty(self.nbutton,"text","Show Player")
		statef.assignProperty(self.navigator,"geometry",QtCore.QRect((self.width)-380,(self.height/2)-375,380,800))
		statef.assignProperty(self.nbutton,"geometry",QtCore.QPoint(0,0))
		statef.assignProperty(self.player,"geometry",QtCore.QRect(0,self.height,400,150))
		statef.assignProperty(self.player,"opacity",0.0)
		statef.assignProperty(self.nbutton,"opacity",1.0)
		statef.assignProperty(self.navigator,"opacity",1.0)

		
		
		t1 = statei.addTransition(self.nbutton.clicked,statef)
		 
		t1.addAnimation(QtCore.QPropertyAnimation(self.navigator,"geometry",statei))
		t1.addAnimation(QtCore.QPropertyAnimation(self.nbutton,"geometry",statei))
		t1.addAnimation(QtCore.QPropertyAnimation(self.navigator,"opacity",statei))
		
		t2 = statef.addTransition(self.nbutton.clicked,statei)
		t2.addAnimation(QtCore.QPropertyAnimation(self.player,"geometry",statef))
		t2.addAnimation(QtCore.QPropertyAnimation(self.nbutton,"geometry",statef))
		t2.addAnimation(QtCore.QPropertyAnimation(self.player,"opacity",statef))

		#self.machine.addState(statei)
		#self.machine.addState(statef)
		self.machine.setInitialState(statei)


		self.machine.start()

		self.setScene(self.graphicsscene)

		


		
		


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName('JukeBox')
	q = Main()
	
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
