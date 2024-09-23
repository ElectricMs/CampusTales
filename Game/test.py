import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QStackedLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Layout Example")

        # 创建一个中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 使用QStackedLayout来管理多个布局
        self.stacked_layout = QStackedLayout()

        # 创建第一个布局
        layout1 = QVBoxLayout()
        label = QLabel("这是一个标签")
        line_edit = QLineEdit()
        layout1.addWidget(label)
        layout1.addWidget(line_edit)

        # 创建第二个布局
        layout2 = QVBoxLayout()
        button = QPushButton("点击切换布局")
        button.clicked.connect(self.toggle_layout)
        layout2.addWidget(button)

        # 将两个布局添加到QStackedLayout中
        container1 = QWidget()
        container1.setLayout(layout1)
        container2 = QWidget()
        container2.setLayout(layout2)
        self.stacked_layout.addWidget(container1)
        self.stacked_layout.addWidget(container2)

        # 设置当前显示的布局为第一个
        self.current_layout_index = 1
        self.stacked_layout.setCurrentIndex(self.current_layout_index)

        # 将堆叠布局设置为中心部件的布局
        central_widget.setLayout(self.stacked_layout)

    def toggle_layout(self):
        """切换当前显示的布局"""
        self.current_layout_index = 1 - self.current_layout_index  # 在0和1之间切换
        self.stacked_layout.setCurrentIndex(self.current_layout_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())