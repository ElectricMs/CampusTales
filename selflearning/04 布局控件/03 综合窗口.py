from PySide6.QtWidgets import ( QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                                QLineEdit, QComboBox, QCheckBox, QRadioButton, QButtonGroup,
                                QTextEdit, QPlainTextEdit, QSlider)
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()
        self.lb1= QLabel("Label 1")
        self.lb1.setText("This is Label 1")
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn1 = QPushButton("Button 1")
        self.btn1.clicked.connect(self.btn1_clicked)

        self.lineedit= QLineEdit()
        self.lineedit.setPlaceholderText("Enter text here")
        self.lineedit.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineedit.textChanged.connect(self.lineedit_changed)
        self.lineedit.returnPressed.connect(self.lineedit_return_pressed)

        self.cb1 = QComboBox()# 不能直接传文字
        self.cb1.setPlaceholderText("Select an option")
        self.cb1.addItems(["Option 1", "Option 2", "Option 3"])
        self.cb1.removeItem(1)# 删除第二个选项
        self.cb1.currentIndexChanged.connect(self.cb1_index_changed)

        self.checkBox1 = QCheckBox("Check Box 1")
        self.checkBox1.setCheckable(False)
        self.checkBox2 = QCheckBox("Check Box 2")
        self.checkBox2.setChecked(True)
        self.checkBox2.stateChanged.connect(self.checkBox2_state_changed)

        self.radioBtn1 = QRadioButton("Radio Button 1")
        self.radioBtn2 = QRadioButton("Radio Button 2")
        self.radioBtnGroup = QButtonGroup()
        self.radioBtnGroup.addButton(self.radioBtn1)
        self.radioBtnGroup.addButton(self.radioBtn2)
        self.radioBtnGroup.buttonClicked.connect(self.radioBtn_clicked)

        self.richText= QTextEdit()
        self.richText.setPlaceholderText("Enter text here")
        # self.richText.setMarkdown("# This is a title\n\nThis is a paragraph")
        self.richText.setHtml("<h1>This is a title</h1><p>This is a paragraph</p>")
        self.richText.setPlainText("This is a paragraph")# 会覆盖上面的html
        self.richText.textChanged.connect(lambda: print("Text Changed:", self.richText.toPlainText()))

        self.plainText= QPlainTextEdit()
        self.plainText.setPlainText("This is a paragraph")

        self.slider= QSlider(Qt.Orientation.Horizontal)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)

        mainlayout.addWidget(self.lb1)
        mainlayout.addWidget(self.btn1)
        mainlayout.addWidget(self.lineedit)
        mainlayout.addWidget(self.cb1)
        mainlayout.addWidget(self.checkBox1)
        mainlayout.addWidget(self.checkBox2)
        mainlayout.addWidget(self.radioBtn1)
        mainlayout.addWidget(self.radioBtn2)
        mainlayout.addWidget(self.richText)
        mainlayout.addWidget(self.plainText)
        mainlayout.addWidget(self.slider)

        self.setLayout(mainlayout)


    def btn1_clicked(self):
        print("Button 1 clicked")

    def lineedit_changed(self, text):
        print("Line Edit text changed:", text)

    def lineedit_return_pressed(self):
        print("Line Edit return pressed:", self.lineedit.text())

    def cb1_index_changed(self, index):
        print("Combo Box index changed:", index)

    def checkBox2_state_changed(self, index):
        print("Check Box 2 state changed:", index)
        print(self.checkBox2.isChecked())
        # 0 未选中， 2 选中， 1 部分选中

    def radioBtn_clicked(self):
        print("Radio Button clicked:", self.radioBtnGroup.checkedButton().text())






if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()