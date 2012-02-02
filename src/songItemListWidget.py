import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
import song
from songItemWidget import *

class songItemGrid(QtGui.QWidget):  
  def __init__(self,songItemList):
     QtGui.QWidget.__init__(self)
     self.layout = QtGui.QGridLayout(self)  
     i = 0   
     for songItem in songItemList :
        songItemWidgetObject = songItemWidget(songItem[0],songItem[1],songItem[2])
        self.layout.addWidget(songItemWidgetObject,i/4,i%4)
        self.connect(songItemWidgetObject,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.selected)
        i = i + 1

     
  def selected(self,albumname):
     print "selected from song item grid " + albumname
     self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),albumname)
     print "jiko"

class songItemListWidget(QtGui.QWidget):
   def __init__(self, songItemList):
      QtGui.QWidget.__init__(self)
      self.layout = QtGui.QGridLayout(self)
      sk = QtGui.QScrollArea()
      self.ob = songItemGrid(songItemList)
      sk.setWidget(self.ob)
      self.scrolarea = sk
      #ob = songItemGrid(songItemList)
      #self.scrolarea.setWidget(ob)
      self.layout.addWidget(self.scrolarea)
      #self.setGeometry(400,400,500,500) 
      self.connect(self.ob,QtCore.SIGNAL("selected(PyQt_PyObject)"),self.selected)

   def updatelist(self,songItemList):
      self.scrolarea.close()
      self.ob = songItemGrid(songItemList)
      sk =  QtGui.QScrollArea()
      
      sk.setWidget(self.ob)
      self.scrolarea = sk
      self.layout.addWidget(self.scrolarea)
  
   
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

