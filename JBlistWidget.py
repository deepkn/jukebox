import sys
from PyQt4 import QtGui,QtCore

class JBlist(QtGui.QListWidget):

   def __init__(self,lists):
      QtGui.QListWidget.__init__(self)
      self.lists = lists
      for items in lists :
         self.addItem("\n"+items+"\n")
      self.setGeometry(400,400,400,500)

   def updatelist(self,lists):
      self.lists = lists
      self.clear()
      for items in lists :
         self.addItem("\n"+items+"\n")
      self.setGeometry(400,400,400,500)
   
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
