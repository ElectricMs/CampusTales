from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb=QComboBox()
        cb.addItems(['a','b','c','d','e'])

        cb.currentTextChanged.connect(self.showName)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)


    def showName(self,name):
        print(name)



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()