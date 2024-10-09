# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cover.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import resoure_main_rc

class Ui_cover(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"#centralwidget{border-image: url(:/image/resource/cover.png);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 180, 480, 45))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"\n"
"#pushButton{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"}\n"
"#pushButton:hover{\n"
"border-image:  url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 270, 480, 45))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"\n"
"#pushButton_2{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"}\n"
"#pushButton_2:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 360, 480, 45))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"\n"
"#pushButton_3{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"}\n"
"#pushButton_3:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 450, 480, 45))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"}\n"
"#pushButton_4:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 540, 480, 45))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"#pushButton_5{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"}\n"
"#pushButton_5:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"                                    \u5f00\u59cb\u6e38\u620f                  START GAME", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"                                    \u8bfb\u53d6\u5b58\u6863                  LOAD GAME", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"                                    \u6e38\u620f\u8bbe\u7f6e                  CONFIGS", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"                                    \u89d2\u8272\u4ea4\u6d41                  ACTOR INTERACT", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"                                    \u9000\u51fa\u6e38\u620f                  EXIT", None))
    # retranslateUi

