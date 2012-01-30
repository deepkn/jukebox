import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
from albumItemListWidget import albumItemListWidget
from songItemWidget import songItemWidget
from JBlistWidget import *


##class JBButtons(QtGui.QWidget):
##   def __init__(self):
##      QtGui.QWidget.__init__(self)
      


class JBMainWidget(QtGui.QWidget): 
   def __init__(self):
      QtGui.QWidget.__init__(self)
      self.Vlayout = QtGui.QVBoxLayout(self)  
      self.artistButton = QtGui.QPushButton("Artist") 
      self.genreButton = QtGui.QPushButton("Genre")
      self.scanButton = QtGui.QPushButton("Scan") 
      self.Vlayout.addWidget(self.artistButton )
      self.Vlayout.addWidget(self.genreButton )
      self.Vlayout.addWidget(self.scanButton )
  
      cach = cache()
      albumlist = cach.getAlbumItemList(None,None)
      self.albumListview = albumItemListWidget(albumlist)
      #self.buttons = JBButtons()
      self.Hlayout = QtGui.QHBoxLayout(self)
      self.H2layout = QtGui.QHBoxLayout(self.Hlayout)
      self.H2layout.addWidget(self.albumListview)
      #self.Hlayout.addChildLayout(self.Vlayout)
      self.Hlayout.addChildLayout(self.H2layout)

if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   #cac = cache()
   #cac.insert_folder("/home/nikhcc/music1") 
   #song_list = cac.getsongItemList(None,None)
   #print song_list
   #ob = JBMainWidget()
   ic = QtGui.QIcon("/home/nikhcc/JukeBox/data/mp3.jpg")
   #ic.show()
   tb = QtGui.QToolButton()
   siz = QtCore.QSize(100,100)
   ic.actualSize(siz)
   tb.setIcon(ic)
   pb =QtGui.QPushButton(ic,"kolli")  
   #asb = JBButtons()
   #asb.show()
   tb.show()
   app.exec_()

