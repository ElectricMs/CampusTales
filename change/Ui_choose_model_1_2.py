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
import resource1_rc_2

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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 271, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"#label{letter-spacing:5px;}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 60, 581, 51))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(15)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.next_button = QPushButton(self.frame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(930, 140, 100, 35))
        self.next_button.setStyleSheet(u"#next_button{border-image: url(:/image2/resource/next_button.png);}\n"
"#next_button:hover{\n"
"	border-image: url(:/image2/resource/next_button2.png);}")
        self.save_button = QPushButton(self.frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(1050, 140, 100, 35))
        self.save_button.setStyleSheet(u"#save_button{\n"
"	border-image: url(:/image2/resource/save_button2.png);}\n"
"#save_button:hover{\n"
"	border-image: url(:/image2/resource/save_hover.png);}")
        self.exit_button = QPushButton(self.frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(1170, 140, 100, 35))
        self.exit_button.setStyleSheet(u"#exit_button{\n"
"	border-image: url(:/image2/resource/exit_button2.png);}\n"
"#exit_button:hover{\n"
"	border-image: url(:/image2/resource/exit_hover.png);}")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(40, 70, 851, 111))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(15)
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setStyleSheet(u"#plainTextEdit{\n"
"background-color:transparent;\n"
"border:None;}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 100, 581, 81))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"#pushButton{\n"
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
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 170, 581, 81))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"#pushButton_2{\n"
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
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(360, 240, 581, 81))
        font3 = QFont()
        font3.setPointSize(15)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"#pushButton_3{\n"
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
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"choose_model", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7fe0\u82b1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u957f\u4f60\u597d\uff0c\u6211\u60f3\u7ade\u9009\u4eca\u5e74\u7684\u5b66\u751f\u4f1a\u4e3b\u5e2d\uff0c\u80fd\u7ed9\u6211\u4e00\u70b9\u6307\u5bfc\u5417\uff1f", None))
        self.next_button.setText("")
        self.save_button.setText("")
        self.exit_button.setText("")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e0a\u65b9\u7684\u9009\u9879\uff0c\u6216\u8005\u5728\u6b64\u8f93\u5165\u4f60\u7684\u4e2a\u6027\u5316\u56de\u7b54~", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u597d\uff0c\u4eca\u5929\u665a\u4e0a\u6211\u4eec\u4e00\u8d77\u53bb\u81ea\u4e60\u5ba4\u5427", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u597d\uff0c\u4eca\u5929\u665a\u4e0a\u6211\u4eec\u4e00\u8d77\u53bb\u81ea\u4e60\u5ba4\u5427", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u597d\uff0c\u4eca\u5929\u665a\u4e0a\u6211\u4eec\u4e00\u8d77\u53bb\u81ea\u4e60\u5ba4\u5427", None))
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_7.setText("")
    # retranslateUi

