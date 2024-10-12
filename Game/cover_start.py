from PySide6.QtCore import Qt,QEvent,QTimer, QEasingCurve, QPropertyAnimation, QVariantAnimation
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QStackedLayout,QGraphicsOpacityEffect
from UI_resource.Ui_cover import Ui_cover
from UI_resource.Ui_Agent_choose import Ui_Agent_choose
from UI_resource.Ui_choose_model_1 import Ui_MainWindow as Ui_choose_model_1
from UI_resource.Ui_strength_assignment import Ui_strength_assignment


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

class GameLayout_diary(QMainWindow, Ui_strength_assignment):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
        self.game_layout_diary.exit_button.clicked.connect(self.back)
        self.game_layout_diary.pushButton_5.clicked.connect(self.next)
        self.game_layout_Agent.pushButton.clicked.connect(self.agent_girlfriend)

    def Agent_choose(self):
        self.stacked_layout.setCurrentIndex(1)

    def choose_model_1(self):
        self.stacked_layout.setCurrentIndex(2)

    def game_start(self):
        self.stacked_layout.setCurrentIndex(3)
        from main import Game
        self.game = Game(self)
        self.game_layout_diary.misson_1.setText(self.game.start()+"不管怎样，我决定从现在开始记日记，这应该是个好习惯吧。")

    def next(self):
        self.game.next()


    def back(self):
        self.stacked_layout.setCurrentIndex(0)

    def agent_girlfriend(self):
        from Event.crush_atFirstBlush import event_crush_atFirstBlush
        self.event_crush_atFirstBlush = event_crush_atFirstBlush(self.game)
        self.event_crush_atFirstBlush.event_start()
        
   
if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()