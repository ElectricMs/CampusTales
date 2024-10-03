import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

class SliderContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建主布局
        main_layout = QVBoxLayout()

        # 添加多行水平滑块
        for i in range(3):  # 例如，添加5行滑块
            slider_row = self.create_slider_row(f"Slider {i+1}")
            main_layout.addLayout(slider_row)
            if i < 4:  # 最后一行后面不需要添加伸缩空间
                main_layout.addSpacing(10)  # 添加固定间距

        # 设置主窗口的布局
        self.setLayout(main_layout)

        # 设置窗口标题和大小
        self.setWindowTitle('Slider Container Example')
        self.setGeometry(100, 100, 300, 200)

    def create_slider_row(self, label_text):
        # 创建水平布局
        row_layout = QHBoxLayout()

        # 创建标签
        label = QLabel(label_text)
        row_layout.addWidget(label)

        # 创建滑块
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        row_layout.addWidget(slider)

        return row_layout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SliderContainer()
    window.show()
    sys.exit(app.exec_())