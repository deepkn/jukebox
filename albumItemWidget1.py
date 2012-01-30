import sys
from PyQt4 import QtGui,QtCore
#from cache1 import *
import song
import ClickableLabel


class albumItemWidget(QtGui.QWidget):
  
   def __init__(self,album,image):    
      QtGui.QWidget.__init__(self)
      self.label = album
      self.setGeometry(300,300,150,150)
      self.setMaximumSize(150,150)
      self.labelLayout = QtGui.QVBoxLayout(self)
      self.albumLabel  = QtGui.QLabel(album)
      self.albumart = QtGui.QPixmap(image)
      self.imageLabel = ClickableLabel.ClickableQLabel(self)
      self.imageLabel.setPixmap(self.albumart.scaled(150,150))  # set this as pushbutton or any clickable
      self.labelLayout.addWidget( self.imageLabel)#
      self.labelLayout.addWidget(self.albumLabel)
      self.connect(self.imageLabel,QtCore.SIGNAL('clicked()'),self.selected)
      self.connect(self.imageLabel,QtCore.SIGNAL('pressed()'),self.zoomin)     
     # self.connect(self,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.kol)     

   def getalabel(self) :
      return self.label

   #def selected(self):    # not yet checked...
      #self.imageLabel.setPixmap(self.albumart.scaled(200,200))
    #  self.emit(SIGNAL("selected(PyQt_PyObject)"),self.albumname)

   #def selected1( self): 
    
    #  self.emit(QtCore.SIGNAL('selected(PyQt_PyObject)'),self.label)

   def zoomin(self):
      self.imageLabel.setPixmap(self.albumart.scaled(200,200))
         
   def selected(self):
      self.imageLabel.setPixmap(self.albumart.scaled(150,150))
      print "selected slot from albumitemwidget "
      self.emit(QtCore.SIGNAL('selected(PyQt_PyObject)'),self.label)
      print "ok" + self.label
  


 # def glowOnClick(self)  // will define later 
 
   #def kol(self,album):
    #  print album
    #  print "called"

      
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  fd = albumItemWidget("album name","/home/deepak/Downloads/kol.jpg")
  #app.connect(fd,QtCore.SIGNAL('nikhil()'),kol)
  fd.show()
  app.exec_()
  


 
