# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
import song
from songItemWidget import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class songItemGrid(QtGui.QWidget):  
  def __init__(self,songItemList):
     QtGui.QWidget.__init__(self)
     self.layout = QtGui.QGridLayout(self)  
     i = 0   
     for songItem in songItemList :
        songItemWidgetObject = songItemWidget(songItem[0],songItem[1],songItem[2])
        songItemWidgetObject.setStyleSheet("background: transparent;")
        self.layout.addWidget(songItemWidgetObject,i/4,i%4)
        self.connect(songItemWidgetObject,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.selected)
        i = i + 1

     
  def selected(self,filename):
     print "selected from song item grid " + filename
     self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),filename)
     print "jiko"

class songItemListWidget(QtGui.QWidget):
   def __init__(self, songItemList):
      QtGui.QWidget.__init__(self)
      self.layout = QtGui.QGridLayout(self)
      sk = QtGui.QScrollArea()
      self.ob = songItemGrid(songItemList)
      
      self.ob.setStyleSheet("background: transparent;")
      
      sk.setWidget(self.ob)
      
      self.scrolarea = sk
      self.scrolarea.setStyleSheet("background: transparent;")
      #ob = songItemGrid(songItemList)
      #self.scrolarea.setWidget(ob)
      self.setObjectName(_fromUtf8("widget"))
      self.setStyleSheet(_fromUtf8("#widget{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));}\n"))
      self.layout.addWidget(self.scrolarea)
      #self.setGeometry(400,400,500,500) 
      self.connect(self.ob,QtCore.SIGNAL("selected(PyQt_PyObject)"),self.selected)

   def updatelist(self,songItemList):
      self.scrolarea.close()
      self.ob = songItemGrid(songItemList)
      self.ob.setStyleSheet("background: transparent;")
      sk =  QtGui.QScrollArea()
      
      sk.setWidget(self.ob)
      self.scrolarea = sk
      self.scrolarea.setStyleSheet("background: transparent;")
      self.layout.addWidget(self.scrolarea)
      self.connect(self.ob,QtCore.SIGNAL("selected(PyQt_PyObject)"),self.selected)
   
   def selected(self,albumname):
     print " song item list widget "+ albumname
     self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),albumname)
     print "olo  " + albumname
    

if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   cac = cache()
   #cac.insert_folder("/home/nikhcc/music1") 
   song_list = cac.getsongItemList(None,None)
   print song_list
   ob = albumItemListWidget(song_list) 
   ob.show()
   app.exec_()

