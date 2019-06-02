from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QGroupBox
from PyQt5.QtGui import QIcon, QFont
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
        self.create_layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.label = QLabel(self)
        self.label.setFont(QFont('Sanserif', 15))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def create_layout(self):
        self.groupBox = QGroupBox(
            'What Is Your Favorite Programming Language?')
        self.groupBox.setFont(QFont('Sanserif', 13))
        hboxlayout = QHBoxLayout()
        self.radiobtn1 = QRadioButton('Python')
        self.radiobtn1.setFont(QFont('Sanserif', 13))
        self.radiobtn1.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn1)
        self.radiobtn2 = QRadioButton('Java')
        self.radiobtn2.setFont(QFont('Sanserif', 13))
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn2)
        self.radiobtn3 = QRadioButton('Golang')
        self.radiobtn3.setFont(QFont('Sanserif', 13))
        self.radiobtn3.toggled.connect(self.onRadioBtn)
        hboxlayout.addWidget(self.radiobtn3)
        self.groupBox.setLayout(hboxlayout)

    def onRadioBtn(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label.setText('You have selected {}'.format(radioBtn.text()))


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())