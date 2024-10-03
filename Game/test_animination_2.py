import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QSize, QPoint, QAbstractAnimation, QVariantAnimation
from PySide6.QtGui import QFont

class ElasticButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)  # 设置为开启鼠标追踪

        # 初始化动画对象
        self.geometry_animation = QPropertyAnimation(self, b"geometry")
        self.geometry_animation.setDuration(200)
        self.geometry_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.font_animation = QVariantAnimation()
        self.font_animation.setDuration(300)
        self.font_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.font_animation.valueChanged.connect(self.update_font)

        self.if_first_call = False  # 标志是否第一次调用

    def first_call(self):
        self.original_geometry = self.geometry()  # 保存原始尺寸
        self.enlarged_geometry = QRect(self.original_geometry.x(), self.original_geometry.y(),
                                       self.original_geometry.width() + 40, self.original_geometry.height() + 40)  # 放大后的尺寸
        self.original_font_size = self.font().pointSize()  # 保存原始字体大小
        self.enlarged_font_size = self.original_font_size + 2  # 放大后的字体大小

    def update_font(self, point_size):
        font = self.font()
        font.setPointSize(point_size)
        self.setFont(font)

    def enterEvent(self, event):
        super().enterEvent(event)
        if not self.if_first_call:
            self.first_call()
            self.if_first_call = True
        if self.geometry_animation.state() == QAbstractAnimation.State.Running:
            self.geometry_animation.stop()
        if self.font_animation.state() == QAbstractAnimation.State.Running:
            self.font_animation.stop()

        self.geometry_animation.setStartValue(self.geometry())
        self.geometry_animation.setEndValue(self.enlarged_geometry)
        self.font_animation.setStartValue(self.font().pointSize())
        self.font_animation.setEndValue(self.enlarged_font_size)

        self.geometry_animation.start()
        self.font_animation.start()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        if self.geometry_animation.state() == QAbstractAnimation.State.Running:
            self.geometry_animation.stop()
        if self.font_animation.state() == QAbstractAnimation.State.Running:
            self.font_animation.stop()

        self.geometry_animation.setStartValue(self.geometry())
        self.geometry_animation.setEndValue(self.original_geometry)
        self.font_animation.setStartValue(self.font().pointSize())
        self.font_animation.setEndValue(self.original_font_size)

        self.geometry_animation.start()
        self.font_animation.start()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elastic Button Layout")

        # 创建垂直布局
        self.mylayout = QVBoxLayout()
        self.mylayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 添加多个按钮
        self.buttons = []
        for i in range(5):
            button = ElasticButton(f"Button {i+1}", self)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            self.mylayout.addWidget(button)
            self.buttons.append(button)

        # 添加顶部和底部的间距项
        self.top_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.bottom_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.mylayout.addItem(self.top_spacer)
        self.mylayout.addItem(self.bottom_spacer)

        # 设置布局
        self.setLayout(self.mylayout)

        # 设置窗口大小
        self.setGeometry(300, 300, 400, 300)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_button_positions()

    def adjust_button_positions(self):
        total_height = self.height()
        available_height = total_height - sum(button.height() for button in self.buttons)
        top_margin = available_height // 2
        bottom_margin = available_height - top_margin

        self.top_spacer.changeSize(0, top_margin)
        self.bottom_spacer.changeSize(0, bottom_margin)

        y_position = top_margin
        for button in self.buttons:
            button.setGeometry(button.x(), y_position, button.width(), button.height())
            y_position += button.height()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())