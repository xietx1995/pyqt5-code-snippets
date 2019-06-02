from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, \
    QGroupBox, QCheckBox, QLabel
from PyQt5.QtGui import QFont, QIcon
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 CheckBox"
        self.icon = "icon.png"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.label = QLabel()
        self.label.setFont(QFont("Sanserif", 15))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox(
            "What Is Your Favorite Programming Language ?")
        self.groupBox.setFont(QFont("Sanserif", 13))
        hboxLayout = QHBoxLayout()
        self.check1 = QCheckBox("Python")
        self.check1.setFont(QFont("Sanserif", 13))
        self.check1.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.check1)
        self.check2 = QCheckBox("Java")
        self.check2.setFont(QFont("Sanserif", 13))
        self.check2.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.check2)
        self.check3 = QCheckBox("C++")
        self.check3.setFont(QFont("Sanserif", 13))
        self.check3.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.check3)
        self.groupBox.setLayout(hboxLayout)

    def onCheckbox_toggled(self):
        arr = []
        if self.check1.isChecked():
            arr.append(self.check1.text())
        if self.check2.isChecked():
            arr.append(self.check2.text())
        if self.check3.isChecked():
            arr.append(self.check3.text())
        self.label.setText("You have selected: " + ", ".join(arr))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())