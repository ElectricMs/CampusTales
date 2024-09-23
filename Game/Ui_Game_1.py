# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Game_1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(960, 540)
        Form.setMinimumSize(QSize(960, 540))
        Form.setMaximumSize(QSize(960, 540))
        font = QFont()
        font.setPointSize(15)
        Form.setFont(font)
        self.pushButton_Next = QPushButton(Form)
        self.pushButton_Next.setObjectName(u"pushButton_Next")
        self.pushButton_Next.setGeometry(QRect(710, 430, 191, 51))
        font1 = QFont()
        font1.setPointSize(19)
        self.pushButton_Next.setFont(font1)
        self.border = QLabel(Form)
        self.border.setObjectName(u"border")
        self.border.setGeometry(QRect(280, 50, 351, 431))
        font2 = QFont()
        font2.setPointSize(14)
        self.border.setFont(font2)
        self.border.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 20px")
        self.radioButton_NO = QRadioButton(Form)
        self.radioButton_NO.setObjectName(u"radioButton_NO")
        self.radioButton_NO.setGeometry(QRect(380, 380, 98, 20))
        self.radioButton_Yes = QRadioButton(Form)
        self.radioButton_Yes.setObjectName(u"radioButton_Yes")
        self.radioButton_Yes.setGeometry(QRect(470, 380, 98, 20))
        self.label_Text = QLabel(Form)
        self.label_Text.setObjectName(u"label_Text")
        self.label_Text.setGeometry(QRect(330, 100, 261, 141))
        self.label_Text.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_Text.setWordWrap(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_Next.setText(QCoreApplication.translate("Form", u"Next", None))
        self.border.setText("")
        self.radioButton_NO.setText(QCoreApplication.translate("Form", u"No", None))
        self.radioButton_Yes.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.label_Text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

