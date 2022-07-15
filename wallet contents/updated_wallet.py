from bitcoin import *
from PySide6.QtWidgets import  (QApplication,
                               QTabWidget,
                               QWidget,
                               QVBoxLayout,
                               QHBoxLayout,
                               QGroupBox,
                               QPushButton,
                               QLabel,
                               QSpinBox,
                               QLineEdit,
                               QRadioButton,
                               QComboBox)
from PySide6.QtCore import Qt
import sys

app = QApplication(sys.argv)

button = QPushButton('Submit Transaction')
label = QLabel('Currency')
spinbox = QSpinBox()
lineedit = QLineEdit()
radio_button1 = QRadioButton('Generate Address')
radio_button2 = QRadioButton('Generate Public Key')
radio_button3 = QRadioButton('Generate Private Key')
combo_box = QComboBox()
combo_box.addItems(["Bitcoin", "Ethereum", "Dogecoin", "Ripple", "Blocknote"])

vlayout = QVBoxLayout()
vlayout.addWidget(button)
vlayout.addWidget(radio_button1)
vlayout.addWidget(radio_button2)
vlayout.addWidget(radio_button3)
vlayout.addWidget(spinbox)

hlayout = QHBoxLayout()
hlayout.addWidget(lineedit)
hlayout.addWidget(label)
hlayout.addWidget(combo_box)

top_groupbox = QGroupBox('Actions')
top_groupbox.setLayout(vlayout)

bottom_groupbox = QGroupBox('Select Currency')
bottom_groupbox.setLayout(hlayout)

layout = QVBoxLayout()
layout.addWidget(top_groupbox)
layout.addWidget(bottom_groupbox)

class ButtonAndLabel(QWidget):

    def __init__(self):
        super(ButtonAndLabel, self).__init__()

        self.button = QPushButton("button")
        self.button.clicked.connect(self.buttonClicked)

        self.label = QLabel("label: before clicked")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def buttonClicked(self):
        self.label.setText("label: after clicked")

class TabbedWindow(QTabWidget):

    def __init__(self, parent=None):
        super(TabbedWindow, self).__init__(parent)
        widget1 = QWidget()
        self.widget2 = ButtonAndLabel()
        widget3 = QWidget()
        self.addTab(widget1, "Tab 1")
        self.addTab(self.widget2, "Tab 2")
        self.addTab(widget3, "Tab 3")

window = QWidget()
window.setLayout(layout)
window.show()
window.resize(800,600)
sys.exit(app.exec_())
