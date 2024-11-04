from PySide6.QtCore import Qt,QEvent,QRect
from PySide6.QtGui import QMouseEvent,QFont,QFocusEvent
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QLabel,QHBoxLayout,QLineEdit
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
        self.setPlaceholderText('请输入：')

        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(14)
        self.setFont(font3)
        self.setReadOnly(True)  #设置只读
        self.resize(250,51)
        self.setText("your name")
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
        self.name_lineEdit.setGeometry(QRect(340, 170, 151, 41))
        self.name_lineEdit.show()
        self.ui.label_2.setVisible(False)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setValue(60)
        self.ui.label.setText("60")
        self.ui.label.setFont(QFont("Sanserif", 15))
        self.ui.horizontalSlider.valueChanged.connect(self.changedValue)
        
        self.ui.high_speed_button.clicked.connect(high_speed)
 
        self.ui.low_speed_button.clicked.connect(low_speed)
        self.ui.save_button.clicked.connect(self.save_setting)

        self.mainWindow=None
        self.allocateEnergy=None
    def set_allocateEnergy_instance(self,allocateEnergy_instance):
        self.allocateEnergy=allocateEnergy_instance
   

        

    def set_mainWindow_instance(self, mainWindow_instance):
        self.mainWindow = mainWindow_instance    

    def save_setting(self):
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

        
        print(self.name_lineEdit.text())
        print(self.ui.horizontalSlider.value())
    def changedValue(self):
        
        size = self.ui.horizontalSlider.value()
        # change_sound(float(size))
        self.ui.label.setText(str(size))
   
if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()