from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Hello World", self)
        btn.setGeometry(0, 0, 300, 50)
        btn.setToolTip("This is a tooltip")
        btn.setText("Hello World again")



        mainLayout = QVBoxLayout()
        lb=QLabel("This is a label")
        lb.setText("This is a label again")
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(lb)
        self.setLayout(mainLayout)


        line = QLineEdit(self)
        line.setGeometry(0, 100, 300, 50)
        line.setPlaceholderText("Enter text here")









if __name__ == '__main__':
    # 创建一个QApplication实例
    app = QApplication()
    
    # 创建一个MyWindow实例
    window = MyWindow()
    
    # 显示窗口
    window.show()
    
    # 进入应用程序的主循环
    app.exec()