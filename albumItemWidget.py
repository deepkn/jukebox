import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
import song


class albumItemWidget(QtGui.QWidget):
  
   def __init__(self,album,image):    
      QtGui.QWidget.__init__(self)
      self.albumname = album
      self.setGeometry(300,300,150,150)
      self.setMaximumSize(150,150)
      self.labelLayout = QtGui.QVBoxLayout(self)
      self.albumLabel  = QtGui.QLabel(album)
      self.albumart = QtGui.QPixmap(image)
      self.imageLabel = QtGui.QLabel()
      self.imageLabel.setPixmap(self.albumart.scaled(200,200))
      self.labelLayout.addWidget( self.imageLabel)
      self.labelLayout.addWidget(self.albumLabel)

   def getalbum(self) :
      return self.albumname

   #def glowOnClick(self)  // will define later 
       
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  fd = albumItemWidget("album name","image path")
  fd.show()
  app.exec_()
  


 
