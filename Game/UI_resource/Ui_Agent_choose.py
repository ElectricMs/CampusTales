# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Agent_choose.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QPropertyAnimation, QEasingCurve,QAbstractAnimation, QVariantAnimation,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import resource.resource2_rc
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
        self.enlarged_geometry = QRect(self.original_geometry.x() -30, self.original_geometry.y() - 15, 
                                       self.original_geometry.width() + 60, self.original_geometry.height() + 30)  # 放大后的尺寸
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
            #print("Animation is running, stop it first")
            self.animation.stop()  # 停止当前动画
        if self.font_animation.state() == QAbstractAnimation.State.Running:
            #print("Font animation is running, stop it first")
            self.font_animation.stop()  # 停止当前动画

        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.enlarged_geometry)
        self.font_animation.setStartValue(self.font().pointSize())
        self.font_animation.setEndValue(self.enlarged_font_size)
        
        #print("Enter event")
        #print(self.animation.startValue())
        #print(self.animation.endValue())
        self.animation.start()
        self.font_animation.start()

    def leaveEvent(self, event):
        # 当鼠标离开按钮时触发
        super().leaveEvent(event)
        if self.animation.state() == QAbstractAnimation.State.Running:
            #print("Animation is running, stop it first")
            self.animation.stop()  # 停止当前动画
        if self.font_animation.state() == QAbstractAnimation.State.Running:
            #print("Font animation is running, stop it first")
            self.font_animation.stop()  # 停止当前动画

        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.original_geometry)
        self.font_animation.setStartValue(self.font().pointSize())
        self.font_animation.setEndValue(self.original_font_size)

        #print("Leave event")
        #print(self.animation.startValue())
        #print(self.animation.endValue())
        self.animation.start()
        self.font_animation.start()
class Ui_Agent_choose(object):
    def setupUi(self, Agent_choose):
        if not Agent_choose.objectName():
            Agent_choose.setObjectName(u"Agent_choose")
        Agent_choose.resize(1280, 720)
        Agent_choose.setStyleSheet(u"border-image: url(:/image/resource/Agent/paper_l.png);")
        self.centralwidget = QWidget(Agent_choose)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = ScaleButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 330, 201, 81))
        font = QFont()
        font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);\n"
" }")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 231, 71))
        font1 = QFont()
        font1.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font1.setPointSize(45)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"#label{color: rgb(85, 0, 0);}\n"
"#label{letter-spacing:3px;}")
        self.pushButton_2 = ScaleButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 500, 200, 80))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}")
        self.pushButton_3 = ScaleButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 210, 200, 80))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}\n"
"")
        self.pushButton_4 = ScaleButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(730, 180, 221, 80))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}\n"
"")
        self.pushButton_5 =ScaleButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(770, 460, 211, 80))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"#pushButton_5{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}")
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(1150, 680, 100, 35))
        self.exit_button.setStyleSheet(u"#exit_button{border-image: url(:/image/resource/exit_button2.png)}\n"
"#exit_button:hover{border-image: url(:/image/resource/exit_hover.png)}\n"
"")
        Agent_choose.setCentralWidget(self.centralwidget)

        self.retranslateUi(Agent_choose)

        QMetaObject.connectSlotsByName(Agent_choose)
    # setupUi

    def retranslateUi(self, Agent_choose):
        Agent_choose.setWindowTitle(QCoreApplication.translate("Agent_choose", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("Agent_choose", u"girlfriend", None))
        self.label.setText(QCoreApplication.translate("Agent_choose", u"AGENT", None))
        self.pushButton_2.setText(QCoreApplication.translate("Agent_choose", u"president", None))
        self.pushButton_3.setText(QCoreApplication.translate("Agent_choose", u"Teacher", None))
        self.pushButton_4.setText(QCoreApplication.translate("Agent_choose", u"interviewer", None))
        self.pushButton_5.setText(QCoreApplication.translate("Agent_choose", u"?", None))
        self.exit_button.setText("")
    # retranslateUi

