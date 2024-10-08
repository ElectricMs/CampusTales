# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'strength_assignment.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource3_rc

class Ui_strength_assignment(object):
    def setupUi(self, strength_assignment):
        if not strength_assignment.objectName():
            strength_assignment.setObjectName(u"strength_assignment")
        strength_assignment.resize(1280, 720)
        strength_assignment.setStyleSheet(u"#centralwidget{border-image: url(:/image/resource/Strength_assign/p0424_l.png);}")
        self.centralwidget = QWidget(strength_assignment)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 40, 991, 631))
        self.label.setStyleSheet(u"border-image: url(:/image/resource/Strength_assign/02_brown.png);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(760, 680, 100, 35))
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"	border-image: url(:/image/resource/Strength_assign/qsave.png);}\n"
"#pushButton:hover{\n"
"	border-image: url(:/image/resource/Strength_assign/qload2.png);}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1120, 680, 100, 35))
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"	border-image: url(:/image/resource/Strength_assign/screen.png);}\n"
"#pushButton_2:hover{\n"
"	\n"
"	border-image: url(:/image/resource/Strength_assign/screen2.png);}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1000, 680, 100, 35))
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"	border-image: url(:/image/resource/Strength_assign/title.png);\n"
"	}\n"
"#pushButton_3:hover{\n"
"	border-image: url(:/image/resource/Strength_assign/title2.png);\n"
"	}")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(880, 680, 100, 35))
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"	border-image: url(:/image/resource/Strength_assign/qload.png);}\n"
"#pushButton_4:hover{\n"
"	border-image: url(:/image/resource/Strength_assign/qload2.png);}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 80, 541, 551))
        self.label_2.setStyleSheet(u"#label_2{border-image: url(:/image/resource/Strength_assign/paper2_yellow_l.png);}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(850, 90, 311, 531))
        self.label_3.setStyleSheet(u"border-image: url(:/image/resource/Strength_assign/label2_l.png);")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QRect(910, 149, 191, 61))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(24)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"      \n"
"	border-image: url(:/image/resource/Strength_assign/round_s.png);}\n"
"\n"
"QCheckBox::indicator{/*\u9009\u62e9\u6846\u5c3a\u5bf8*/\n"
"    \n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"       \n"
"	border-image: url(:/image/resource/Strength_assign/round_pressed.png);\n"
"}")
        self.checkBox.setIconSize(QSize(30, 30))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QRect(910, 220, 191, 61))
        self.checkBox_2.setFont(font)
        self.checkBox_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_2.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"      \n"
"	border-image: url(:/image/resource/Strength_assign/round_s.png);}\n"
"\n"
"QCheckBox::indicator{/*\u9009\u62e9\u6846\u5c3a\u5bf8*/\n"
"    \n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"       \n"
"	border-image: url(:/image/resource/Strength_assign/round_pressed.png);\n"
"}")
        self.checkBox_2.setIconSize(QSize(30, 30))
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setGeometry(QRect(910, 290, 191, 61))
        self.checkBox_3.setFont(font)
        self.checkBox_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_3.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"      \n"
"	border-image: url(:/image/resource/Strength_assign/round_s.png);}\n"
"\n"
"QCheckBox::indicator{/*\u9009\u62e9\u6846\u5c3a\u5bf8*/\n"
"    \n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"       \n"
"	border-image: url(:/image/resource/Strength_assign/round_pressed.png);\n"
"}")
        self.checkBox_3.setIconSize(QSize(30, 30))
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setGeometry(QRect(910, 360, 191, 61))
        self.checkBox_4.setFont(font)
        self.checkBox_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_4.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"      \n"
"	border-image: url(:/image/resource/Strength_assign/round_s.png);}\n"
"\n"
"QCheckBox::indicator{/*\u9009\u62e9\u6846\u5c3a\u5bf8*/\n"
"    \n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"       \n"
"	border-image: url(:/image/resource/Strength_assign/round_pressed.png);\n"
"}")
        self.checkBox_4.setIconSize(QSize(30, 30))
        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setGeometry(QRect(910, 430, 191, 61))
        self.checkBox_5.setFont(font)
        self.checkBox_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_5.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"      \n"
"	border-image: url(:/image/resource/Strength_assign/round_s.png);}\n"
"\n"
"QCheckBox::indicator{/*\u9009\u62e9\u6846\u5c3a\u5bf8*/\n"
"    \n"
"	width: 50px;\n"
"	height: 50px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"       \n"
"	border-image: url(:/image/resource/Strength_assign/round_pressed.png);\n"
"}")
        self.checkBox_5.setIconSize(QSize(30, 30))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(990, 530, 130, 41))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(13)
        font1.setBold(False)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"#pushButton_5{\n"
"border-image: url(:/image/resource/Strength_assign/002_07.png);\n"
"padding:10px;\n"
"}\n"
"#pushButton_5:hover{\n"
"	border-image: url(:/image/resource/Strength_assign/002_07_hover.png);}\n"
"#pushButton_5:pressed{\n"
"	border-image: url(:/image/resource/Strength_assign/002_07_click.png);}")
        self.label_checkbox1 = QLabel(self.centralwidget)
        self.label_checkbox1.setObjectName(u"label_checkbox1")
        self.label_checkbox1.setGeometry(QRect(320, 150, 491, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_checkbox1.setFont(font2)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 90, 431, 31))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.label_6.setFont(font3)
        self.label_checkbox2 = QLabel(self.centralwidget)
        self.label_checkbox2.setObjectName(u"label_checkbox2")
        self.label_checkbox2.setGeometry(QRect(320, 175, 491, 31))
        self.label_checkbox2.setFont(font2)
        self.label_checkbox3 = QLabel(self.centralwidget)
        self.label_checkbox3.setObjectName(u"label_checkbox3")
        self.label_checkbox3.setGeometry(QRect(320, 205, 491, 31))
        self.label_checkbox3.setFont(font2)
        self.label_checkbox4 = QLabel(self.centralwidget)
        self.label_checkbox4.setObjectName(u"label_checkbox4")
        self.label_checkbox4.setGeometry(QRect(320, 230, 491, 31))
        self.label_checkbox4.setFont(font2)
        self.label_checkbox5 = QLabel(self.centralwidget)
        self.label_checkbox5.setObjectName(u"label_checkbox5")
        self.label_checkbox5.setGeometry(QRect(320, 265, 491, 21))
        self.label_checkbox5.setFont(font2)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 160, 151, 61))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_5.setFont(font4)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(50, 20, 141, 141))
        self.graphicsView.setStyleSheet(u"border-image: url(:/image/resource/Strength_assign/boy_normal_-removebg-preview.png);\n"
"background-color:grey;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 250, 141, 41))
        font5 = QFont()
        font5.setPointSize(13)
        self.label_7.setFont(font5)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 320, 141, 51))
        self.label_8.setFont(font5)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 540, 411, 20))
        self.label_9.setFont(font5)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        strength_assignment.setCentralWidget(self.centralwidget)

        self.retranslateUi(strength_assignment)

        QMetaObject.connectSlotsByName(strength_assignment)
    # setupUi

    def retranslateUi(self, strength_assignment):
        strength_assignment.setWindowTitle(QCoreApplication.translate("strength_assignment", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.checkBox.setText(QCoreApplication.translate("strength_assignment", u" \u5b66\u4e60", None))
        self.checkBox_2.setText(QCoreApplication.translate("strength_assignment", u" \u5b66\u4e60", None))
        self.checkBox_3.setText(QCoreApplication.translate("strength_assignment", u" \u5b66\u4e60", None))
        self.checkBox_4.setText(QCoreApplication.translate("strength_assignment", u" \u5b66\u4e60", None))
        self.checkBox_5.setText(QCoreApplication.translate("strength_assignment", u" \u5b66\u4e60", None))
        self.pushButton_5.setText(QCoreApplication.translate("strength_assignment", u"\u5f00\u59cb\u65b0\u7684\u4e00\u5468", None))
        self.label_checkbox1.setText(QCoreApplication.translate("strength_assignment", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("strength_assignment", u"\u53ef\u9009\u9879\u76ee", None))
        self.label_checkbox2.setText(QCoreApplication.translate("strength_assignment", u"TextLabel", None))
        self.label_checkbox3.setText(QCoreApplication.translate("strength_assignment", u"TextLabel", None))
        self.label_checkbox4.setText(QCoreApplication.translate("strength_assignment", u"TextLabel", None))
        self.label_checkbox5.setText(QCoreApplication.translate("strength_assignment", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("strength_assignment", u"\u5c0f\u660e\uff08\u4f60\u81ea\u5df1\uff09", None))
        self.label_7.setText(QCoreApplication.translate("strength_assignment", u"\u7cbe\u529b\u503c\uff1aX", None))
        self.label_8.setText(QCoreApplication.translate("strength_assignment", u"\u5c5e\u6027\u503c\uff1aMaybe", None))
        self.label_9.setText(QCoreApplication.translate("strength_assignment", u"\u66f4\u591a\u6d3b\u52a8\uff0c\u8bf7\u95ef\u5173\u89e3\u9501.........", None))
    # retranslateUi

