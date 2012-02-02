# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stack.ui'
#
# Created: Fri Jan 27 12:22:39 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(274, 437)
        Form.setStyleSheet("background-image: url(:/images/images/weather/images/weather_elements/bg_day_clear.png);\n"
"border-image: url(:/images/images/weather/images/weather_elements/bg_day_clear.png);")
        self.backButton = QtGui.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(100, 350, 92, 61))
        self.backButton.setMinimumSize(QtCore.QSize(92, 0))
        self.backButton.setMaximumSize(QtCore.QSize(92, 16777215))
        self.backButton.setStyleSheet("font: 75 10pt \"Andale Mono\";\n"
"selection-background-color: rgb(255, 255, 0);\n"
"font: 75 18pt \"Arial Black\";\n"
"border-color: rgb(0, 0, 127);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.500318, radius:0.5, fx:0.5, fy:0.5, stop:0.58 rgba(255, 255, 255, 255), stop:0.945 rgba(0, 0, 92, 255));")
        self.backButton.setObjectName("backButton")
        self.artistLabel = QtGui.QLabel(Form)
        self.artistLabel.setGeometry(QtCore.QRect(40, 60, 201, 71))
        self.artistLabel.setObjectName("artistLabel")
        self.genreLabel = QtGui.QLabel(Form)
        self.genreLabel.setGeometry(QtCore.QRect(40, 140, 201, 71))
        self.genreLabel.setObjectName("genreLabel")
        self.albumLabel = QtGui.QLabel(Form)
        self.albumLabel.setGeometry(QtCore.QRect(40, 220, 201, 71))
        self.albumLabel.setObjectName("albumLabel")
       
        self.songLabel = QtGui.QLabel(Form)
        self.songLabel.setGeometry(QtCore.QRect(40, 300, 201, 71))
        self.songLabel.setObjectName("songLabel")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Andale Mono\'; font-size:10pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setWhatsThis(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Andale Mono\'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">kkkk</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("Form", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.artistLabel.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dacd10;\">TextLabel</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.genreLabel.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffd608;\">TextLabel</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.albumLabel.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dfd916;\">TextLabel</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


        self.songLabel.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dfd916;\">TextLabel</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
      


