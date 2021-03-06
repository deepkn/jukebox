import sys
from PyQt4 import QtGui,QtCore
from cache1 import *
from albumItemListWidget import albumItemListWidget
from songItemListWidget import songItemListWidget
from JBlistWidget import *
from stackWidget import *

class JBButtons(QtGui.QWidget):
   def __init__(self):
      QtGui.QWidget.__init__(self)
      self.Vlayout = QtGui.QVBoxLayout(self)  
      self.artistButton = QtGui.QPushButton("Artist") 
      self.genreButton = QtGui.QPushButton("Genre")
      self.scanButton = QtGui.QPushButton("Scan")
      self.backButton = QtGui.QPushButton("Back")
      self.backButton.close() 
      self.Vlayout.addWidget(self.artistButton )
      self.Vlayout.addWidget(self.genreButton )
      self.Vlayout.addWidget(self.scanButton )
      self.Vlayout.addWidget(self.backButton ) 
      #self.connect(self.artistButton ,QtCore.SIGNAL('Clicked()'),QtCore.SLOT(self.artistslot()))
      
   

class JBMainWidget(QtGui.QWidget): 
   def __init__(self):
      QtGui.QWidget.__init__(self)
      
      self.cach = cache()
      albumlist = self.cach.getAlbumItemList(None,None)
      self.albumListview = albumItemListWidget(albumlist)
      self.songListview  = songItemListWidget([])
      self.songListview.close()
      self.albumListview.setMinimumWidth(1200) 
      self.songListview.setMaximumWidth(1) 
      self.buttons = JBButtons()
      self.k = []  
      self.listWidget = JBlist(self.k)
      self.stackbar = stackBar()

      self.Vlayout = QtGui.QVBoxLayout(self)
      self.Hlayout = QtGui.QHBoxLayout(self)

      self.Hlayout.addWidget(self.buttons)
      self.Hlayout.addWidget(self.albumListview)
      self.Hlayout.addWidget(self.songListview)
      self.Vlayout.addLayout(self.Hlayout)
      self.Vlayout.addWidget( self.stackbar)

      self.artistlistopen = False
      self.genrelistopen  = False
      self.listslotvalidity  = True
      self.buttons.backButton.close()

   def artistslot(self):
      print " artist slot begin"
      self.artistlistopen = True
      stackstate = self.stackbar.getState()
      self.k = self.cach.getArtistList(stackstate["genre"])
      self.listslotvalidity  = False
      self.listWidget.updatelist(self.k)# thinks signal is genrated inside this...
      self.listslotvalidity  = True
      self.listWidget.show()     
      self.buttons.artistButton.close()
      self.buttons.genreButton.close()
      self.buttons.scanButton.close()
      self.buttons.backButton.show()
      print " artist slot ends"     
         


   def genreslot(self):
      print " genre slot begin"
      self.genrelistopen = True
   
      stackstate = self.stackbar.getState()
      self.k = self.cach.getGenreList(stackstate["artist"])
      
         
      self.listslotvalidity  = False
      self.listWidget.updatelist(self.k)# thinks signal is genrated inside this...
      self.listslotvalidity  = True
     
      self.listWidget.show()
    
      self.artistButton.close()
      self.genreButton.close()
      self.scanButton.close()
      #self.buttons.backButton.show()
      print " genre slot ends" 
          


   	 
   def backslot(self):
      print " back slot beg"
      if self.artistlistopen == True :
         self.artistlistopen = False        
      else :
         self.genrelistopen = False
      self.listWidget.close()
      self.genreButton.show()
      self.scanButton.show()  
      self.artistButton.show()
      
      print " back slot  ends"
     

   def listslot(self) :
      print " list slot begin"
      if self.listslotvalidity  == True:
         if self.genrelistopen == True :
            print "  slot if begin"
            index = self.listWidget.currentRow() 
            genre = self.listWidget.getdata(index)
            self.stackbar.push("genre",genre)
            print genre + '  genre'
            print " list slot if ends"
         else  :
            print " list slot else big"
            index = self.listWidget.currentRow() 
            artist = self.listWidget.getdata(index)
            self.stackbar.push("artist",artist)
            print artist + '  artist'
            print " list slot else ends"
         self.backslot()
      print "list slot end"
 



   def albumslot(self,albumname):
      songlist = self.cach.getSongItemList(albumname)
      print songlist
      self.songListview.updatelist(songlist)
      self.songListview.setMinimumWidth(1000)
      self.albumListview.setMaximumWidth(1)
      self.songListview.show()  
      self.albumListview.close()

   
########## algo ###################
 
   def refresh(self):
      stackstate = self.stackbar.getState()
      albumlist  = self.cach.getAlbumItemList(stackstate["genre"],stackstate["artist"],self.navigator.getText())
      self.albumListview.updatelist(albumlist)
      print "refresh"
   
##### todo ######

# scanslot
# songslot

 #########

if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   ob = JBMainWidget()
 
   app.connect(ob.buttons.artistButton ,QtCore.SIGNAL('pressed()'),ob.artistslot)
   app.connect(ob.buttons.genreButton ,QtCore.SIGNAL('pressed()'),ob.genreslot)
   app.connect(ob.buttons.backButton ,QtCore.SIGNAL('pressed()'),ob.backslot)
   app.connect(ob.listWidget ,QtCore.SIGNAL('itemSelectionChanged ()'),ob.listslot)
   app.connect(ob.stackbar ,QtCore.SIGNAL('updated'),ob.refresh)
   app.connect(ob.albumListview , QtCore.SIGNAL('selected(PyQt_PyObject)'),ob.albumslot)
   ob.show()

   app.exec_()

