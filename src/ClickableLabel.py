import sys
from PyQt4 import QtGui,QtCore


class ClickableQLabel(QtGui.QLabel):

   def __init__(self,parent):
      QtGui.QLabel.__init__(self,parent)

   def mouseReleaseEvent(self,event):
      self.emit(QtCore.SIGNAL('clicked()'))

   def mousePressEvent(self,event):
      self.emit(QtCore.SIGNAL('pressed()'))
