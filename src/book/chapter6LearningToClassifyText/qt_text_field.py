"""
https://pythonspot.com/en/python-qt-examples/
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class theApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title="PyQt testbox"
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(380, 40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 75)

        # connect button to funtion on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message ton', "you typed : " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = theApp()
    sys.exit(app.exec_())
