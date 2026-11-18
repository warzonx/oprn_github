from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
from objet import Ui_MainWindow
import sys
class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Experience")
        self.btnOk.clicked.connect(self.btnOk_clicked)
        self.btnCancel.clicked.connect(self.btnCancel_clicked)


    def btnOk_clicked(self):
        print(f"Login: {self.txtLogin.text()}, Password: {self.txtPassword.text()}, Age: {self.spinAge.value()}")
    def btnCancel_clicked(self):
        sys.exit()
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Mainwindow()
    window.show()
    app.exec()