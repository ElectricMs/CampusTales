from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QVBoxLayout, QHBoxLayout, QLabel
from Ui_trans import Ui_Form

class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 用于存储数据类型的字典
        self.lengthVar={'米':100,'千米':100000,'厘米':1,'分米':10}
        self.weightVar={'克':1,'千克':1000,'斤':500}
        self.TypeDict={'长度':self.lengthVar,'质量':self.weightVar}

        self.dataType.addItems(list(self.TypeDict.keys()))
        self.oneInputcomboBox.addItems(list(self.lengthVar.keys()))
        self.twoInputcomboBox.addItems(list(self.lengthVar.keys()))
        self.bind()


    def bind(self):
        self.dataType.currentTextChanged.connect(self.typeChanged)
        self.pushButton.clicked.connect(self.calc)


    def calc(self):
        bigType=self.dataType.currentText()
        # 获取第一个输入框的值
        value=self.oneInputlineEdit.text()
        if value=='':
            return
        
        currentType=self.oneInputcomboBox.currentText()
        transType=self.twoInputcomboBox.currentText()

        standardization = float(value) * self.TypeDict[bigType][currentType]
        result = standardization / self.TypeDict[bigType][transType]

        self.originData.setText(f'{value} {currentType}=')
        self.transData.setText(f'{result} {transType}')

        self.twoInputlineEdit.setText(str(result))
        

    def typeChanged(self,text):
        self.oneInputcomboBox.clear()
        self.twoInputcomboBox.clear()
        
        self.oneInputcomboBox.addItems(list(self.TypeDict[text].keys()))
        self.twoInputcomboBox.addItems(list(self.TypeDict[text].keys()))









if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()