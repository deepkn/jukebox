# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'navigator.ui'
#
# Created: Mon Jan 30 01:48:42 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(350, 728)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.setStyleSheet(_fromUtf8("background: transparent"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 170, 241, 41))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgba(85, 255, 0,120);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButtonBack = QtGui.QPushButton(Form)
        self.pushButtonBack.setGeometry(QtCore.QRect(270, 170, 71, 41))
        self.pushButtonBack.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonBack.setText(QtGui.QApplication.translate("Form", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.pushButtonRight = QtGui.QPushButton(Form)
        self.pushButtonRight.setGeometry(QtCore.QRect(220, 60, 81, 51))
        self.pushButtonRight.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonRight.setText(QtGui.QApplication.translate("Form", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRight.setObjectName(_fromUtf8("pushButtonRight"))
        self.pushButtonDown = QtGui.QPushButton(Form)
        self.pushButtonDown.setGeometry(QtCore.QRect(130, 110, 91, 51))
        self.pushButtonDown.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonDown.setText(QtGui.QApplication.translate("Form", "down", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDown.setObjectName(_fromUtf8("pushButtonDown"))
        self.pushButtonUp = QtGui.QPushButton(Form)
        self.pushButtonUp.setGeometry(QtCore.QRect(129, 10, 91, 51))
        self.pushButtonUp.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonUp.setText(QtGui.QApplication.translate("Form", "up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUp.setObjectName(_fromUtf8("pushButtonUp"))
        self.pushButtonLeft = QtGui.QPushButton(Form)
        self.pushButtonLeft.setGeometry(QtCore.QRect(49, 60, 81, 51))
        self.pushButtonLeft.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonLeft.setText(QtGui.QApplication.translate("Form", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLeft.setObjectName(_fromUtf8("pushButtonLeft"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 230, 331, 318))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton1 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton1.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton1.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton1.setMouseTracking(True)
        self.pushButton1.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton1.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.gridLayout_3.addWidget(self.pushButton1, 0, 0, 1, 1)
        self.pushButton2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton2.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton2.setMouseTracking(True)
        self.pushButton2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton2.setText(QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.gridLayout_3.addWidget(self.pushButton2, 0, 1, 1, 1)
        self.pushButton3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton3.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton3.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton3.setMouseTracking(True)
        self.pushButton3.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton3.setText(QtGui.QApplication.translate("Form", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))
        self.gridLayout_3.addWidget(self.pushButton3, 0, 2, 1, 1)
        self.pushButton4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton4.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton4.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton4.setMouseTracking(True)
        self.pushButton4.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton4.setText(QtGui.QApplication.translate("Form", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton4.setObjectName(_fromUtf8("pushButton4"))
        self.gridLayout_3.addWidget(self.pushButton4, 0, 3, 1, 1)
        self.pushButton7 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton7.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton7.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton7.setMouseTracking(True)
        self.pushButton7.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton7.setText(QtGui.QApplication.translate("Form", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton7.setObjectName(_fromUtf8("pushButton7"))
        self.gridLayout_3.addWidget(self.pushButton7, 1, 0, 1, 1)
        self.pushButton8 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton8.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton8.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton8.setMouseTracking(True)
        self.pushButton8.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton8.setText(QtGui.QApplication.translate("Form", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton8.setObjectName(_fromUtf8("pushButton8"))
        self.gridLayout_3.addWidget(self.pushButton8, 1, 1, 1, 1)
        self.pushButton9 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton9.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton9.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton9.setMouseTracking(True)
        self.pushButton9.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton9.setText(QtGui.QApplication.translate("Form", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton9.setObjectName(_fromUtf8("pushButton9"))
        self.gridLayout_3.addWidget(self.pushButton9, 1, 2, 1, 1)
        self.pushButtonA = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonA.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonA.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonA.setMouseTracking(True)
        self.pushButtonA.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonA.setText(QtGui.QApplication.translate("Form", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonA.setObjectName(_fromUtf8("pushButtonA"))
        self.gridLayout_3.addWidget(self.pushButtonA, 1, 4, 1, 1)
        self.pushButtonB = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonB.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonB.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonB.setMouseTracking(True)
        self.pushButtonB.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonB.setText(QtGui.QApplication.translate("Form", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonB.setObjectName(_fromUtf8("pushButtonB"))
        self.gridLayout_3.addWidget(self.pushButtonB, 1, 5, 1, 1)
        self.pushButtonC = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonC.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonC.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonC.setMouseTracking(True)
        self.pushButtonC.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonC.setText(QtGui.QApplication.translate("Form", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonC.setObjectName(_fromUtf8("pushButtonC"))
        self.gridLayout_3.addWidget(self.pushButtonC, 2, 0, 1, 1)
        self.pushButtonD = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonD.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonD.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonD.setMouseTracking(True)
        self.pushButtonD.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonD.setText(QtGui.QApplication.translate("Form", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonD.setObjectName(_fromUtf8("pushButtonD"))
        self.gridLayout_3.addWidget(self.pushButtonD, 2, 1, 1, 1)
        self.pushButtonE = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonE.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonE.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonE.setMouseTracking(True)
        self.pushButtonE.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonE.setText(QtGui.QApplication.translate("Form", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonE.setObjectName(_fromUtf8("pushButtonE"))
        self.gridLayout_3.addWidget(self.pushButtonE, 2, 2, 1, 1)
        self.pushButtonF = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonF.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonF.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonF.setMouseTracking(True)
        self.pushButtonF.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonF.setText(QtGui.QApplication.translate("Form", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonF.setObjectName(_fromUtf8("pushButtonF"))
        self.gridLayout_3.addWidget(self.pushButtonF, 2, 3, 1, 1)
        self.pushButtonG = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonG.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonG.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonG.setMouseTracking(True)
        self.pushButtonG.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonG.setText(QtGui.QApplication.translate("Form", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonG.setObjectName(_fromUtf8("pushButtonG"))
        self.gridLayout_3.addWidget(self.pushButtonG, 2, 4, 1, 1)
        self.pushButton5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton5.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton5.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton5.setMouseTracking(True)
        self.pushButton5.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton5.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton5.setObjectName(_fromUtf8("pushButton5"))
        self.gridLayout_3.addWidget(self.pushButton5, 0, 4, 1, 1)
        self.pushButton0 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton0.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton0.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton0.setMouseTracking(True)
        self.pushButton0.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton0.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton0.setObjectName(_fromUtf8("pushButton0"))
        self.gridLayout_3.addWidget(self.pushButton0, 1, 3, 1, 1)
        self.pushButton6 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton6.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton6.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton6.setMouseTracking(True)
        self.pushButton6.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton6.setText(QtGui.QApplication.translate("Form", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton6.setObjectName(_fromUtf8("pushButton6"))
        self.gridLayout_3.addWidget(self.pushButton6, 0, 5, 1, 1)
        self.pushButtonH = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonH.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonH.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonH.setMouseTracking(True)
        self.pushButtonH.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonH.setText(QtGui.QApplication.translate("Form", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonH.setObjectName(_fromUtf8("pushButtonH"))
        self.gridLayout_3.addWidget(self.pushButtonH, 2, 5, 1, 1)
        self.pushButtonI = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonI.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonI.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonI.setMouseTracking(True)
        self.pushButtonI.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonI.setText(QtGui.QApplication.translate("Form", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonI.setObjectName(_fromUtf8("pushButtonI"))
        self.gridLayout_3.addWidget(self.pushButtonI, 3, 0, 1, 1)
        self.pushButtonJ = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonJ.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonJ.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonJ.setMouseTracking(True)
        self.pushButtonJ.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonJ.setText(QtGui.QApplication.translate("Form", "J", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonJ.setObjectName(_fromUtf8("pushButtonJ"))
        self.gridLayout_3.addWidget(self.pushButtonJ, 3, 1, 1, 1)
        self.pushButtonK = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonK.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonK.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonK.setMouseTracking(True)
        self.pushButtonK.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonK.setText(QtGui.QApplication.translate("Form", "K", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonK.setObjectName(_fromUtf8("pushButtonK"))
        self.gridLayout_3.addWidget(self.pushButtonK, 3, 2, 1, 1)
        self.pushButtonL = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonL.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonL.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonL.setMouseTracking(True)
        self.pushButtonL.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonL.setText(QtGui.QApplication.translate("Form", "L", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonL.setObjectName(_fromUtf8("pushButtonL"))
        self.gridLayout_3.addWidget(self.pushButtonL, 3, 3, 1, 1)
        self.pushButtonM = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonM.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonM.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonM.setMouseTracking(True)
        self.pushButtonM.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonM.setText(QtGui.QApplication.translate("Form", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonM.setObjectName(_fromUtf8("pushButtonM"))
        self.gridLayout_3.addWidget(self.pushButtonM, 3, 4, 1, 1)
        self.pushButtonN = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonN.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonN.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonN.setMouseTracking(True)
        self.pushButtonN.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonN.setText(QtGui.QApplication.translate("Form", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonN.setObjectName(_fromUtf8("pushButtonN"))
        self.gridLayout_3.addWidget(self.pushButtonN, 3, 5, 1, 1)
        self.pushButtonO = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonO.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonO.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonO.setMouseTracking(True)
        self.pushButtonO.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonO.setText(QtGui.QApplication.translate("Form", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonO.setObjectName(_fromUtf8("pushButtonO"))
        self.gridLayout_3.addWidget(self.pushButtonO, 4, 0, 1, 1)
        self.pushButtonP = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonP.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonP.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonP.setMouseTracking(True)
        self.pushButtonP.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonP.setText(QtGui.QApplication.translate("Form", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonP.setObjectName(_fromUtf8("pushButtonP"))
        self.gridLayout_3.addWidget(self.pushButtonP, 4, 1, 1, 1)
        self.pushButtonQ = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonQ.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonQ.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonQ.setMouseTracking(True)
        self.pushButtonQ.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonQ.setText(QtGui.QApplication.translate("Form", "Q", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQ.setObjectName(_fromUtf8("pushButtonQ"))
        self.gridLayout_3.addWidget(self.pushButtonQ, 4, 2, 1, 1)
        self.pushButtonR = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonR.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonR.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonR.setMouseTracking(True)
        self.pushButtonR.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonR.setText(QtGui.QApplication.translate("Form", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonR.setObjectName(_fromUtf8("pushButtonR"))
        self.gridLayout_3.addWidget(self.pushButtonR, 4, 3, 1, 1)
        self.pushButtonS = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonS.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonS.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonS.setMouseTracking(True)
        self.pushButtonS.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonS.setText(QtGui.QApplication.translate("Form", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonS.setObjectName(_fromUtf8("pushButtonS"))
        self.gridLayout_3.addWidget(self.pushButtonS, 4, 4, 1, 1)
        self.pushButtonT = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonT.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonT.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonT.setMouseTracking(True)
        self.pushButtonT.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonT.setText(QtGui.QApplication.translate("Form", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonT.setObjectName(_fromUtf8("pushButtonT"))
        self.gridLayout_3.addWidget(self.pushButtonT, 4, 5, 1, 1)
        self.pushButtonU = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonU.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonU.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonU.setMouseTracking(True)
        self.pushButtonU.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonU.setText(QtGui.QApplication.translate("Form", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonU.setObjectName(_fromUtf8("pushButtonU"))
        self.gridLayout_3.addWidget(self.pushButtonU, 5, 0, 1, 1)
        self.pushButtonV = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonV.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonV.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonV.setMouseTracking(True)
        self.pushButtonV.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonV.setText(QtGui.QApplication.translate("Form", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonV.setObjectName(_fromUtf8("pushButtonV"))
        self.gridLayout_3.addWidget(self.pushButtonV, 5, 1, 1, 1)
        self.pushButtonW = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonW.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonW.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonW.setMouseTracking(True)
        self.pushButtonW.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonW.setText(QtGui.QApplication.translate("Form", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonW.setObjectName(_fromUtf8("pushButtonW"))
        self.gridLayout_3.addWidget(self.pushButtonW, 5, 2, 1, 1)
        self.pushButtonX = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonX.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonX.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonX.setMouseTracking(True)
        self.pushButtonX.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonX.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonX.setObjectName(_fromUtf8("pushButtonX"))
        self.gridLayout_3.addWidget(self.pushButtonX, 5, 3, 1, 1)
        self.pushButtonZ = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonZ.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonZ.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonZ.setMouseTracking(True)
        self.pushButtonZ.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonZ.setText(QtGui.QApplication.translate("Form", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonZ.setObjectName(_fromUtf8("pushButtonZ"))
        self.gridLayout_3.addWidget(self.pushButtonZ, 5, 5, 1, 1)
        self.pushButtonY = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonY.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButtonY.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButtonY.setMouseTracking(True)
        self.pushButtonY.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.558909, y2:0.0514091, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 100));\n"
"font: 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButtonY.setText(QtGui.QApplication.translate("Form", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonY.setObjectName(_fromUtf8("pushButtonY"))
        self.gridLayout_3.addWidget(self.pushButtonY, 5, 4, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 0, 20, 721))
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
	QtCore.QObject.connect(self.pushButton0, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton1, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton2, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton3, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton4, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton5, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton6, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton7, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton8, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButton9, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonA, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonB, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonC, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonD, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonE, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonF, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonG, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonH, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonI, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonJ, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonK, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonL, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonM, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonN, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonO, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonP, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonQ, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonR, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonS, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonT, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonU, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonV, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonW, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonX, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonY, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        QtCore.QObject.connect(self.pushButtonZ, QtCore.SIGNAL("clicked()"), Form.keyPadSlot)
        
        QtCore.QObject.connect(self.pushButtonBack, QtCore.SIGNAL("clicked()"), Form.backButtonSlot)

        QtCore.QObject.connect(self.pushButtonRight, QtCore.SIGNAL("clicked()"), Form.directionSlot)
	QtCore.QObject.connect(self.pushButtonLeft, QtCore.SIGNAL("clicked()"), Form.directionSlot)	
	QtCore.QObject.connect(self.pushButtonDown, QtCore.SIGNAL("clicked()"), Form.directionSlot)
	QtCore.QObject.connect(self.pushButtonUp, QtCore.SIGNAL("clicked()"), Form.directionSlot)
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

