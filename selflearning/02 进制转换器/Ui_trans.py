# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.transData = QLabel(Form)
        self.transData.setObjectName(u"transData")
        self.transData.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.transData.setFont(font)

        self.gridLayout.addWidget(self.transData, 1, 0, 1, 1)

        self.oneInputcomboBox = QComboBox(Form)
        self.oneInputcomboBox.setObjectName(u"oneInputcomboBox")
        self.oneInputcomboBox.setMinimumSize(QSize(126, 40))

        self.gridLayout.addWidget(self.oneInputcomboBox, 3, 1, 1, 1)

        self.twoInputcomboBox = QComboBox(Form)
        self.twoInputcomboBox.setObjectName(u"twoInputcomboBox")
        self.twoInputcomboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputcomboBox, 7, 1, 1, 1)

        self.dataType = QComboBox(Form)
        self.dataType.setObjectName(u"dataType")
        self.dataType.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.dataType, 2, 0, 1, 2)

        self.twoInputlineEdit = QLineEdit(Form)
        self.twoInputlineEdit.setObjectName(u"twoInputlineEdit")
        self.twoInputlineEdit.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputlineEdit, 7, 0, 1, 1)

        self.originData = QLabel(Form)
        self.originData.setObjectName(u"originData")
        self.originData.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(17)
        self.originData.setFont(font1)
        self.originData.setStyleSheet(u"color:rgb(148, 148, 148)")

        self.gridLayout.addWidget(self.originData, 0, 0, 1, 1)

        self.oneInputlineEdit = QLineEdit(Form)
        self.oneInputlineEdit.setObjectName(u"oneInputlineEdit")
        self.oneInputlineEdit.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.oneInputlineEdit, 3, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.transData.setText(QCoreApplication.translate("Form", u"0", None))
        self.originData.setText(QCoreApplication.translate("Form", u"0=", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

