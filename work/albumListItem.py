import sys
from PyQt4 import QtGui,QtCore
import cache
import song


class albumListItem(QtGui.QWidget):
  
  def __init__(self,album,image):
    
    QtGui.QWidget.__init__(self)
    self.setGeometry(300,300,150,150)
    self.setMaximumSize(150,150)
    #self.labelWidget = QtGui.QWidget(self)
    #self.mainWidget  = QtGui.QWidget(self)
    print album
    self.labelLayout = QtGui.QVBoxLayout(self)
    #self.mainLayout  = QtGui.QHBoxLayout(self.mainWidget)
    
    #self.trackLabel  = QtGui.QLabel("No file selected")
    #self.artistLabel = QtGui.QLabel("------")
    #self.lengthLabel = QtGui.QLabel("------")
    self.albumLabel  = QtGui.QLabel(album)
    #self.genreLabel  = QtGui.QLabel("------")
    
    self.albumart = QtGui.QPixmap(image)
    self.imageLabel = QtGui.QLabel()
    self.imageLabel.setPixmap(self.albumart.scaled(150,150))
    
    
    #self.labelLayout.addWidget(self.trackLabel)
    #self.labelLayout.addWidget(self.artistLabel)
    #self.labelLayout.addWidget(self.lengthLabel)
    self.labelLayout.addWidget( self.imageLabel)
    self.labelLayout.addWidget(self.albumLabel)
    #self.labelLayout.addWidget(self.genreLabel)    
    #self.mainLayout.addWidget( self.labelWidget)
  
  
  #def setdisplay(self,album,datalist):
    
   # self.trackLabel.setText(datalist[0])
   # self.artistLabel.setText(datalist[1])
   # self.lengthLabel.setText(datalist[2])
   # self.albumLabel.setText(datalist[3])
   # self.genreLabel.setText(datalist[4])
   # print datalist[5]
   # self.albumart  = QtGui.QPixmap("/home/nikhcc/OTHER.jpeg")
   # print self.albumart
   # self.imageLabel.setPixmap(self.albumart)
    #imageLabel.setPixmap(self.albumart.scaled(150,150))

    
    
    
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  #fd = fileDisplay()
  cac = cache.cache() 
  song_obj = cac.read_folder("/home/nikhcc/music","artist")
  li = song_obj[0].get_mindata()
  fd = albumListItem("kooi.. aatirambile kombile ththaamma kiliko ththamma....",li[5])
  #albumart  = QtGui.QPixmap("/home/nikhcc/com.jpg")
  #imageLabel = QtGui.QLabel()
  #imageLabel.setPixmap(albumart)
  #imageLabel.show()

  #fd.setdisplay(song_obj[3].get_mindata())
  fd.setAutoFillBackground(True)
  fd. setUpdatesEnabled(True)
  fd.update(303,303,100,100)
  fd.show()
  app.exec_()
  


 
