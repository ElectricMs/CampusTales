# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Conversation.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(960, 540)
        Form.setMinimumSize(QSize(960, 540))
        Form.setMaximumSize(QSize(960, 540))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 60, 241, 411))
        self.label.setStyleSheet(u"border:2px solid blue;\n"
"border-radius:20px;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 60, 531, 411))
        self.label_2.setStyleSheet(u"border:2px solid blue;\n"
"border-radius:20px;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 80, 491, 321))
        self.label_3.setStyleSheet(u"border:2px solid blue;\n"
"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 400, 441, 51))
        self.label_4.setStyleSheet(u"border:2px solid blue;\n"
"")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(810, 400, 51, 51))
        self.label_5.setStyleSheet(u"border:2px solid blue;\n"
"")
        self.plainTextEdit_Input = QPlainTextEdit(Form)
        self.plainTextEdit_Input.setObjectName(u"plainTextEdit_Input")
        self.plainTextEdit_Input.setGeometry(QRect(380, 410, 421, 31))
        self.pushButton_Send = QPushButton(Form)
        self.pushButton_Send.setObjectName(u"pushButton_Send")
        self.pushButton_Send.setGeometry(QRect(810, 400, 51, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_Send.setFont(font)
        self.pushButton_Send.setStyleSheet(u"background-color: transparent;\n"
"border:none;")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(380, 90, 471, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 469, 299))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_Value = QLabel(Form)
        self.label_Value.setObjectName(u"label_Value")
        self.label_Value.setGeometry(QRect(103, 80, 191, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_Value.setFont(font1)
        self.label_Value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_Back = QPushButton(Form)
        self.pushButton_Back.setObjectName(u"pushButton_Back")
        self.pushButton_Back.setGeometry(QRect(850, 20, 91, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.pushButton_Send.setText(QCoreApplication.translate("Form", u"\u2014>", None))
        self.label_Value.setText(QCoreApplication.translate("Form", u"100", None))
        self.pushButton_Back.setText(QCoreApplication.translate("Form", u"BackToMain", None))
    # retranslateUi

