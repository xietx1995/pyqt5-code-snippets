from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5 import QtGui
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Layout'
        self.icon = 'icon.png'
        self.left = 500
        self.top = 300
        self.width = 400
        self.height = 300

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_layout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def create_layout(self):
        self.groupBox = QGroupBox(
            'What is your favorite programming language?')
        hboxlayout = QHBoxLayout()

        self.button1 = QPushButton('Python', self)
        self.button1.setMinimumHeight(40)
        hboxlayout.addWidget(self.button1)

        self.button2 = QPushButton('Java', self)
        self.button2.setMinimumHeight(40)
        hboxlayout.addWidget(self.button2)

        self.button3 = QPushButton('Golang', self)
        self.button3.setMinimumHeight(40)
        hboxlayout.addWidget(self.button3)

        self.groupBox.setLayout(hboxlayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
