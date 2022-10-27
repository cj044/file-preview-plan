from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MyTextEdit(QtWidgets.QTextEdit):
    def mousePressEvent(self, e):
        self.link = self.anchorAt(e.pos())

    def mouseReleaseEvent(self, e):
        if self.link:
            print(f"Clicked on {self.link}")
            self.link = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chat_log = MyTextEdit(self.centralwidget)
        self.chat_log.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.chat_log.setReadOnly(True)
        self.chat_log.setObjectName("chat_log")
        MainWindow.setCentralWidget(self.centralwidget)


class MainFrame(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        self.setupUi(self)

    def appending(self):
        messages = ["Somethingsomething", "Hello", "What is up", "Big bo"]
        for msg in messages:
            self.chat_log.append(
            f'<span>{msg}<a style="color: pink" href="{msg}">[Add]</a></span>'
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainFrame()
    form.show()
    form.appending()
    app.exec_()