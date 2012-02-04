# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from stackUi import Ui_Form
import time

class stackBar(QtGui.QWidget):

        backButtonClicked = QtCore.pyqtSignal()
        
	def __init__(self):
		
		QtGui.QWidget.__init__(self)
                ui = Ui_Form()
                ui.setupUi(self)
                ui.artistLabel.close()
                ui.genreLabel.close()
 		ui.albumLabel.close()
		ui.songLabel.close()
		self.stackstate = {'artist':None,
                                   'genre' :None,
                                   'album' :None,
                                   'song'  :None   }

                self.labeldict = { 'artist':ui.artistLabel,
                                   'genre' :ui.genreLabel,
                                   'album' :ui.albumLabel,
                                   'song'  :ui.songLabel     }
       
		self.categorylist = []
                self.connect(ui.backButton,QtCore.SIGNAL('clicked()'),self.pop)
		
	def getState(self):
		return self.stackstate
        
        def stackupdate(self):
           self.emit(QtCore.SIGNAL("updated"))

	def push(self,category,value):
		self.categorylist.append(category)
		self.stackstate[category]=value
                self.labeldict[category].setText(category + " : " + value)
                self.labeldict[category].show()
		self.stackupdate()
	def pop(self):
	        self.backButtonClicked.emit()
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

	
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	sb = stackBar()	
	sb.push('artist','Yesudas')
	sb.push('album','anything')
	q=sb.pop()
        sb.push('genre','anything')
        sb.push('album','anything')
	sb.show()
	app.exec_()
	
		
