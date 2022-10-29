import sys
from pathlib import Path
from PySide2 import QtCore,QtUiTools
import sys
# import QtWidget Modules
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip
# import QtGui modules
from PySide2.QtGui import QIcon, QFont
class UiLoader(QtUiTools.QUiLoader):
    _baseinstance = None

    def createWidget(self, classname, parent=None, name=''):
        if parent is None and self._baseinstance is not None:
            widget = self._baseinstance
        else:
            widget = super(UiLoader, self).createWidget(classname, parent, name)
            if self._baseinstance is not None:
                setattr(self._baseinstance, name, widget)
        return widget
    def loadUi(self, uifile, baseinstance=None):
        self._baseinstance = baseinstance
        widget = self.load(uifile)
        QtCore.QMetaObject.connectSlotsByName(widget)
        return widget
class MainWindow(QWidget):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui()

    def ui(self):
        self.test= UiLoader().loadUi('dropURL.ui', self)  # 这里是改的地方
        self.setAcceptDrops(True)
        self.setToolTip('goods.png')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):

        urls = event.mimeData().urls()
        paths = [Path(url.toLocalFile()) for url in urls]
        self.textBrowser.setText('\n'.join([str(p) for p in paths]))
        self.textBrowser.setText.setToolTip("Active Icon")
    def setIconModes(self):
        # set icon
        icon1 = QIcon("geeksforgeeks.png")
        # set label
        label1 = QLabel('Sample', self)
        # set image in Active state(100X100是指 icon)
        pixmap1 = icon1.pixmap(100, 100, QIcon.Active, QIcon.On)
        # set Pixmap
        label1.setPixmap(pixmap1)
        # set tooltip text
        label1.setToolTip("Active Icon")
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()