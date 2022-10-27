# import system module
import sys

# import QtWidget Modules
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip

# import QtGui modules
from PySide2.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("GeeksforGeeks - ToolTip")

        # set window geometry
        self.setGeometry(300, 300, 500, 400)

        # set tooltip font and font type
        QToolTip.setFont(QFont("Decorative", 30, QFont.Bold))

        # set tooltip
        self.setToolTip('Our Main Window')

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

        # # set icon
        # icon2 = QIcon("geeksforgeeks.png")
        # # set label
        # label2 = QLabel('Sample', self)
        # # set image in Disabled state
        # pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        # # set P
        # label2.setPixmap(pixmap2)
        # label2.move(100, 0)
        # label2.setToolTip("Disable Icon")


myApp = QApplication(sys.argv)
window = Window()
window.setIconModes()
window.show()

myApp.exec_()
sys.exit(0)