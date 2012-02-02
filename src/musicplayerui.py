# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicplayer.ui'
#
# Created: Fri Jan 27 23:24:31 2012
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
        Form.resize(568, 302)
        Form.setMinimumSize(QtCore.QSize(567, 302))
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.frame1 = QtGui.QFrame(Form)
        self.frame1.setGeometry(QtCore.QRect(10, 10, 551, 281))
        self.frame1.setStyleSheet(_fromUtf8("#frame1{background : transparent;}"))
        self.frame1.setFrameShape(QtGui.QFrame.Panel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.frame = QtGui.QFrame(self.frame1)
        self.frame.setGeometry(QtCore.QRect(9, 149, 531, 121))
        self.frame.setMinimumSize(QtCore.QSize(531, 121))
        self.frame.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border-image: url(:/Downloads/btnoff1.png);}\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Downloads/btnon1.png);}\n"
"#pb1{\n"
"    image: url(:/Downloads/playoff.png);}\n"
"#pb1:pressed{\n"
"    image: url(:/Downloads/playon.png);}\n"
"#pb2{\n"
"    image: url(:/Downloads/pauseoff.png);}\n"
"#pb2:pressed{\n"
"    image: url(:/Downloads/pauseon.png);}\n"
"#pb3{\n"
"    image: url(:/Downloads/stop2.png);}\n"
"#pb3:pressed{\n"
"    image: url(:/Downloads/stop2on.png);}\n"
"#pb4{\n"
"    image: url(:/Downloads/volume_up.png);}\n"
"#pb5{\n"
"    image: url(:/Downloads/volume_down.png);}"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.layoutWidget = QtGui.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 103))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb1 = QtGui.QPushButton(self.layoutWidget)
        self.pb1.setMinimumSize(QtCore.QSize(111, 101))
        self.pb1.setText(_fromUtf8(""))
        self.pb1.setObjectName(_fromUtf8("pb1"))
        self.horizontalLayout_2.addWidget(self.pb1)
        self.pb2 = QtGui.QPushButton(self.layoutWidget)
        self.pb2.setMinimumSize(QtCore.QSize(111, 101))
        self.pb2.setText(_fromUtf8(""))
        self.pb2.setObjectName(_fromUtf8("pb2"))
        self.horizontalLayout_2.addWidget(self.pb2)
        self.pb3 = QtGui.QPushButton(self.layoutWidget)
        self.pb3.setMinimumSize(QtCore.QSize(111, 101))
        self.pb3.setText(_fromUtf8(""))
        self.pb3.setObjectName(_fromUtf8("pb3"))
        self.horizontalLayout_2.addWidget(self.pb3)
        self.pb4 = QtGui.QPushButton(self.layoutWidget)
        self.pb4.setMinimumSize(QtCore.QSize(71, 101))
        self.pb4.setText(_fromUtf8(""))
        self.pb4.setObjectName(_fromUtf8("pb4"))
        self.horizontalLayout_2.addWidget(self.pb4)
        self.pb5 = QtGui.QPushButton(self.layoutWidget)
        self.pb5.setMinimumSize(QtCore.QSize(71, 101))
        self.pb5.setText(_fromUtf8(""))
        self.pb5.setObjectName(_fromUtf8("pb5"))
        self.horizontalLayout_2.addWidget(self.pb5)
        self.layoutWidget1 = QtGui.QWidget(self.frame1)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 110, 529, 34))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.layoutWidget1)
        self.seekSlider.setMinimumSize(QtCore.QSize(401, 19))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayout.addWidget(self.seekSlider)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.layoutWidget1)
        self.volumeSlider.setMinimumSize(QtCore.QSize(120, 32))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

from PyQt4 import phonon
import musicplayer_rc
