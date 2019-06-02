from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.icon = "icon.png"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        labelImage = QLabel('Python image', self)
        pixmap = QPixmap('pic.png')
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())