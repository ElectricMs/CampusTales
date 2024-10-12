# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_model_1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resource.resource1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"border-image: url(:/image1/resource/classroom.png);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 510, 1280, 211))
        self.frame.setStyleSheet(u"#frame{\n"
"        border-image: url(:/image1/resource/message.png);\n"
"    }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(70, 0, 271, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_name.setStyleSheet(u"#label{letter-spacing:5px;}")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_content = QLabel(self.frame)
        self.label_content.setObjectName(u"label_content")
        self.label_content.setGeometry(QRect(50, 60, 581, 51))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_content.setFont(font1)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(930, 140, 100, 35))
        self.pushButton_4.setStyleSheet(u"border-image: url(:/image2/resource/qload.png);")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1050, 140, 100, 35))
        self.pushButton_5.setStyleSheet(u"border-image: url(:/image2/resource/title.png);")
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1170, 140, 100, 35))
        self.pushButton_6.setStyleSheet(u"border-image: url(:/image2/resource/screen.png);")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(810, 140, 100, 35))
        self.pushButton_7.setStyleSheet(u"border-image: url(:/image2/resource/qsave.png);")
        self.pushButton_option1 = QPushButton(self.centralwidget)
        self.pushButton_option1.setObjectName(u"pushButton_option1")
        self.pushButton_option1.setGeometry(QRect(360, 100, 581, 81))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(15)
        self.pushButton_option1.setFont(font2)
        self.pushButton_option1.setStyleSheet(u"#pushButton{\n"
"    image: url(:/image1/resource/button.png);\n"
"    background-color:transparent;\n"
"    border:None;\n"
"    }\n"
"    #pushButton:hover{\n"
"        image: url(:/image1/resource/button2.png);\n"
"    }\n"
"    #pushButton:pressed{\n"
"        image:url(:/image1/resource/button3.png);\n"
"    }")
        self.pushButton_option2 = QPushButton(self.centralwidget)
        self.pushButton_option2.setObjectName(u"pushButton_option2")
        self.pushButton_option2.setGeometry(QRect(360, 170, 581, 81))
        self.pushButton_option2.setFont(font2)
        self.pushButton_option2.setStyleSheet(u"#pushButton_2{\n"
"    image: url(:/image1/resource/button.png);\n"
"    background-color:transparent;\n"
"    border:None;\n"
"    }\n"
"    #pushButton_2:hover{\n"
"        image: url(:/image1/resource/button2.png);\n"
"    }\n"
"    #pushButton_2:pressed{\n"
"        image:url(:/image1/resource/button3.png);\n"
"    }")
        self.pushButton_option3 = QPushButton(self.centralwidget)
        self.pushButton_option3.setObjectName(u"pushButton_option3")
        self.pushButton_option3.setGeometry(QRect(360, 240, 581, 81))
        font3 = QFont()
        font3.setPointSize(15)
        self.pushButton_option3.setFont(font3)
        self.pushButton_option3.setStyleSheet(u"#pushButton_3{\n"
"    image: url(:/image1/resource/button.png);\n"
"    background-color:transparent;\n"
"    border:None;\n"
"    }\n"
"    #pushButton_3:hover{\n"
"        image: url(:/image1/resource/button2.png);\n"
"    }\n"
"    #pushButton_3:pressed{\n"
"        image:url(:/image1/resource/button3.png);\n"
"    }")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 220, 450, 450))
        self.label_6.setStyleSheet(u"border-image: url(:/people/resource/girl_smile-removebg-preview.png);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 220, 450, 450))
        self.label_8.setStyleSheet(u"border-image: url(:/people/resource/girl_shy-removebg-preview (2).png);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(860, 200, 500, 500))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"border-image: url(:/people/resource/boy_normal_-removebg-preview.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.frame.raise_()
        self.pushButton_option1.raise_()
        self.pushButton_option2.raise_()
        self.pushButton_option3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"choose_model", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u7fe0\u82b1", None))
        self.label_content.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u957f\u4f60\u597d\uff0c\u6211\u60f3\u7ade\u9009\u4eca\u5e74\u7684\u5b66\u751f\u4f1a\u4e3b\u5e2d\uff0c\u80fd\u7ed9\u6211\u4e00\u70b9\u6307\u5bfc\u5417\uff1f", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_option1.setText(QCoreApplication.translate("MainWindow", u"\u597d\uff0c\u4eca\u5929\u665a\u4e0a\u6211\u4eec\u4e00\u8d77\u53bb\u81ea\u4e60\u5ba4\u5427", None))
        self.pushButton_option2.setText(QCoreApplication.translate("MainWindow", u"\u597d\uff0c\u4eca\u5929\u665a\u4e0a\u6211\u4eec\u4e00\u8d77\u53bb\u81ea\u4e60\u5ba4\u5427", None))
        self.pushButton_option3.setText(QCoreApplication.translate("MainWindow", u"\u597d\uff0c\u4eca\u5929\u665a\u4e0a\u6211\u4eec\u4e00\u8d77\u53bb\u81ea\u4e60\u5ba4\u5427", None))
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_7.setText("")
    # retranslateUi

