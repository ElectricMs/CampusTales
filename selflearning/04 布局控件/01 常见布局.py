from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


        # login page


        self.mainlayout = QVBoxLayout()
        # self.userlayout = QHBoxLayout()
        # self.passwordlayout = QHBoxLayout()

        # self.userlayout.addWidget(QLabel("User Name"))
        # self.userlayout.addWidget(QLineEdit())
        # self.mainlayout.addLayout(self.userlayout)

        # self.passwordlayout.addWidget(QLabel("Password"))
        # self.passwordlayout.addWidget(QLineEdit())
        # self.mainlayout.addLayout(self.passwordlayout)

        # self.formlayout = QFormLayout()
        # self.formlayout.addRow(QLabel("User Name"), QLineEdit())
        # self.formlayout.addRow(QLabel("Password"), QLineEdit())
        # self.formlayout.addRow(QPushButton("Login"))
        # self.mainlayout.addLayout(self.formlayout)



        # self.mainlayout.addWidget(QPushButton("Login"))

        self.gridlayout = QGridLayout()
        self.gridlayout.addWidget(QLabel("User Name"), 0, 0)
        self.gridlayout.addWidget(QLineEdit(), 0, 1)
        self.gridlayout.addWidget(QLabel("Password"), 1, 0)
        self.gridlayout.addWidget(QLineEdit(), 1, 1)

        self.gridlayout.addWidget(QPushButton("Login"), 2, 0, 1, 2)


        self.mainlayout.addLayout(self.gridlayout)






        self.setLayout(self.mainlayout)




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()