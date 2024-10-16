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
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)
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
        self.label_content.setGeometry(QRect(30, 70, 711, 71))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_content.setFont(font1)
        self.label_content.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_content.setWordWrap(True)
        self.pushButton_save = QPushButton(self.frame)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(1050, 140, 100, 35))
        self.pushButton_save.setStyleSheet(u"#pushButton_save{\n"
"	border-image: url(:/image2/resource/save_button2.png);}\n"
"#pushButton_save:hover{\n"
"	border-image: url(:/image2/resource/save_hover.png);}")
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(1170, 140, 100, 35))
        self.pushButton_exit.setStyleSheet(u"#pushButton_exit{\n"
"	border-image: url(:/image2/resource/exit_button2.png);}\n"
"#pushButton_exit:hover{\n"
"border-image: url(:/image2/resource/exit_hover.png);}")
        self.pushButton_next = QPushButton(self.frame)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(930, 140, 100, 35))
        self.pushButton_next.setStyleSheet(u"#pushButton_next{\n"
"border-image: url(:/image2/resource/next_button.png);\n"
"}\n"
"#pushButton_next:hover{\n"
"	border-image: url(:/image2/resource/next_button2.png);\n"
"}")
        self.plainTextEdit_input = QPlainTextEdit(self.frame)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit_input")
        self.plainTextEdit_input.setGeometry(QRect(30, 70, 711, 71))
        font2 = QFont()
        font2.setPointSize(15)
        self.plainTextEdit_input.setFont(font2)
        self.plainTextEdit_input.setStyleSheet(u"#plainTextEdit_input{\n"
"background-color:transparent;\n"
"border:None;\n"
"}")
        self.pushButton_option1 = QPushButton(self.centralwidget)
        self.pushButton_option1.setObjectName(u"pushButton_option1")
        self.pushButton_option1.setGeometry(QRect(360, 100, 581, 81))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(15)
        self.pushButton_option1.setFont(font3)
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
        self.pushButton_option2.setFont(font3)
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
        self.pushButton_option3.setFont(font2)
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
        self.label_img_left = QLabel(self.centralwidget)
        self.label_img_left.setObjectName(u"label_img_left")
        self.label_img_left.setGeometry(QRect(0, 220, 450, 450))
        self.label_img_left.setStyleSheet(u"border-image: url(:/people/resource/girl_smile-removebg-preview.png);")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 220, 450, 450))
        self.label_8.setStyleSheet(u"border-image: url(:/people/resource/girl_shy-removebg-preview (2).png);")
        self.label_img_right = QLabel(self.centralwidget)
        self.label_img_right.setObjectName(u"label_img_right")
        self.label_img_right.setGeometry(QRect(860, 200, 500, 500))
        self.label_img_right.setFont(font2)
        self.label_img_right.setStyleSheet(u"border-image: url(:/people/resource/boy_normal_-removebg-preview.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_img_left.raise_()
        self.label_8.raise_()
        self.label_img_right.raise_()
        self.frame.raise_()
        self.pushButton_option1.raise_()
        self.pushButton_option2.raise_()
        self.pushButton_option3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"choose_model", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Narrator", None))
        self.label_content.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.pushButton_save.setText("")
        self.pushButton_exit.setText("")
        self.pushButton_next.setText("")
        self.plainTextEdit_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e0a\u65b9\u7684\u9009\u9879\uff0c\u6216\u8005\u5728\u6b64\u8f93\u5165\u4f60\u7684\u4e2a\u6027\u5316\u56de\u7b54~", None))
        self.pushButton_option1.setText(QCoreApplication.translate("MainWindow", u"Option1", None))
        self.pushButton_option2.setText(QCoreApplication.translate("MainWindow", u"Option2", None))
        self.pushButton_option3.setText(QCoreApplication.translate("MainWindow", u"Option3", None))
        self.label_img_left.setText("")
        self.label_8.setText("")
        self.label_img_right.setText("")
    # retranslateUi

