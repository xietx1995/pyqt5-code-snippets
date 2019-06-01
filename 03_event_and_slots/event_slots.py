from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtGui, QtCore
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = 'PyQt5 Push Button'
        left = 500
        top = 200
        width = 400
        height = 300
        icon = 'icon.png'

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.setGeometry(left, top, width, height)
        self.create_button()
        self.show()

    def create_button(self):
        button = QPushButton('Click Me', self)
        button.setGeometry(QtCore.QRect(100, 100, 200, 50))
        button.setIcon(QtGui.QIcon('button.png'))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip('Click me to open the home page.')
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        sys.exit(0)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
