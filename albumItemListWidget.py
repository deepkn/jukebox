import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
import song
from albumItemWidget1 import *

class albumItemGrid(QtGui.QWidget):  
  def __init__(self,albumItemList):
    QtGui.QWidget.__init__(self)
    self.layout = QtGui.QGridLayout(self)  
    i = 0   
    for albumItem in albumItemList :
       albumItemWidgetObject = albumItemWidget(albumItem[0],albumItem[1])
       self.layout.addWidget(albumItemWidgetObject,i/5,i%5)
       self.connect(albumItemWidgetObject,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.selected)     
       i = i + 1
    
  def selected(self,albumname):
     self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),albumname)
     print "kol"

class albumItemListWidget(QtGui.QWidget):
  def __init__(self, albumItemList):
     QtGui.QWidget.__init__(self)
     self.layout = QtGui.QGridLayout(self)
     sk =  QtGui.QScrollArea()
     #self.scrolarea = QtGui.QScrollArea()
     self.ob = albumItemGrid(albumItemList)
     sk.setWidget(self.ob)
     self.scrolarea = sk
     sk.close()
     self.layout.addWidget(self.scrolarea)
     self.setGeometry(400,400,1000,500) 
     self.connect(self.ob,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.selected)
  
  def updatelist(self,albumItemList):
     self.scrolarea.close()
     self.ob = albumItemGrid(albumItemList)
     sk =  QtGui.QScrollArea()
     
     sk.setWidget(self.ob)
     self.scrolarea = sk
     self.layout.addWidget(self.scrolarea)

  def selected(self,albumname):
     self.emit(QtCore.SIGNAL("selected(PyQt_PyObject)"),albumname)
     print "op  " + albumname
    
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
   #ob.close()
   #ob.close()
   app.exec_()

