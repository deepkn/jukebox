import sys
from PyQt4 import QtGui,QtCore
import song
import cache 
from albumListItem import *
 
class albumGrid(QtGui.QWidget):  
  def __init__(self,albumlist):
    " takes list of albumname and image path"

    QtGui.QWidget.__init__(self)
    self.layout = QtGui.QGridLayout(self)
    i=0     
    for album in albumlist :
     self.albumItemObject = albumListItem(album[0],album[1])
     self.layout.addWidget(self.albumItemObject,i/3,i%3)
     i = i+1 

app = QtGui.QApplication(sys.argv)
cac = cache.cache() 
songlist = cac.read_folder("/home/deepak/Downloads","title")
si = []
for song in songlist :
   mini = song.get_mindata()
   li   = ( mini[0] ,mini [1] )
   si.insert(0,li)


print si
ob = albumGrid(si)
ob.show()
app.exec_()
