import sys
from PyQt4 import QtGui,QtCore
#from cache1 import *
import song
import ClickableLabel

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class albumItemWidget(QtGui.QWidget):
  
   selected = QtCore.pyqtSignal(str)

   def __init__(self,album,image):    
      QtGui.QWidget.__init__(self)
      self.label = album
      self.setObjectName((_fromUtf8("topwidget")))
      self.setGeometry(300,300,250,175) # size position
      self.setMaximumSize(250,175)
      self.setStyleSheet(_fromUtf8("#topwidget{background-color: rgba(255,255,255,0);}"))
      self.labelLayout = QtGui.QVBoxLayout(self)
      self.albumLabel  = QtGui.QLabel(album)
      self.albumLabel.setObjectName((_fromUtf8("album")))
      self.albumLabel.setStyleSheet((_fromUtf8("#album{font: 12pt \"Arial Black\";\n"
 						       "color: rgb(255, 255, 255);}")))							
      self.albumart = QtGui.QPixmap(image)
      self.imageLabel = ClickableLabel.ClickableQLabel(self)
      self.imageLabel.setPixmap(self.albumart.scaled(150,150))
      #self.imageLabel.setObjectName((_fromUtf8("imagelabel")))
      #self.imageLabel.setStyleSheet((_fromUtf8("#imagelabel{background-color: rgba(255,255,255,0);}")))
      self.labelLayout.addWidget( self.imageLabel)
      self.labelLayout.addWidget(self.albumLabel)
      self.connect(self.imageLabel,QtCore.SIGNAL('clicked()'),self.selectedSlot)
      self.connect(self.imageLabel,QtCore.SIGNAL('pressed()'),self.zoomin)     
     # self.connect(self,QtCore.SIGNAL('selected(PyQt_PyObject)'),self.kol)  
      self.setStyleSheet("background: transparent;")   

   def getalabel(self) :
      return self.label

   #def selected(self):    # not yet checked...
      #self.imageLabel.setPixmap(self.albumart.scaled(200,200))
    #  self.emit(SIGNAL("selected(PyQt_PyObject)"),self.albumname)

   #def selected1( self): 
    
    #  self.emit(QtCore.SIGNAL('selected(PyQt_PyObject)'),self.label)

   def zoomin(self):
      self.imageLabel.setPixmap(self.albumart.scaled(200,200))
         
   def selectedSlot(self):
      self.imageLabel.setPixmap(self.albumart.scaled(150,150))
      print "selected slot from albumitemwidget "
      self.selected.emit(self.label)
      #self.emit(QtCore.SIGNAL('selected(PyQt_PyObject)'),self.label)
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
  


 
