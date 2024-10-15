from PySide6.QtCore import Qt,QEvent,QTimer, QEasingCurve, QPropertyAnimation, QVariantAnimation,QRect,QCoreApplication
from PySide6.QtGui import QMouseEvent,QFont
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QStackedLayout,QGraphicsOpacityEffect,QGraphicsBlurEffect,QFrame,QLabel
from UI_resource.Ui_cover import Ui_cover
from UI_resource.Ui_agent_choose import Ui_Agent_choose
from UI_resource.Ui_choose_model_1 import Ui_MainWindow as Ui_choose_model_1
from UI_resource.Ui_allocateEnergy import Ui_allocateEnergy
#全局变量用于存储每个任务的精力值
value_list=[]
#全局变量，用于实现Label的换页
count=0

#####我的UI
class GameLayout_choose_model_1(QMainWindow, Ui_choose_model_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #给这两个label设置透明度
        self.opacity_effect_6 = QGraphicsOpacityEffect()
        self.opacity_effect_8 = QGraphicsOpacityEffect()
        
        self.label_6.setGraphicsEffect(self.opacity_effect_6)
        self.label_8.setGraphicsEffect(self.opacity_effect_8)
        self.opacity_effect_8.setOpacity(0)
        self.opacity_effect_6.setOpacity(1)
        

    def set_stream_text(self, text):
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        self.current_index=0
        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(lambda:self.update_text_stream(str(text)))
            self.timer.start(50)  # 每50毫秒更新一次
        else:
            self.timer.start()

    def update_text_stream(self,text:str):
        if self.current_index < len(text):
            self.label_content.setText(text[:self.current_index + 1])
            self.current_index += 1
        else:
            self.timer.stop()


class GameLayout_allocateEnergy(QMainWindow, Ui_allocateEnergy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame.setVisible(False)
        self.add_diary_widget()

    
    def add_diary_widget(self):
        #每周展示diary的widget，包含许多组件
        self.widget_diary = QWidget(self)
        self.widget_diary.setVisible(False)
        self.widget_diary.setGeometry(0, 0, 1280, 720)
        # 背景图片
        self.label_diary_img = QLabel(self.widget_diary)
        self.label_diary_img.setGeometry(QRect(270, 30, 621, 661))
        self.label_diary_img.setStyleSheet(u"border-image: url(:/image/resource/Strength_assign/paper2_yellow_l.png);")
        # 内容
        self.label_diary_content = QLabel(self.widget_diary)
        self.label_diary_content.setGeometry(QRect(290, 50, 581, 561))
        # 字体 后面要重命名
        font_diaryWidget = QFont()
        font_diaryWidget.setFamilies([u"\u5343\u56fe\u7b14\u950b\u624b\u5199\u4f53"])
        font_diaryWidget.setPointSize(18)
        font_diaryWidget.setBold(True)
        self.label_diary_content.setFont(font_diaryWidget)
        self.label_diary_content.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        # self.widget_diary.label_content.setText(QCoreApplication.translate("strength_assignment", u"\u661f\u671f\u4e00      5\u670828\u65e5     \u6674", None))
        self.label_diary_content.setWordWrap(True)
        self.label_diary_content.setText("你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好")

        #模糊状态恢复测试按钮
        self.pushButton_test_blur = QPushButton(self.widget_diary)
        self.pushButton_test_blur.setGeometry(QRect(500, 180, 75, 24))
        self.pushButton_test_blur.setText("恢复")
        self.pushButton_test_blur.clicked.connect(self.blur_recover)
        
        #每周执行任务的内容widget,模糊背景
        self.next_button = QPushButton(self.widget_diary)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(700, 620, 171, 41))
        font10 = QFont()
        font10.setPointSize(16)
        font10.setBold(True)
        self.next_button.setFont(font10)
        self.next_button.setStyleSheet("#next_button{color:brown;\n"
            "background-color: rgb(255, 230, 0);}"
                    "#next_button:hover{color:brown;\n"
            "background-color: rgb(255, 200, 0);}"
                    "#next_button:pressed{color:brown;\n"
            "background-color: rgb(255, 170, 0);}"
        )
    
        
    # 点击nextWeek后，模糊背景，显示diary页面
    def blur(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(20)
        self.blur_effect.setBlurHints(QGraphicsBlurEffect.BlurHint.PerformanceHint)
        self.centralwidget.setGraphicsEffect(self.blur_effect)
        self.widget_diary.setVisible(True) # diary widget显示


    # 展示完最后一张日记后diary页面消失，显示能量分配界面
    def blur_recover(self):
        self.centralwidget.setGraphicsEffect(None)  # type: ignore
        self.widget_diary.setVisible(False)





class GameLayout_Agent(QMainWindow, Ui_Agent_choose):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
     
    

class GameLayout_MainMenu(QMainWindow, Ui_cover):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



class MyWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        
        self.resize(1280,720)
        
        self.stacked_layout = QStackedLayout()
        self.game_layout_main_menu = GameLayout_MainMenu()
        self.game_layout_Agent= GameLayout_Agent()
        self.game_layout_choose_model_1= GameLayout_choose_model_1()
        self.game_layout_allocateEnergy= GameLayout_allocateEnergy()

        
        self.stacked_layout.addWidget(self.game_layout_main_menu) 
        self.stacked_layout.addWidget(self.game_layout_Agent)
        self.stacked_layout.addWidget(self.game_layout_choose_model_1)
        self.stacked_layout.addWidget(self.game_layout_allocateEnergy)
        
        
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)
        
        self.bind()
        # 设置当前显示的布局为主菜单
        self.current_layout_index = 0
        self.stacked_layout.setCurrentIndex(self.current_layout_index)


    def bind(self):
        self.game_layout_main_menu.pushButton.clicked.connect(self.game_start)
        self.game_layout_main_menu.pushButton_4.clicked.connect(self.Agent_choose)
        self.game_layout_main_menu.pushButton_5.clicked.connect(self.close)
        self.game_layout_Agent.exit_button.clicked.connect(self.back)
        self.game_layout_allocateEnergy.pushButton_exit.clicked.connect(self.back)
        self.game_layout_allocateEnergy.pushButton_next.clicked.connect(self.nextWeek)
        self.game_layout_Agent.pushButton.clicked.connect(self.agent_girlfriend)
        self.game_layout_allocateEnergy.pushButton_yes.clicked.connect(self.event_true)
        self.game_layout_allocateEnergy.pushButton_no.clicked.connect(self.event_false)


    def Agent_choose(self):
        self.stacked_layout.setCurrentIndex(1)


    def choose_model_1(self):
        self.stacked_layout.setCurrentIndex(2)

    def game_start(self):
        self.stacked_layout.setCurrentIndex(3)
        from main import Game
        self.game = Game(self)
        self.game.start()
        # self.game_layout_diary.ui.misson_1.setText(self.game.start()+"不管怎样，我决定从现在开始记日记，这应该是个好习惯吧。")
        # 这里首先应该是黑屏的过场动画和基本选项选择 暂时先跳过
        def bind_afterGame():
            self.game_layout_allocateEnergy.pushButton_nextPage.clicked.connect(lambda: self.game.pageTuning(1))
            self.game_layout_allocateEnergy.pushButton_previousPage.clicked.connect(lambda: self.game.pageTuning(-1))
            
            self.game_layout_allocateEnergy.pushButton_minus1.clicked.connect(lambda: self.game.modifyEnergy(-1,1))
            self.game_layout_allocateEnergy.pushButton_minus2.clicked.connect(lambda: self.game.modifyEnergy(-1,2))
            self.game_layout_allocateEnergy.pushButton_minus3.clicked.connect(lambda: self.game.modifyEnergy(-1,3))
            self.game_layout_allocateEnergy.pushButton_minus4.clicked.connect(lambda: self.game.modifyEnergy(-1,4))
            self.game_layout_allocateEnergy.pushButton_minus5.clicked.connect(lambda: self.game.modifyEnergy(-1,5))
            self.game_layout_allocateEnergy.pushButton_plus1.clicked.connect(lambda: self.game.modifyEnergy(1,1))
            self.game_layout_allocateEnergy.pushButton_plus2.clicked.connect(lambda: self.game.modifyEnergy(1,2))
            self.game_layout_allocateEnergy.pushButton_plus3.clicked.connect(lambda: self.game.modifyEnergy(1,3))
            self.game_layout_allocateEnergy.pushButton_plus4.clicked.connect(lambda: self.game.modifyEnergy(1,4))
            self.game_layout_allocateEnergy.pushButton_plus5.clicked.connect(lambda: self.game.modifyEnergy(1,5))

        bind_afterGame()



    def event_true(self):
        self.game.event_true()

    def event_false(self):
        self.game.event_false()


    def nextWeek(self):
        print("next week")
        self.game.nextWeek()


    def back(self):
        self.stacked_layout.setCurrentIndex(0)

    def agent_girlfriend(self):
        from Event.crush_atFirstBlush import event_crush_atFirstBlush
        self.event_crush_atFirstBlush = event_crush_atFirstBlush(self.game)
        self.event_crush_atFirstBlush.event_start()
        
   

if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    # input_list=["睡觉","睡觉","睡觉"]
    # input_list=["睡觉","睡觉","睡觉","唱歌","跳舞","rap","打篮球"]
    # list1=input_list
    # input_list_length=len(list1)
    
    # for i in range(input_list_length):
    #     value_list.append(0)
    
    # window.game_layout_diary.ui.mission1_show.setText("")
    # window.game_layout_diary.ui.mission2_show.setText("")
    # window.game_layout_diary.ui.mission3_show.setText("")
    # window.game_layout_diary.ui.mission4_show.setText("")
    # window.game_layout_diary.ui.mission5_show.setText("")
    
    
    # #list初始化
    # label_list=window.game_layout_diary.get_label_list()
    # plus_button_list=window.game_layout_diary.get_plus_button_list()
    # minus_button_list=window.game_layout_diary.get_minus_button_list()
    # for i in range(5):
    #     label_list[i].setVisible(False)
    #     plus_button_list[i].setVisible(False)
    #     minus_button_list[i].setVisible(False)
    # bind()
    # if input_list_length<=5:
    #     for i in range(input_list_length):
    #         label_list[i].setText(list1[i]+"  0")
    #         label_list[i].setVisible(True)
    #         plus_button_list[i].setVisible(True)
    #         minus_button_list[i].setVisible(True)
        
            
    # else:
    #     for i in range(5):
    #         label_list[i].setText(list1[i]+"  0")
            
    #         label_list[i].setVisible(True)
    #         plus_button_list[i].setVisible(True)
    #         minus_button_list[i].setVisible(True)
        
    #     window.game_layout_diary.ui.left_button.clicked.connect(left_show)
    #     window.game_layout_diary.ui.right_button.clicked.connect(right_show)
    window.show()
    app.exec()