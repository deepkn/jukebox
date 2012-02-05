# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from navigatorUi import Ui_Form

class navi(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
	self.setStyleSheet('background: transparent')

    def keyPadSlot(self):
        previoustext =  self.ui.lineEdit.text()
        self.ui.lineEdit.setText( previoustext + self.sender().text() )
        self.emit(QtCore.SIGNAL('textChanged(PyQt_PyObject)'),self.ui.lineEdit.text())

    def backButtonSlot(self):
        previoustext =  self.ui.lineEdit.text()
        self.ui.lineEdit.setText( previoustext[0:-1] )
        self.emit(QtCore.SIGNAL('textChanged(PyQt_PyObject)'),self.ui.lineEdit.text())   
    

    def directionSlot(self):
        self.emit(QtCore.SIGNAL('direction(PyQt_PyObject)'),self.sender().text())
  
    def test(self,name):
       print name

    def getText(self):
       return self.ui.lineEdit.text()

    def refresh(self):
       self.ui.lineEdit.setText("")




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = navi()
    QtCore.QObject.connect(Form, QtCore.SIGNAL("textChanged(PyQt_PyObject)"), Form.test)
    Form.show()
    sys.exit(app.exec_())

