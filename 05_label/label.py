from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
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
        vbox = QVBoxLayout()
        label1 = QLabel('This is PyQt5 Label')
        vbox.addWidget(label1)
        label2 = QLabel('This is PyQt5 GUI Application Development, Hello!')
        label2.setFont(QtGui.QFont('Sanserif', 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)
        self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())