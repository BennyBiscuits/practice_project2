from PySide6.QtWidgets import QApplication, QWidget, QFormLayout, QSpinBox, QLineEdit
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setWindowTitle('Welcome, please register your account.')

        nameLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        verifypasswordLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        ageSpinBox = QSpinBox()
        
        passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        formLayout = QFormLayout()
        formLayout.addRow("Name or Username:", nameLineEdit)
        formLayout.addRow("Password:", passwordLineEdit)
        formLayout.addRow('Verify Password:', verifypasswordLineEdit)
        formLayout.addRow("Email:", emailLineEdit)
        formLayout.addRow("Age:", ageSpinBox)

        self.setLayout(formLayout)
        self.resize(600, 600)

        self.show()

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
