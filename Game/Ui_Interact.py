# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interact.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(960, 540)
        Form.setMinimumSize(QSize(960, 540))
        Form.setMaximumSize(QSize(960, 540))
        self.pushButton_Back = QPushButton(Form)
        self.pushButton_Back.setObjectName(u"pushButton_Back")
        self.pushButton_Back.setGeometry(QRect(854, 20, 91, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 60, 221, 51))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.pushButton_PSU = QPushButton(Form)
        self.pushButton_PSU.setObjectName(u"pushButton_PSU")
        self.pushButton_PSU.setGeometry(QRect(180, 160, 251, 61))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_PSU.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_Back.setText(QCoreApplication.translate("Form", u"BackToMain", None))
        self.label.setText(QCoreApplication.translate("Form", u"Interact", None))
        self.pushButton_PSU.setText(QCoreApplication.translate("Form", u"President of Students' Union", None))
    # retranslateUi

