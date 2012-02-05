# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
from albumItemWidget1 import *
import song

class songItemWidget(albumItemWidget):
  
  
   selected = QtCore.pyqtSignal(str)
   
   def __init__(self,filename,title,image):    
      albumItemWidget.__init__(self,title,image)
      self.file = filename
      self.label = filename
   def getfilename(self) : 
      return self.file

   #def glowOnClick(self)  // will define later 
       
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  fd = songItemWidget("filename","title name","image path")
  print fd.getfilename()
  fd.show()
  app.exec_()
  


 
