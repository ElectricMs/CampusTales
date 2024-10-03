# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QEvent,QAbstractAnimation, QVariantAnimation,QPropertyAnimation, QEasingCurve,
    QSize, QTimer, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)


class ScaleButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)  # 设置为开启鼠标追踪

        # 初始化动画对象
        self.animation_time = 100  # 动画时间
        self.setStyleSheet(u"background-color:transparent;border:none;")
        
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(self.animation_time)  
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # 使用“InOutQuad”缓动曲线使得动画效果更加平滑

        self.font_animation = QVariantAnimation()
        self.font_animation.setDuration(self.animation_time)  
        self.font_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # 使用“InOutQuad”缓动曲线使得动画效果更加平滑
        self.font_animation.valueChanged.connect(self.update_font)  # 连接valueChanged信号到槽函数

        self.if_first_call = False  # 标志是否第一次调用

        self.timer = QTimer()
# 设置时间间隔（毫秒）
        self.timer.setInterval(100)  # 2秒后改变颜色
# 连接信号与槽
        self.timer.timeout.connect(self.change_color)
        
    def first_call(self):
        self.original_geometry = self.geometry()  # 保存原始尺寸
        print(self.original_geometry)
        self.enlarged_geometry = QRect(self.original_geometry.x() , self.original_geometry.y() -50, 
                                       self.original_geometry.width() , self.original_geometry.height() + 100)  # 放大后的尺寸
        self.original_font_size = self.font().pointSize()  # 保存原始字体大小
        self.enlarged_font_size = self.original_font_size +10  # 放大后的字体大小

    def update_font(self, point_size):
        font = self.font()
        font.setPointSize(point_size)
        self.setFont(font)

    def enterEvent(self, event):
        # 当鼠标进入按钮时触发
        super().enterEvent(event)
        if self.timer.isActive():
        # 如果定时器正在运行，则停止
            self.timer.stop()
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
        self.setStyleSheet("color:orange;background-color:transparent;border:none;")
        print("Enter event")
        print(self.animation.startValue())
        print(self.animation.endValue())
        self.animation.start()
        self.font_animation.start()
        
        
    def change_color(self):
    # 改变按钮背景色
        self.setStyleSheet("color:black;background-color:transparent;border:none;")
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
        self.timer.start()

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(960, 540)
        widget.setMinimumSize(QSize(960, 540))
        widget.setMaximumSize(QSize(960, 540))
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 381, 91))
        font = QFont()
        font.setPointSize(34)
        self.label.setFont(font)
        self.widget1 = QWidget(widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(60, 150, 170, 280))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 20, 0, 0)
        #StartButton
        self.startButton = ScaleButton(self.widget1)
        self.startButton.setObjectName(u"startButton")
        font1 = QFont()
        font1.setPointSize(16)
        self.startButton.setFont(font1)
        # self.startButton.setGeometry(QRect(50, 30, 100, 30))
        self.verticalLayout.addWidget(self.startButton)
        # InteractButton
        self.interactButton = ScaleButton(self.widget1)
        self.interactButton.setObjectName(u"interactButton")
        self.interactButton.setFont(font1)    
        # self.interactButton.setGeometry(QRect(50, 120, 100, 30))
        self.verticalLayout.addWidget(self.interactButton)
        # OptionButton
        self.optionButton = ScaleButton(self.widget1)
        self.optionButton.setObjectName(u"optionButton")
        self.optionButton.setFont(font1)   
        # self.optionButton.setGeometry(QRect(50, 180, 100, 30))
        
        self.verticalLayout.addWidget(self.optionButton)
        #ExitButton
        self.exitButton = ScaleButton(self.widget1)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setFont(font1)
        # self.exitButton.setGeometry(QRect(50, 250, 100, 30))

        self.verticalLayout.addWidget(self.exitButton)
        # self.verticalLayout.setContentsMargins(0,0,0,30)

        self.retranslateUi(widget)
        self.exitButton.clicked.connect(widget.close)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"CampusTales", None))
        self.label.setText(QCoreApplication.translate("widget", u"CampusTales", None))
        self.startButton.setText(QCoreApplication.translate("widget", u"Start", None))
        self.interactButton.setText(QCoreApplication.translate("widget", u"Interact", None))
        self.optionButton.setText(QCoreApplication.translate("widget", u"Option", None))
        self.exitButton.setText(QCoreApplication.translate("widget", u"Exit", None))
    # retranslateUi

