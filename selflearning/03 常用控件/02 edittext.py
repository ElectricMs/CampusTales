from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPlainTextEdit, QPushButton
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        textedit = QTextEdit()
        textedit.setHtml("<h1>Hello World</h1><b>This is a bold text</b>")
     
        plaintextedit = QPlainTextEdit()
        btn = QPushButton("Add")
        btn.clicked.connect(lambda: plaintextedit.appendPlainText("Hello World"))


        mainlayout = QVBoxLayout()
        mainlayout.addWidget(textedit)
        mainlayout.addWidget(plaintextedit)
        mainlayout.addWidget(btn)
        self.setLayout(mainlayout)




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()