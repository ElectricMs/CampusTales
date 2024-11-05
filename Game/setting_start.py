from PySide6.QtCore import Qt,QEvent,QRect,QCoreApplication
from PySide6.QtGui import QMouseEvent,QFont,QFocusEvent
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QLabel,QHBoxLayout,QLineEdit,QButtonGroup,QFrame
from UI_resource.Ui_setting import Ui_MainWindow
#from cover_start import change_sound
InteractionTimerInterval=50
TextTimerInterval=100
AnimationTimerInterval=100
def high_speed():
    global InteractionTimerInterval
    InteractionTimerInterval=25
    global TextTimerInterval
    TextTimerInterval=50
    global AnimationTimerInterval
    AnimationTimerInterval=50
    print("当前是文字高速")
def low_speed():
    global InteractionTimerInterval
    InteractionTimerInterval=100
    global TextTimerInterval
    TextTimerInterval=200
    global AnimationTimerInterval
    AnimationTimerInterval=200
    print("当前是文字低速")
def middle_speed():
    global InteractionTimerInterval
    InteractionTimerInterval=50
    global TextTimerInterval
    TextTimerInterval=100
    global AnimationTimerInterval
    AnimationTimerInterval=100
    print("当前是文字中速")
class lineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText('给自己起个名字吧~')

        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(14)
        self.setFont(font3)
        self.setReadOnly(True)  #设置只读
        self.resize(250,51)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)  #关闭右键上下菜单
        
    def mousePressEvent(self, arg__1: QMouseEvent) -> None:  #单击
        if arg__1.button() == Qt.MouseButton.RightButton:  #右键点击
            self.setReadOnly(True)
	
    def mouseDoubleClickEvent(self, arg__1:QMouseEvent) -> None:  #双击
        if arg__1.button() == Qt.MouseButton.LeftButton:  #左键双击
            self.setReadOnly(False)
        super().mouseDoubleClickEvent(arg__1)

    def focusOutEvent(self, arg__1: QFocusEvent) -> None:  #失去焦点
        self.setReadOnly(True)
        super().focusOutEvent(arg__1)

class MyWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.name_lineEdit = lineEdit()
        self.name_lineEdit.setParent(self.ui.centralwidget)
        self.name_lineEdit.setStyleSheet(u"background-color: transparent;\n")
        self.name_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文字居中对齐
                                        #  "border: 2px solid #bcf0c4;")
        # self.label_2.setObjectName(u"label_2")
        self.name_lineEdit.setGeometry(QRect(340, 170, 200, 41))

        self.frame = QFrame()
        self.frame.setParent(self.ui.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 160, 900, 300))
        font4 = QFont()
        font4.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.frame.setFont(font4)
        self.frame.setStyleSheet(u"#frame{\n"
"	border-image: url(:/image/resource/\u5f39\u7a97.png);}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 50, 361, 81))
        font2 = QFont()
        font2.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 180, 161, 61))
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(22)
        font5.setBold(True)
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"#pushButton{border-image: url(:/image/resource/Strength_assign/002_07.png);}\n"
"#pushButton:hover{border-image: url(:/image/resource/Strength_assign/002_07_hover.png);}\n"
"#pushButton:pressed{border-image: url(:/image/resource/Strength_assign/002_07_click.png);}\n"
"\n"
"")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8bbe\u7f6e\u5df2\u4fdd\u5b58", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        
        self.pushButton.clicked.connect(self.confirm)
        #self.name_lineEdit.show()
        self.ui.label_2.setVisible(False)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setValue(60)
        self.ui.label.setText("60")
        self.ui.label.setFont(QFont("Sanserif", 15))
        self.ui.horizontalSlider.valueChanged.connect(self.changedValue)
        
        self.ui.high_speed_button.clicked.connect(high_speed)
        self.ui.middle_speed_button.clicked.connect(middle_speed)
        self.ui.low_speed_button.clicked.connect(low_speed)
        self.ui.save_button.clicked.connect(self.save_setting)

        self.mainWindow=None
        self.allocateEnergy=None
        self.button_group=QButtonGroup(self)
        self.button_group.addButton(self.ui.high_speed_button)
        self.button_group.addButton(self.ui.low_speed_button)
        self.button_group.addButton(self.ui.middle_speed_button)
        # 设置按钮为可选中
        self.ui.high_speed_button.setCheckable(True)
        self.ui.low_speed_button.setCheckable(True)
        self.ui.middle_speed_button.setCheckable(True)
        # 默认选择第一个按钮
        self.ui.middle_speed_button.setChecked(True)
        # self.ui.name_lineEdit.setReadOnly(True)
        self.frame.setVisible(False)


    def set_allocateEnergy_instance(self,allocateEnergy_instance):
        self.allocateEnergy=allocateEnergy_instance

    def set_mainWindow_instance(self, mainWindow_instance):
        self.mainWindow = mainWindow_instance    

    def save_setting(self):
        self.frame.setVisible(True)
        value=float(self.ui.horizontalSlider.value())
        if self.mainWindow:
            self.mainWindow.change_sound(value)
        else:
            print("B instance not set")
        if self.allocateEnergy:
            if self.name_lineEdit.text()=="":
                
                return
            else:
                self.allocateEnergy.change_name(self.name_lineEdit.text())
        else:
            print("allocateEnergy instance not set")
        
        # print(self.name_lineEdit.text())
        # print(self.ui.horizontalSlider.value())
        
    def confirm(self):
        self.frame.setVisible(False)
        self.name_lineEdit.setReadOnly(True)

    def changedValue(self):
        
        size = self.ui.horizontalSlider.value()
        # change_sound(float(size))
        self.ui.label.setText(str(size))
   
if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
   
    window.show()
    app.exec()