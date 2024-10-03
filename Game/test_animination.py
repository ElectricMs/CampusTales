import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QSize, QPoint, QAbstractAnimation, QVariantAnimation
from PySide6.QtGui import QFont

class ScaleButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)  # 设置为开启鼠标追踪

        # 初始化动画对象
        self.animation_time = 180  # 动画时间


        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(self.animation_time)  
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # 使用“InOutQuad”缓动曲线使得动画效果更加平滑

        self.font_animation = QVariantAnimation()
        self.font_animation.setDuration(self.animation_time)  
        self.font_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # 使用“InOutQuad”缓动曲线使得动画效果更加平滑
        self.font_animation.valueChanged.connect(self.update_font)  # 连接valueChanged信号到槽函数

        self.if_first_call = False  # 标志是否第一次调用
        
    def first_call(self):
        self.original_geometry = self.geometry()  # 保存原始尺寸
        print(self.original_geometry)
        self.enlarged_geometry = QRect(self.original_geometry.x() - 20, self.original_geometry.y() - 15, 
                                       self.original_geometry.width() + 40, self.original_geometry.height() + 30)  # 放大后的尺寸
        self.original_font_size = self.font().pointSize()  # 保存原始字体大小
        self.enlarged_font_size = self.original_font_size + 8  # 放大后的字体大小

    def update_font(self, point_size):
        font = self.font()
        font.setPointSize(point_size)
        self.setFont(font)

    def enterEvent(self, event):
        # 当鼠标进入按钮时触发
        super().enterEvent(event)
        if not self.if_first_call:
            self.first_call()
            self.if_first_call = True
        if self.animation.state() == QAbstractAnimation.State.Running:
            print("Animation is running, stop it first")
            self.animation.stop()  # 停止当前动画
        if self.font_animation.state() == QAbstractAnimation.State.Running:
            print("Font animation is running, stop it first")
            self.font_animation.stop()  # 停止当前动画

        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.enlarged_geometry)
        self.font_animation.setStartValue(self.font().pointSize())
        self.font_animation.setEndValue(self.enlarged_font_size)
        
        print("Enter event")
        print(self.animation.startValue())
        print(self.animation.endValue())
        self.animation.start()
        self.font_animation.start()

    def leaveEvent(self, event):
        # 当鼠标离开按钮时触发
        super().leaveEvent(event)
        if self.animation.state() == QAbstractAnimation.State.Running:
            print("Animation is running, stop it first")
            self.animation.stop()  # 停止当前动画
        if self.font_animation.state() == QAbstractAnimation.State.Running:
            print("Font animation is running, stop it first")
            self.font_animation.stop()  # 停止当前动画

        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.original_geometry)
        self.font_animation.setStartValue(self.font().pointSize())
        self.font_animation.setEndValue(self.original_font_size)

        print("Leave event")
        print(self.animation.startValue())
        print(self.animation.endValue())
        self.animation.start()
        self.font_animation.start()

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyWindow")
        button = ScaleButton("Hover Me!", self)
        button.clicked.connect(self.close)
        button.setGeometry(QRect(50, 50, 100, 30))
        self.setGeometry(300, 300, 400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())