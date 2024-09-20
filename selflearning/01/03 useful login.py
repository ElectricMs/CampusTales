from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from Ui_login import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFun)


    def loginFun(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if account == '123' and password == '123':
            print('Login success')
        else:
            print('Login failed')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()