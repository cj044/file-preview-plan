import sys
from pathlib import Path
from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton,QTextBrowser
from PySide2.QtCore import Qt, QUrl
from PySide2.QtCore import QFile, QStringListModel
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtCore,QtUiTools
from traceback import print_exc

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


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        paths = [Path(url.toLocalFile()) for url in urls]
        self.textBrowser.setText('\n'.join([str(p) for p in paths]))


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow(app)
#     window.show()
#     app.exec()
#
#
# if __name__ == '__main__':
#     main()
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()