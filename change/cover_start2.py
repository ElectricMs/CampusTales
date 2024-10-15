from PySide6.QtCore import Qt,QEvent,QTimer, QEasingCurve, QPropertyAnimation, QVariantAnimation,QRect,QCoreApplication
from PySide6.QtGui import QMouseEvent,QFont
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QStackedLayout,QGraphicsOpacityEffect,QGraphicsBlurEffect,QFrame,QLabel
from Ui_cover import Ui_cover
from Ui_Agent_choose import Ui_Agent_choose
from Ui_choose_model_1_2 import Ui_MainWindow as Ui_choose_model_1
from Ui_strength_assignment_2 import Ui_strength_assignment
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
        
        
        # self.pushButton_option1.clicked.connect(self.be_shy)
        # self.label_content.setText("")
        # self.text="学长你好，我想竞选今年的学生会会长，您能够给我一点指导吗？"
        # self.current_index = 0
        # if self.text!="":
        #     self.start_flow_text()


    def be_shy(self):
        self.text="学长，你这样说人家害羞了"
        self.start_flow_text()
        # self.ui.label_2.setText("学长，你这样说人家害羞了")
        self.pushButton_option1.setText("")
        self.pushButton_option2.setText("")
        self.pushButton_option3.setText("")
        #渐出动画
        self.animation = QVariantAnimation()
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setDuration(1000)  # 动画持续时间
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)  # 设置缓动曲线
        
        def update_opacity(value):
            self.opacity_effect_6.setOpacity(value)
            self.opacity_effect_8.setOpacity(1-value)
            
        self.animation.valueChanged.connect(update_opacity)
         # 开始动画
        self.animation.start()


    def set_stream_text(self, text):
        self.current_index=0
        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(lambda:self.update_text_stream(text))
            self.timer.start(50)  # 每50毫秒更新一次
        else:
            self.timer.start()

    def update_text_stream(self,text:str):
        if self.current_index < len(text):
            self.label_content.setText(text[:self.current_index + 1])
            self.current_index += 1
        else:
            self.timer.stop()


    def start_flow_text(self):
        self.current_index=0
        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_text)
            self.timer.start(100)  # 每100毫秒更新一次
        else:
            self.timer.start()

    def update_text(self):
        if self.current_index < len(self.text):
            self.label_content.setText(self.text[:self.current_index + 1])
            self.current_index += 1
        else:
            self.timer.stop()

class GameLayout_diary(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_strength_assignment()
        self.ui.setupUi(self)
        self.ui.frame.setVisible(False)
        self.ui.pushButton_5.clicked.connect(self.phase2)
        #弹窗测试按钮
        self.ui.pushButton_6 = QPushButton(self)
        self.ui.pushButton_6.setObjectName(u"pushButton_6")
        self.ui.pushButton_6.setGeometry(QRect(380, 180, 75, 24))
        self.ui.pushButton_6.setText("来个事件")
        self.ui.pushButton_6.clicked.connect(self.chuxian)
        #每周任务执行过程的widget
        self.new_widget = QWidget(self)
        self.new_widget.setVisible(False)
        self.new_widget.setGeometry(0, 0, 1280, 720)
        self.new_widget.label_16 = QLabel(self.new_widget)
        self.new_widget.label_16.setObjectName(u"label_16")
        self.new_widget.label_16.setGeometry(QRect(270, 30, 621, 661))
        self.new_widget.label_16.setStyleSheet(u"border-image: url(:/image/resource/Strength_assign/paper2_yellow_l.png);")
        self.new_widget.write_content = QLabel(self.new_widget)
        self.new_widget.write_content.setObjectName(u"write_content")
        self.new_widget.write_content.setGeometry(QRect(290, 50, 581, 561))
        font11 = QFont()
        font11.setFamilies([u"\u5343\u56fe\u7b14\u950b\u624b\u5199\u4f53"])
        font11.setPointSize(18)
        font11.setBold(True)
        self.new_widget.write_content.setFont(font11)
        self.new_widget.write_content.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.new_widget.write_content.setText(QCoreApplication.translate("strength_assignment", u"\u661f\u671f\u4e00      5\u670828\u65e5     \u6674", None))
        self.new_widget.write_content.setWordWrap(True)
        self.new_widget.write_content.setText("你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好你好")
        #模糊状态恢复测试按钮
        self.new_widget.pushButton_7 = QPushButton(self.new_widget)
        self.new_widget.pushButton_7.setObjectName(u"pushButton_7")
        self.new_widget.pushButton_7.setGeometry(QRect(500, 180, 75, 24))
        self.new_widget.pushButton_7.setText("恢复")
        self.new_widget.pushButton_7.clicked.connect(self.recover)
        
        #每周执行任务的内容widget,模糊背景
        self.new_widget.next_button = QPushButton(self.new_widget)
        self.new_widget.next_button.setObjectName(u"next_button")
        self.new_widget.next_button.setGeometry(QRect(700, 620, 171, 41))
        font10 = QFont()
        font10.setPointSize(16)
        font10.setBold(True)
        self.new_widget.next_button.setFont(font10)
        self.new_widget.next_button.setStyleSheet("#next_button{color:brown;\n"
"background-color: rgb(255, 230, 0);}"
        "#next_button:hover{color:brown;\n"
"background-color: rgb(255, 200, 0);}"
        "#next_button:pressed{color:brown;\n"
"background-color: rgb(255, 170, 0);}"
)
        
        self.ui.true_button.setText("是")
        self.ui.true_button.clicked.connect(self.guanbi)
        self.ui.false_button.setText("否")
        self.ui.false_button.clicked.connect(self.guanbi)
        self.new_widget.next_button.setText("Next")
    #弹窗出现
    def chuxian(self):
        self.ui.frame.setVisible(True)
    def get_label_list(self):
        label_list=[self.ui.mission1_show,self.ui.mission2_show,self.ui.mission3_show,self.ui.mission4_show,self.ui.mission5_show]
        return label_list
    def get_plus_button_list(self):
        plus_button_list=[self.ui.plus1,self.ui.plus2,self.ui.plus3,self.ui.plus4,self.ui.plus5]
        return plus_button_list
    def get_minus_button_list(self):
        minus_button_list=[self.ui.minus1,self.ui.minus2,self.ui.minus3,self.ui.minus4,self.ui.minus5]
        return minus_button_list
    def get_mission_label(self):
        mission_label_list=[self.ui.misson_1,self.ui.mission_2,self.ui.mission_3,self.ui.mission_4,self.ui.mission_5,self.ui.mission_6,self.ui.mission_7,self.ui.mission_8,self.ui.mission_9,self.ui.mission_10]
        return mission_label_list
    #清空当前列表
    def delete_all(self):
        self.ui.misson_1.setText("")
        self.ui.mission_2.setText("")
        self.ui.mission_3.setText("")
        self.ui.mission_4.setText("")
        self.ui.mission_5.setText("")
        self.ui.mission_6.setText("")
        self.ui.mission_7.setText("")
        self.ui.mission_8.setText("")
        self.ui.mission_9.setText("")
        self.ui.mission_10.setText("")

    #弹窗关闭
    def guanbi(self):
        self.ui.frame.setVisible(False)
        
        
    # 点击pushButton_5进每周任务执行阶段
    def phase2(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(20)
        self.blur_effect.setBlurHints(QGraphicsBlurEffect.BlurHint.PerformanceHint)
        self.ui.centralwidget.setGraphicsEffect(self.blur_effect)
        self.new_widget.setVisible(True)
    #点击pushButton_7回到第一阶段，模糊消失
    def recover(self):
        self.ui.centralwidget.setGraphicsEffect(None)
        self.new_widget.setVisible(False)
#以下是GameLayout_diary类外函数
def plus(label:QLabel,label2:QLabel,num):
        global value_list
        if int(label2.text())<5:
            return
        words_list=label.text().split("  ")
        value_list[num]=int(words_list[1])+5
        label.setText(words_list[0]+"  "+str(value_list[num]))
        print(num)
        print(value_list[num])
        tmp=int(label2.text())
        tmp=tmp-5
        label2.setText(str(tmp))
def minus(label:QLabel,label2:QLabel,num):
        global value_list
        words_list=label.text().split("  ")
        if int(words_list[1])<5: 
            return
        value_list[num]=int(words_list[1])-5
        label.setText(words_list[0]+"  "+str(value_list[num]))
        print(value_list[num])
        tmp=int(label2.text())
        tmp=tmp+5
        label2.setText(str(tmp))       
#绑定按钮,因为绑定的信号是类外函数，在类内绑定的时候老是有参数报错，所以放在类外
def bind():
    window.game_layout_diary.ui.plus1.clicked.connect(lambda:plus(window.game_layout_diary.ui.mission1_show,window.game_layout_diary.ui.total_strength,0+count))
    window.game_layout_diary.ui.minus1.clicked.connect(lambda:minus(window.game_layout_diary.ui.mission1_show,window.game_layout_diary.ui.total_strength,0+count))
    window.game_layout_diary.ui.plus2.clicked.connect(lambda:plus(window.game_layout_diary.ui.mission2_show,window.game_layout_diary.ui.total_strength,1+count))
    window.game_layout_diary.ui.minus2.clicked.connect(lambda:minus(window.game_layout_diary.ui.mission2_show,window.game_layout_diary.ui.total_strength,1+count))
    window.game_layout_diary.ui.plus3.clicked.connect(lambda:plus(window.game_layout_diary.ui.mission3_show,window.game_layout_diary.ui.total_strength,2+count))
    window.game_layout_diary.ui.minus3.clicked.connect(lambda:minus(window.game_layout_diary.ui.mission3_show,window.game_layout_diary.ui.total_strength,2+count))
    window.game_layout_diary.ui.plus4.clicked.connect(lambda:plus(window.game_layout_diary.ui.mission4_show,window.game_layout_diary.ui.total_strength,3+count))
    window.game_layout_diary.ui.minus4.clicked.connect(lambda:minus(window.game_layout_diary.ui.mission4_show,window.game_layout_diary.ui.total_strength,3+count))
    window.game_layout_diary.ui.plus5.clicked.connect(lambda:plus(window.game_layout_diary.ui.mission5_show,window.game_layout_diary.ui.total_strength,4+count))
    window.game_layout_diary.ui.minus5.clicked.connect(lambda:minus(window.game_layout_diary.ui.mission5_show,window.game_layout_diary.ui.total_strength,4+count)) 
def xiaoyu5():
    global count
    count=0
    
def dayu5():
    global count
    count=5
    
def left_show():
    for i in range(5):
        label_list[i].setText(list1[i]+"  "+str(value_list[i]))
        label_list[i].setVisible(True)
        plus_button_list[i].setVisible(True)
        minus_button_list[i].setVisible(True)  
    xiaoyu5()
def right_show():
        
    for i in range(5):
        label_list[i].setVisible(False)
        plus_button_list[i].setVisible(False)
        minus_button_list[i].setVisible(False)
    for i in range(0,len-5):
        label_list[i].setText(list1[i+5]+"  "+str(value_list[i+5]))
        label_list[i].setVisible(True)
        plus_button_list[i].setVisible(True)
        minus_button_list[i].setVisible(True)
    dayu5()     

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
        self.game_layout_diary= GameLayout_diary()

        
        self.stacked_layout.addWidget(self.game_layout_main_menu) 
        self.stacked_layout.addWidget(self.game_layout_Agent)
        self.stacked_layout.addWidget(self.game_layout_choose_model_1)
        self.stacked_layout.addWidget(self.game_layout_diary)
        
        
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
        self.game_layout_diary.ui.exit_button.clicked.connect(self.back)
        # self.game_layout_diary.ui.pushButton_5.clicked.connect(self.next)
        # self.game_layout_Agent.pushButton.clicked.connect(self.agent_girlfriend)

    def Agent_choose(self):
        self.stacked_layout.setCurrentIndex(1)

    def choose_model_1(self):
        self.stacked_layout.setCurrentIndex(2)

    def game_start(self):
        self.stacked_layout.setCurrentIndex(3)
    #     from main import Game
    #     self.game = Game(self)
    #     self.game_layout_diary.ui.misson_1.setText(self.game.start()+"不管怎样，我决定从现在开始记日记，这应该是个好习惯吧。")

    # def next(self):
    #     self.game.next()


    def back(self):
        self.stacked_layout.setCurrentIndex(0)

    # def agent_girlfriend(self):
    #     from Event.crush_atFirstBlush import event_crush_atFirstBlush
    #     self.event_crush_atFirstBlush = event_crush_atFirstBlush(self.game)
    #     self.event_crush_atFirstBlush.event_start()
        
   
if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    # input_list=["睡觉","睡觉","睡觉"]
    input_list=["睡觉","睡觉","睡觉","唱歌","跳舞","rap","打篮球"]
    list1=input_list
    len=len(list1)
    
    for i in range(len):
        value_list.append(0)
    #清空最初的内容
    window.game_layout_diary.delete_all()
    window.game_layout_diary.ui.mission1_show.setText("")
    window.game_layout_diary.ui.mission2_show.setText("")
    window.game_layout_diary.ui.mission3_show.setText("")
    window.game_layout_diary.ui.mission4_show.setText("")
    window.game_layout_diary.ui.mission5_show.setText("")
    
    
    #list初始化
    mission_label_list=window.game_layout_diary.get_mission_label()
    label_list=window.game_layout_diary.get_label_list()
    plus_button_list=window.game_layout_diary.get_plus_button_list()
    minus_button_list=window.game_layout_diary.get_minus_button_list()

    for i in range(len):
        tmp=str(i+1)
        mission_label_list[i].setText(tmp+"、"+list1[i])

    for i in range(5):
        label_list[i].setVisible(False)
        plus_button_list[i].setVisible(False)
        minus_button_list[i].setVisible(False)
    bind()
    if len<=5:
        for i in range(len):
            label_list[i].setText(list1[i]+"  0")
            label_list[i].setVisible(True)
            plus_button_list[i].setVisible(True)
            minus_button_list[i].setVisible(True)
        
            
    else:
        for i in range(5):
            label_list[i].setText(list1[i]+"  0")
            
            label_list[i].setVisible(True)
            plus_button_list[i].setVisible(True)
            minus_button_list[i].setVisible(True)
        
        window.game_layout_diary.ui.left_button.clicked.connect(left_show)
        window.game_layout_diary.ui.right_button.clicked.connect(right_show)
    window.show()
    app.exec()