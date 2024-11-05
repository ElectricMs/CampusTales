# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QMouseEvent,QFocusEvent,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QWidget,QLineEdit)
import resource.resource2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font.setPointSize(36)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#centralwidget{background-color: #e6f3f3;}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(40, 10, 271, 101))
        font1 = QFont()
        font1.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font1.setPointSize(48)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(80, 150, 201, 81))
        font2 = QFont()
        font2.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.name_label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 170, 151, 41))
        
        self.speed_label = QLabel(self.centralwidget)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setGeometry(QRect(80, 270, 201, 81))
        self.speed_label.setFont(font2)
        self.sound_label = QLabel(self.centralwidget)
        self.sound_label.setObjectName(u"sound_label")
        self.sound_label.setGeometry(QRect(80, 390, 201, 81))
        self.sound_label.setFont(font2)
        self.teach_label = QLabel(self.centralwidget)
        self.teach_label.setObjectName(u"teach_label")
        self.teach_label.setGeometry(QRect(80, 510, 201, 81))
        self.teach_label.setFont(font2)
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(1020, 660, 100, 35))
        self.save_button.setStyleSheet(u"#save_button{\n"
"	border-image: url(:/image/resource/save_button2.png);}\n"
"#save_button:hover{\n"
"	border-image: url(:/image/resource/save_hover.png);}")
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(1150, 660, 100, 35))
        self.exit_button.setStyleSheet(u"#exit_button{\n"
"	border-image: url(:/image/resource/exit_button2.png);}\n"
"#exit_button:hover{\n"
"	border-image: url(:/image/resource/exit_hover.png);}")
        self.view_button = QPushButton(self.centralwidget)
        self.view_button.setObjectName(u"view_button")
        self.view_button.setGeometry(QRect(340, 520, 141, 51))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.view_button.setFont(font3)
        self.view_button.setStyleSheet(u"#view_button{background:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 #e4f1f3,stop:1#bcf0c4);\n"
"border-radius:12px;}\n"
"#view_button:hover{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}")
        self.high_speed_button = QPushButton(self.centralwidget)
        self.high_speed_button.setObjectName(u"high_speed_button")
        self.high_speed_button.setGeometry(QRect(340, 280, 141, 51))
        self.high_speed_button.setFont(font3)
        self.high_speed_button.setStyleSheet(u"#high_speed_button{background:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 #e4f1f3,stop:1#bcf0c4);\n"
"border-radius:12px;}\n"
"#high_speed_button:hover{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}\n"
"\n"
"#high_speed_button:checked{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}")
        self.middle_speed_button = QPushButton(self.centralwidget)
        self.middle_speed_button.setObjectName(u"middle_speed_button")
        self.middle_speed_button.setGeometry(QRect(570, 280, 141, 51))
        self.middle_speed_button.setFont(font3)
        self.middle_speed_button.setStyleSheet(u"#middle_speed_button{background:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 #e4f1f3,stop:1#bcf0c4);\n"
"border-radius:12px;}\n"
"#middle_speed_button:hover{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}\n"
"\n"
"#middle_speed_button:checked{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}")
        self.low_speed_button = QPushButton(self.centralwidget)
        self.low_speed_button.setObjectName(u"low_speed_button")
        self.low_speed_button.setGeometry(QRect(800, 280, 141, 51))
        self.low_speed_button.setFont(font3)
        self.low_speed_button.setStyleSheet(u"#low_speed_button{background:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 #e4f1f3,stop:1#bcf0c4);\n"
"border-radius:12px;}\n"
"#low_speed_button:hover{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}\n"
"\n"
"#low_speed_button:checked{\n"
"background:#bcf0c4;\n"
"border-radius:12px;}")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(340, 420, 551, 16))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(910, 400, 50, 51))
 
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"SETTING", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5b57\u901f\u5ea6", None))
        self.sound_label.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u97f3\u91cf", None))
        self.teach_label.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u6559\u7a0b", None))
        self.save_button.setText("")
        self.exit_button.setText("")
        self.view_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.high_speed_button.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f", None))
        self.middle_speed_button.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901f", None))
        self.low_speed_button.setText(QCoreApplication.translate("MainWindow", u"\u6162\u901f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"100", None))
        
    # retranslateUi

