# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yinru.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_Page1(object):
    def setupUi(self, Page1):
        if not Page1.objectName():
            Page1.setObjectName(u"Page1")
        Page1.resize(1280, 720)
        Page1.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(0, 0, 0);}")
        self.centralwidget = QWidget(Page1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 230, 731, 141))
        font = QFont()
        font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font.setPointSize(67)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 370, 261, 101))
        font1 = QFont()
        font1.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font1.setPointSize(63)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 650, 201, 41))
        font2 = QFont()
        font2.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font2.setPointSize(20)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.test_pushButton = QPushButton(self.centralwidget)
        self.test_pushButton.setObjectName(u"test_pushButton")
        self.test_pushButton.setGeometry(QRect(130, 210, 75, 24))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 620, 341, 71))
        Page1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Page1)

        QMetaObject.connectSlotsByName(Page1)
    # setupUi

    def retranslateUi(self, Page1):
        Page1.setWindowTitle(QCoreApplication.translate("Page1", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Page1", u"\u6b22\u8fce\u6765\u5230\u6a21\u62df\u4eba\u751f", None))
        self.label_2.setText(QCoreApplication.translate("Page1", u"\u7b2c\u4e09\u90e8", None))
        self.label_3.setText(QCoreApplication.translate("Page1", u"\u6309\u4efb\u610f\u952e\u7ee7\u7eed", None))
        self.test_pushButton.setText(QCoreApplication.translate("Page1", u"\u5f00\u59cb", None))
        self.label_5.setText("")
    # retranslateUi

