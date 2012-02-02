import sys
from PyQt4 import QtGui,QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class JBlist(QtGui.QListWidget):

   def __init__(self,lists):
      QtGui.QListWidget.__init__(self)
      self.setObjectName((_fromUtf8("topwidget")))
      self.lists = lists
      for items in lists :
         self.addItem("\n"+items+"\n")
      self.setGeometry(400,400,400,500)
      self.setStyleSheet(_fromUtf8("#topwidget{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
				   "font: 12pt \"Arial Black\";\n"
 				   "color: rgb(255, 255, 255);}"))


   def updatelist(self,lists):
      self.lists = lists
      self.clear()
      for items in lists :
         self.addItem("\n"+items+"\n")
      #self.setGeometry(400,400,400,500)
      #self.setStyleSheet(_fromUtf8("#topwidget{background-color: rgba(255,255,255,0);}"))

   
   def getdata(self,index):
      return self.lists[index]
#   def nik(self):
#      print " working"
#      self.close()
#      l = self.currentRow()
#      print l
      

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  tp = ["nikhil","koshi","ahemad"]  
  ob = JBlist(tp)
  lp = ["all","new","list"]
  ob.updatelist(lp)
  #app.connect(ob ,QtCore.SIGNAL('itemSelectionChanged ()'),ob.nik)
  ob.show()
  app.exec_()   
