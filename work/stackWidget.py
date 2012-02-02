import sys
from PyQt4 import QtGui,QtCore

import time

class stackBar(QtGui.QWidget):

	def __init__(self):
		
		QtGui.QWidget.__init__(self)
		self.setMinimumWidth(1024)
		self.setMaximumHeight(60)
		self.adjustSize()
                artistLabel = QtGui.QLabel()
                genreLabel  = QtGui.QLabel()
 		albumLabel  = QtGui.QLabel()
		songLabel   = QtGui.QLabel()
		self.stackstate = {'artist':None,
                                   'genre' :None,
                                   'album' :None,
                                   'song'  :None   }

                self.labeldict = { 'artist':artistLabel,
                                   'genre' :genreLabel,
                                   'album' :albumLabel,
                                   'song'  :songLabel     }
       
		self.categorylist = []
		self.bstacklayout = QtGui.QVBoxLayout(self)
		self.backbutn = QtGui.QPushButton("Back")
		self.backbutn.setMaximumHeight(50)
                self.backbutn.setMaximumWidth(50)
		self.backbutn.adjustSize()
		self.bstacklayout.addWidget(self.backbutn)
                self.connect(self.backbutn,QtCore.SIGNAL('clicked()'),self.pop)
                #self.connect(self,QtCore.SIGNAL('updated'),self.noting)
		
	def getState(self):
		return self.stackstate
        
        def stackupdate(self):
           self.emit(QtCore.SIGNAL("updated"))

	def push(self,category,value):
		self.categorylist.append(category)
		self.stackstate[category]=value
                self.labeldict[category].setText(category + " : " + value)
                self.labeldict[category].show()
                self.bstacklayout.addWidget(self.labeldict[category])
		self.stackupdate()
	def pop(self):
		try:
			category=self.categorylist.pop()
			val=self.stackstate[category]
			self.stackstate[category]=None
                        self.labeldict[category].close()
			ret=(category,val)
                        self.stackupdate()
			return ret
		except IndexError:
			print "attempted pop from an empty list"
       # def noting(self):
       #    h = self.getState()
       #    print h


	
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	sb = StackBar()	
	sb.push('artist','Yesudas')
	sb.push('album','anything')
	q=sb.pop()
        sb.push('genre','anything')
        sb.push('album','anything')
        

	sb.show()
	app.exec_()
	
		
