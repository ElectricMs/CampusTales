# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Agent_choose.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import resource2_rc

class Ui_Agent_choose(object):
    def setupUi(self, Agent_choose):
        if not Agent_choose.objectName():
            Agent_choose.setObjectName(u"Agent_choose")
        Agent_choose.resize(1280, 720)
        Agent_choose.setStyleSheet(u"border-image: url(:/image/resource/Agent/paper_l.png);")
        self.centralwidget = QWidget(Agent_choose)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 180, 201, 81))
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
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 410, 200, 80))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(780, 440, 200, 80))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}\n"
"")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(540, 270, 200, 80))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"border-image: url(:/image/resource/Agent/\u5bf9\u8bdd\u6807\u7b7e2.jpg);\n"
"color: rgb(85, 0, 0);}\n"
"")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(780, 140, 200, 80))
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
        self.pushButton_3.setText(QCoreApplication.translate("Agent_choose", u"president", None))
        self.pushButton_4.setText(QCoreApplication.translate("Agent_choose", u"president", None))
        self.pushButton_5.setText(QCoreApplication.translate("Agent_choose", u"president", None))
        self.exit_button.setText("")
    # retranslateUi

