# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
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
        self.startButton = QPushButton(widget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(60, 150, 131, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.startButton.setFont(font1)
        self.startButton.setStyleSheet(u"background-color: transparent;\n"
"border:none;")
        self.interactButton = QPushButton(widget)
        self.interactButton.setObjectName(u"interactButton")
        self.interactButton.setGeometry(QRect(60, 200, 131, 31))
        self.interactButton.setFont(font1)
        self.interactButton.setStyleSheet(u"background-color: transparent;\n"
"border:none;")
        self.optionButton = QPushButton(widget)
        self.optionButton.setObjectName(u"optionButton")
        self.optionButton.setGeometry(QRect(60, 250, 131, 31))
        self.optionButton.setFont(font1)
        self.optionButton.setStyleSheet(u"background-color: transparent;\n"
"border:none;")
        self.exitButton = QPushButton(widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(60, 300, 131, 31))
        self.exitButton.setFont(font1)
        self.exitButton.setStyleSheet(u"background-color: transparent;\n"
"border:none;")

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

