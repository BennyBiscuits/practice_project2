from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PySide6.QtCore import Slot, QDate
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
		

    def initUI(self):        
        self.setWindowTitle('QCalendarWidget example')        

        vbox = QVBoxLayout(self)
        
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.clicked[QDate].connect(self.headsUp)
        
        self.resultLabel = QLabel(calendar.selectedDate().toString(),self)        

        vbox.addWidget(calendar)
        vbox.addWidget(self.resultLabel)

        self.resize(300, 300)
        self.show()

    @Slot(QDate)
    def headsUp(self, arg1):                
        self.resultLabel.setText(arg1.toString())

if __name__ == '__main__':    
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())
