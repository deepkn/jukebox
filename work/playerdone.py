import sys
from PyQt4 import QtGui,QtCore
import musicplayerui


try:
	from PyQt4.phonon import Phonon
except ImportError:
	app = QtGui.QApplication(sys.argv)
	QtGui.QMessageBox.critical(None,"Music Player",
	"Phonon support missing for qt installation...!",
	QtGui.QMessageBox.Ok|QtGui.QMessageBox.Default,QtGui.QMessageBox.NoButton)
	sys.exit(1)

class PlayerWidget(QtGui.QWidget):
	def __init__(self):
		super(QtGui.QWidget,self).__init__()
		self.ui = musicplayerui.Ui_Form()
		self.ui.setupUi(self)
		self.setWindowFlags(self.windowFlags()|QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowSystemMenuHint)
		#self.setAttribute(QtCore.Qt.WA_NoSystemBackground,True)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground,True)
		self.setAttribute(QtCore.Qt.WA_NoSystemBackground,True)		
		#self.setWindowOpacity(0.2)

		self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory,self)
		self.mediaObject = Phonon.MediaObject(self)
		
		self.mediaObject.setTickInterval(1000)
		self.mediaObject.stateChanged.connect(self.statechange)
		

		Phonon.createPath(self.mediaObject,self.audioOutput)
		
		self.ui.pb4.setAutoRepeat(True)
		self.ui.pb5.setAutoRepeat(True)
		self.connect(self.ui.pb1,QtCore.SIGNAL('clicked()'),self.mediaObject.play)
		self.connect(self.ui.pb2,QtCore.SIGNAL('clicked()'),self.mediaObject.pause)
		self.connect(self.ui.pb3,QtCore.SIGNAL('clicked()'),self.mediaObject.stop)
		self.connect(self.ui.pb4,QtCore.SIGNAL('clicked()'),self.volumeup)
		self.connect(self.ui.pb5,QtCore.SIGNAL('clicked()'),self.volumedown)
		self.ui.volumeSlider.setAudioOutput(self.audioOutput)
		self.ui.seekSlider.setMediaObject(self.mediaObject)
		#self.mediaObject.setCurrentSource(Phonon.MediaSource(sys.argv[1]))

	def volumeup(self):
		currentVolume = self.audioOutput.volume()
		self.audioOutput.setVolume(currentVolume+0.01)

	def volumedown(self):
		currentVolume = self.audioOutput.volume()
		self.audioOutput.setVolume(currentVolume-0.01)

	def statechange(self,newSt,oldSt):
		if newSt == Phonon.ErrorState:
			if self.mediaObject.errorType() == Phonon.FatalError:
				QtGui.QMessageBox.warning(self,"Fatal Error",self.mediaObject.errorString())
			else:
				QtGui.QMessageBox.warning(self,"Error",self.mediaObject.errorString())

	def contextMenuEvent(self,event):
		menu = QtGui.QMenu(self)
		quitAction = menu.addAction("Quit")
		action = menu.exec_(self.mapToGlobal(event.pos()))
		if action == quitAction:
			self.close()

	def openFile(self,filepath):
		self.mediaObject.stop()
		self.mediaObject.setCurrentSource(Phonon.MediaSource(filepath))

	

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setApplicationName("Music Player")
	app.setQuitOnLastWindowClosed(True)

	player = PlayerWidget()
	player.show()

	sys.exit(app.exec_())
