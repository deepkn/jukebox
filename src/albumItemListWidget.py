# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
import song
from albumItemWidget1 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class albumItemGrid(QtGui.QWidget):  

  selected = QtCore.pyqtSignal(str)

  def __init__(self,albumItemList):
    QtGui.QWidget.__init__(self)
    self.layout = QtGui.QGridLayout(self)  
    i = 0   
    for albumItem in albumItemList :
       albumItemWidgetObject = albumItemWidget(albumItem[0],albumItem[1])
       albumItemWidgetObject.setStyleSheet("background: transparent;")
       self.layout.addWidget(albumItemWidgetObject,i/4,i%4)
       albumItemWidgetObject.selected.connect(self.selectedSlot)
       #self.connect(albumItemWidgetObject,QtCore.SIGNAL('selected((PyQt_PyObject)'),self.selectedSlot)     
       #self.connect(albumItemWidgetObject,QtCore.SIGNAL("selected(PyQt_PyObject)"),self.selectedSlot)
       i = i + 1
    
  def selectedSlot(self,albumname):
     self.selected.emit(albumname)
     #self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),albumname)
     print "kol"

class albumItemListWidget(QtGui.QWidget):
   
  selected = QtCore.pyqtSignal(str)

  def __init__(self, albumItemList):
     QtGui.QWidget.__init__(self)
     self.layout = QtGui.QGridLayout(self)
     sk =  QtGui.QScrollArea()
     #self.scrolarea = QtGui.QScrollArea()
     self.ob = albumItemGrid(albumItemList)
     self.ob.setStyleSheet("background: transparent;")
     sk.setWidget(self.ob)
     self.scrolarea = sk
     self.scrolarea.setObjectName(_fromUtf8("scroll"))
     self.scrolarea.setStyleSheet(_fromUtf8("#scroll{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(255, 255, 255, 40));}\n"))
     sk.close()
     self.setObjectName(_fromUtf8("widget"))
     self.layout.addWidget(self.scrolarea)
     self.setGeometry(400,400,700,500)
     self.setStyleSheet(_fromUtf8("#widget{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));}\n"))
     #self.connect(self.ob,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.selectedSlot)
     self.ob.selected.connect(self.selectedSlot)
     
  def updatelist(self,albumItemList):
     self.scrolarea.hide()
     self.ob.close()
     self.layout.removeWidget(self.scrolarea)
     self.ob = albumItemGrid(albumItemList)
     sk =  QtGui.QScrollArea()
     self.ob.setStyleSheet("background: transparent;")
     sk.setWidget(self.ob)
     self.scrolarea = sk
     self.scrolarea.setObjectName(_fromUtf8("scroll"))
     self.scrolarea.setStyleSheet(_fromUtf8("#scroll{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(255, 255, 255, 40));}\n"))
     self.layout.addWidget(self.scrolarea)
     self.ob.selected.connect(self.selectedSlot)

  def selectedSlot(self,albumname):
     self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),albumname)
     self.selected.emit(albumname)
     print "opo  " + albumname
    
if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   cac = cache() 
   song_list = cac.getAlbumItemList(None,None,'')
   print song_list
   li = [('kio','lop'),('kol','koi')]
   ob = albumItemListWidget(song_list)
   ob.updatelist(li) 
   ob.updatelist(song_list)
   ob.show()
   app.exec_()

