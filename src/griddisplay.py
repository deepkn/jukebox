import sys
from PyQt4 import QtGui,QtCore
import cache
import song
import musicdisplay

class grid(QtGui.QWidget):
  
  def __init__(self):
    QtGui.QWidget.__init__(self)
    self.gridwidget = QtGui.QWidget(self)
    self.layout = QtGui.QVBoxLayout(self)     
 
  def takeList( self , song_list):
    for song in song_list :
      music_tab = musicdisplay.fileDisplay()
      music_tab.setdisplay( song.get_mindata() )
      self.layout.addWidget( music_tab)
  
      
     
app = QtGui.QApplication(sys.argv)
ob = grid()
cac = cache.cache()
cac.insert_folder("/home/deepak/Downloads") 
song_list = cac.read_folder("/home/deepak/Downloads","title")
ob.takeList(song_list)

"""
app = QtGui.QApplication(sys.argv)
cac = cache.cache() 
song_list = cac.read_folder("/home/deepak/Downloads")
gh = musicdisplay.fileDisplay()
#gh.setdisplay(song_list[4].get_mindata())

#layout.addWidget( gh)

od = QtGui.QWidget()
layout1 = QtGui.QVBoxLayout(od)
od.setGeometry(300,300,450,150)
for song in song_list :
  gh = musicdisplay.fileDisplay()
  gh.setdisplay(song.get_mindata())
  layout1.addWidget( gh)
#layout. 
#for i in range(4) :
#    ob = musicdisplay.fileDisplay() 


app = QtGui.QApplication(sy
#layout1.addWidget(od)
layout1.addWidget(gh)
##layout.addWidget(ob)
#lg = QtGui.QLabel("dinkan")
#ob = grid()

"""
ob.show()
app.exec_()
