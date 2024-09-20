from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout, QPushButton



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb=QCheckBox("I am a checkbox")
        cb.stateChanged.connect(self.showState)
        #cb.setCheckState(1)

        btn=QPushButton("Get State")
        btn.clicked.connect(lambda: print(cb.isChecked()))


        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        mainlayout.addWidget(btn)
        self.setLayout(mainlayout)


    def showState(self, state):
        print(state)







if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()