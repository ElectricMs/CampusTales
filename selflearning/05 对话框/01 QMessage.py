from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox


class myWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        self.btn=QPushButton("button")
        self.btn.clicked.connect(self.buttonClicked)



        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.btn)
        self.setLayout(mainLayout)

    def buttonClicked(self):
        replay = QMessageBox.information(self, "标题", "内容", QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.No, QMessageBox.StandardButton.Ok)
        # QMessageBox.question(self, "Question", "This is a question message")
        # QMessageBox.warning(self, "Warning", "This is a warning message")
        # QMessageBox.critical(self, "Critical", "This is a critical message")
        # QMessageBox.about(self, "About", "This is an about message")
        if replay == QMessageBox.StandardButton.Ok:
            print("点击了确定")
        else:
            print("点击了取消")




if __name__ == '__main__':
    app = QApplication([])
    window = myWindow()
    window.show()
    app.exec()