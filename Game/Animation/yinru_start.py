from PySide6.QtCore import Qt,QEvent,QTimer, Qt,QRect,QUrl
from PySide6.QtGui import QMouseEvent,QFont,QKeyEvent
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QLabel,QPlainTextEdit
from PySide6.QtMultimedia import QSoundEffect
from Animation.Ui_yinru import Ui_Page1
import Animation.resoure_main_rc
import sys
import os


class CustomPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.read_only = False  # 初始化为非只读状态
        self.setPlaceholderText("给自己起个名字吧~")
    def keyPressEvent(self, event: QKeyEvent):
        # print("文本编辑框keyPressEvent被执行")
        
        if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
            
            #print("Enter 键被按下，设置为只读")
            self.setVisible(False)
            self.setReadOnly(True)
            self.read_only = True  # 记录当前状态
            #print("名字是"+self.toPlainText())
        else:
           
            super().keyPressEvent(event)
        # 手动传递事件给 MainWindow
        main_window = self.parent()
        if isinstance(main_window, QMainWindow):
            main_window.keyPressEvent(event)
class MyWindow(QMainWindow):
    def __init__(self,callback):
        
        super().__init__()
        self.ui=Ui_Page1()
        self.ui.setupUi(self)
        self.page=-1
        self.current_index = 0
        self.callback_setCurrentIndex_allocateEnergy = callback
        # 创建一个QSoundEffect实例来播放音效
        self.sound_effect = QSoundEffect(self)

        def resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        audio_file_path = resource_path('Game\Animation\typing.wav')

        self.sound_effect.setSource(QUrl.fromLocalFile(audio_file_path)) 
        print("typing sounds set successfully")
        self.sound_effect.setVolume(0.6)
        self.ui.test_pushButton.setVisible(False)
        self.ui.test_pushButton.clicked.connect(self.start_flow_text)
        self.label_list=[]
        self.text_list=[]
        for label in self.ui.centralwidget.findChildren(QLabel):
            self.label_list.append(label)
            self.text_list.append(label.text())
            label.setText("")
        # print(self.text_list)
        self.count=0
        self.plainTextEdit = CustomPlainTextEdit(self)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(360, 310, 561, 64))
        font3 = QFont()
        font3.setPointSize(22)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"\n"
" QPlainTextEdit {\n"
"				color:white;\n"
"                border: 2px solid white;  /* \u8fb9\u6846\u5bbd\u5ea6\u4e3a2\u50cf\u7d20\uff0c\u989c\u8272\u4e3a\u7ea2\u8272 */				background-color:black;\n"
"                padding: 5px;               /* \u5185\u8fb9\u8ddd\uff0c\u53ef\u9009 */\n"
" }")   
        self.plainTextEdit.setVisible(False)
        self.mainwindow=None
    def set_mainwindow_instance(self,mainwindow_instance):
        self.mainwindow=mainwindow_instance
    def call_allocateEnergy_method(self):

        if self.mainwindow:
            if self.plainTextEdit.toPlainText()=="":
                return
            else:
                self.mainwindow.change_name(self.plainTextEdit.toPlainText())
        else:
            print("allocateEnergy instance not set")
        
          
    def keyPressEvent(self,event):
        #print("yinru页面的keyPressEvent被执行")
        
        # 当按下键时，此方法被调用
        #self.setGeometry(300, 300, 300, 300)
        key=event.key()
        if key==Qt.Key.Key_Return and self.page==3:
            self.change3()
            return
        if self.page==5:
            self.change_namepage()
            
        if self.page==1:
            self.change1()
        if self.page==3 and key==Qt.Key.Key_S:
            # print("S键被按下")
            self.callback_setCurrentIndex_allocateEnergy()
            self.page=-1
            self.stop_sound()
        if self.page==4:
            self.callback_setCurrentIndex_allocateEnergy()
            self.page=-1
            self.stop_sound()
    
        
    def play_sound(self):
        # 播放音效
        self.sound_effect.play()
        # 可以更新界面或其他操作
    def stop_sound(self):
        self.sound_effect.stop()

    def start_flow_text(self):
        from setting_start import AnimationTimerInterval
        self.count=0
        self.current_index=0
        self.play_sound()
        def update_text():
            if self.current_index < len(self.text_list[self.count]):
                self.label_list[self.count].setText(self.text_list[self.count][:self.current_index + 1])
                self.current_index += 1
            else:
                self.count+=1
                self.current_index=0
            if self.count==len(self.text_list):
                
                self.stop_sound()
                self.timer.stop()
            
        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(update_text)
            self.timer.setInterval(AnimationTimerInterval)
            self.timer.start()
        else:
            self.timer.stop()
            self.timer = QTimer(self)
            self.timer.timeout.connect(update_text)
            self.timer.setInterval(AnimationTimerInterval)
            self.timer.start()



    def name_page(self):
        self.page=5
        name_label = QLabel("请为您的角色起一个名字",self.ui.centralwidget)
        name_label.setObjectName(u"name_label")
        name_label.setGeometry(QRect(330, 170, 621, 111))
        font2 = QFont()
        font2.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font2.setPointSize(41)
        font2.setBold(True)
        name_label.setFont(font2)
        name_label.setStyleSheet(u"#name_label{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        
        
        self.plainTextEdit.setVisible(True)# type: ignore
        next_label = QLabel("按Enter键继续下一步",self.ui.centralwidget)
        next_label.setObjectName(u"next_label")
        next_label.setGeometry(QRect(500, 620, 331, 51))
        font = QFont()
        font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font.setPointSize(24)
        next_label.setFont(font)
        next_label.setStyleSheet(u"#next_label{\n"
"	color: rgb(255, 255, 255);\n"
"	}")
        for label in self.ui.centralwidget.findChildren(QLabel):
            self.label_list.append(label)
            self.text_list.append(label.text())
            label.setText("")
        #print(self.text_list)
        
        self.start_flow_text()
        
        name_label.show()
        next_label.show()
   

    def change1(self):
        self.stop_sound()
        self.label_list=[]
        self.text_list=[]
        #遍历所有子控件并删除它们
        for label in self.ui.centralwidget.findChildren(QLabel):
            label.setParent(None)
            label.deleteLater()
            label = None
        for button in self.ui.centralwidget.findChildren(QPushButton):
            button.setParent(None)
            button.deleteLater()
            button=None
        # self.ui.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        # self.setWindowTitle("Page1")
        self.name_page()
        # print("change1结束")
    def change_namepage(self):
        self.stop_sound()
        self.label_list=[]
        self.text_list=[]
        #遍历所有子控件并删除它们
        for label in self.ui.centralwidget.findChildren(QLabel):
            label.setParent(None)
            label.deleteLater()
            label = None
        for button in self.ui.centralwidget.findChildren(QPushButton):
            button.setParent(None)
            button.deleteLater()
            button=None
        self.plainTextEdit.setVisible(False)
        self.call_allocateEnergy_method()
        
        self.Page3()
        # print("change_name结束")
    
            
    # def Page2_label(self):
    #     self.page=2
        
    #     label1 = QLabel("请选择你的性别", self.ui.centralwidget)
    #     label1.setGeometry(QRect(390, 210, 531, 141))
    #     font = QFont()
    #     font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
    #     font.setPointSize(54)
    #     label1.setFont(font)
    #     label1.setStyleSheet(u"color: rgb(255, 255, 255);")
    #     #label.setText("请选择你的性别")
    #     label1.show()
    #     for label in self.ui.centralwidget.findChildren(QLabel):
    #         self.label_list.append(label)
    #         self.text_list.append(label.text())
    #         label.setText("")
    #     #print(self.text_list)
    #     label.show()
    #     self.start_flow_text()
    # def Page2_button(self):
    #     font = QFont()
    #     font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
    #     font.setPointSize(54)
    #     pushButton = QPushButton("男",self.ui.centralwidget)
    #     #pushButton.setObjectName(u"pushButton")
    #     pushButton.setGeometry(QRect(500, 410, 75, 81))
    #     pushButton.setFont(font)
    #     pushButton.setStyleSheet(u"background-color: transparent;\n"
    #     "color:rgb(255, 255, 255);")
        
    #     pushButton.show()
    #     pushButton.clicked.connect(self.man)
    #     pushButton.clicked.connect(self.change2)
    #     pushButton_2 = QPushButton("女",self.ui.centralwidget)
    #     #pushButton_2.setObjectName(u"pushButton_2")
    #     pushButton_2.setGeometry(QRect(720, 410, 75, 81))
    #     pushButton_2.setFont(font)
    #     pushButton_2.setStyleSheet(u"background-color: transparent;\n"
    #     "color:rgb(255, 255, 255);")
    #     pushButton_2.show()
    #     pushButton_2.clicked.connect(self.woman)
    #     pushButton_2.clicked.connect(self.change2)
    # def change2(self):
    #     self.stop_sound()
    #     self.label_list=[]
    #     self.text_list=[]
    #     #遍历所有子控件并删除它们
    #     for label in self.ui.centralwidget.findChildren(QLabel):
    #         label.setParent(None)
    #         label.deleteLater()
    #         label = None
    #     for button in self.ui.centralwidget.findChildren(QPushButton):
    #         button.setParent(None)
    #         button.deleteLater()
    #         button=None
    #     self.Page3()
        

        
    def Page3(self):
        self.page=3
        label1 = QLabel("",self.ui.centralwidget)
        label1.setObjectName(u"label1")
        label1.setGeometry(QRect(350, 130, 581, 201))
        label1.setStyleSheet(u"border-image: url(:/image/resource/\u6211\u7684\u5927\u5b66.png);")
        label1.show()
        explain_button = QLabel("按Enter键查看游戏介绍",self.ui.centralwidget)
        explain_button.setObjectName(u"explain_button")
        explain_button.setGeometry(QRect(430, 370, 421, 61))
        font3 = QFont()
        font3.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font3.setPointSize(30)
        font3.setBold(True)
        explain_button.setFont(font3)
        explain_button.setStyleSheet(u"#explain_button{color: rgb(255, 255, 255);}")
        explain_button.show()
        start_button = QLabel("按S开始游戏",self.ui.centralwidget)
        start_button.setObjectName(u"start_button")
        start_button.setGeometry(QRect(530, 490, 231, 61))
        start_button.setFont(font3)
        start_button.setStyleSheet(u"#start_button{color: rgb(255, 255, 255);}")
        for label in self.ui.centralwidget.findChildren(QLabel):
            self.label_list.append(label)
            self.text_list.append(label.text())
            label.setText("")
        #print(self.text_list)
        
        self.start_flow_text()
        start_button.show()
        
    def change3(self):
        self.stop_sound()
        self.label_list=[]
        self.text_list=[]
        #遍历所有子控件并删除它们
        for label in self.ui.centralwidget.findChildren(QLabel):
            label.setParent(None)
            label.deleteLater()
            label = None
        for button in self.ui.centralwidget.findChildren(QPushButton):
            button.setParent(None)
            button.deleteLater()
            button=None
        self.Page4()
    def Page4(self):
        self.page=4
        label_1 = QLabel("游戏介绍：",self.ui.centralwidget)
        label_1.setObjectName(u"label")
        label_1.setGeometry(QRect(20, 10, 261, 81))
        
        font1 = QFont()
        font1.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font1.setPointSize(38)
        label_1.setFont(font1)
        label_1.setStyleSheet(u"#label{\n"
"	color: rgb(255, 255, 255);\n"
"	}")
        
        label_2 = QLabel("这是一个模拟大学生活的游戏",self.ui.centralwidget)
        label_2.setObjectName(u"label_2")
        label_2.setGeometry(QRect(420, 120, 431, 81))
        font = QFont()
        font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font.setPointSize(24)
        label_2.setFont(font)
        label_2.setStyleSheet(u"#label_2{\n"
"	color: rgb(255, 255, 255);\n"
"	}")
        label_3 = QLabel("在进入游戏后，你将遇到许多校园生活中的特殊事件",self.ui.centralwidget)
        label_3.setObjectName(u"label_4")
        label_3.setGeometry(QRect(270, 210, 811, 81))
        label_3.setFont(font)
        label_3.setStyleSheet(u"#label_4{\n"
"	color: rgb(255, 255, 255);\n"
"	}")
        label_4 = QLabel("你能够把你的金钱和精力，自由地分配到各种日常活动当中，",self.ui.centralwidget)
        label_4.setObjectName(u"label_5")
        label_4.setGeometry(QRect(220, 300, 871, 71))
        label_4.setFont(font)
        label_4.setStyleSheet(u"#label_5{\n"
"	color: rgb(255, 255, 255);\n"
"	}")
        label_5 = QLabel("创造一个独属于你的、个性化的大学生活。",self.ui.centralwidget)
        label_5.setObjectName(u"label_3")
        label_5.setGeometry(QRect(360, 390, 591, 61))
        label_5.setFont(font)
        label_5.setStyleSheet(u"#label_3{\n"
"	color: rgb(255, 255, 255);\n"
"	}")
       
        
        
        
        
        label_6 = QLabel("PS：游戏中隐藏着许多未知的智能角色，待您逐一解锁~",self.ui.centralwidget)
        label_6.setObjectName(u"label_6")
        label_6.setGeometry(QRect(240, 490, 791, 51))
        label_6.setFont(font)
        label_6.setStyleSheet(u"#label_6{color: rgb(255, 255, 255);}")
        label_7 = QLabel("按任意键开始游戏......",self.ui.centralwidget)
        label_7.setObjectName(u"label_7")
        label_7.setGeometry(QRect(520, 640, 331, 51))
        label_7.setFont(font)
        label_7.setStyleSheet(u"#label_7{color: rgb(255, 255, 255);}")
        for label in self.ui.centralwidget.findChildren(QLabel):
            self.label_list.append(label)
            self.text_list.append(label.text())
            label.setText("")
        #print(self.text_list)
        
        self.start_flow_text()
        label_1.show()
        label_2.show()
        label_3.show()
        
        label_4.show()
        label_5.show()
        label_6.show()
        label_7.show()
if __name__=="__main__":
    gender=0
    app=QApplication([])
    window=MyWindow(callback = None)
    window.show()
    
    
    
    app.exec()