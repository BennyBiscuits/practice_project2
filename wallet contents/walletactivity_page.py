#Import Bitcoin
from bitcoin import *
from PySide6.QtWidgets import (QTabWidget, 
                               QApplication, 
                               QWidget, 
                               QLabel, 
                               QPushButton, 
                               QVBoxLayout, 
                               QHBoxLayout, 
                               QGroupBox, 
                               QSpinBox, 
                               QLineEdit, 
                               QRadioButton, 
                               QComboBox)

import sys

#Button 1, Messed Up The Code, Needs Work, Would be cool if the address appeared in a empty text box.
def generate_bitcoin_address():
    #Create Private Key
    private_key = random_key()
    print(random_key)
    #Create Public Key
    public_key = privtopub(random_key)
    print(public_key)
    #Create A Bitcoin Address
    address = pubtoaddr(public_key)
    print('My Address Is :' +address)

#Button 2, Messed Up The Code, Needs Work, Would be cool if the address appeared in a empty text box.
def generate_private_key():
    public_key = privtopub (private_key)
    print (public_key)
    private_key = random_key()
    print(random_key)
    print('My Private Key Is :" +private_key +')


# Define class to create a single push button
class DynamicButton(QWidget):

    def __init__(self):
        # Call parent constructor
        super().__init__()

        # Create a button
        self.btn = QPushButton("Generate Bitcoin Address", self)
        self.btn1 = QPushButton("Generate Private Key", self)
        # Set tooltip text for the button
        self.btn.setToolTip('This is a simple button')
        self.btn1.setToolTip('This is a simple button')
        # Set the geometry of the button
        self.btn.setGeometry(100, 20, 200, 40)
        self.btn1.setGeometry(100, 60, 200, 40)
        # Call function when the button is clicked
        self.btn.clicked.connect(self.onClicked)
        self.btn1.clicked.connect(self.onClicked)

        # Define label at the bottom of the button
        self.msgLabel = QLabel('', self)
        # Set the geometry of the label
        self.msgLabel.setGeometry(90, 60, 290, 60)

        # Display the window
        self.show()

    # Define function to handle the click event of the button
    def onClicked(self):
        # Set text for the label
        self.msgLabel.setText(generate_bitcoin_address())
        self.msgLabel.setText(generate_private_key())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Creation of GUI widgets, not yet on the screen
    bitcoin_button = DynamicButton()
    
    button = QPushButton('Receive Cryptocurrency')
    button2 = QPushButton('Send Cryptocurrency')
    label = QLabel('Currency')
    spinbox = QSpinBox()
    lineedit = QLineEdit()
    radio_button1 = QRadioButton('Generate Address')
    radio_button2 = QRadioButton('Generate Public Key')
    radio_button3 = QRadioButton('Generate Private Key')
    combo_box = QComboBox()
    combo_box.addItems(["Bitcoin", "Ethereum", "Dogecoin", "Blocknote"])

    # VBox is a widget which holds other widgets, and can be assigned to the window to display those widgets
    vlayout = QVBoxLayout()
    vlayout.addWidget(bitcoin_button)
    vlayout.addWidget(button)
    vlayout.addWidget(radio_button1)
    vlayout.addWidget(radio_button2)
    vlayout.addWidget(radio_button3)
    vlayout.addWidget(spinbox)

    # Horizontal box of widgets
    hlayout = QHBoxLayout()
    hlayout.addWidget(lineedit)
    hlayout.addWidget(label)
    hlayout.addWidget(combo_box)

    # Group Boxes
    top_groupbox = QGroupBox('Actions')
    top_groupbox.setLayout(vlayout)
    bottom_groupbox = QGroupBox('Balance')
    bottom_groupbox.setLayout(hlayout)

    main_tab_area = QTabWidget()
    main_tab_area.addTab(top_groupbox, "Actions")
    main_tab_area.addTab(bottom_groupbox, "Balance")

    layout = QVBoxLayout()
    layout.addWidget(main_tab_area)

    window = QWidget()
    window.setLayout(layout)
    window.show()
    window.resize(800, 600)

    sys.exit(app.exec_())
