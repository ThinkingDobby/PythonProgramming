import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("title")
        self.setGeometry(300, 100, 400, 500)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()