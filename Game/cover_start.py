from PySide6.QtCore import Qt,QEvent,QTimer, QEasingCurve, QPropertyAnimation, QVariantAnimation
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QStackedLayout,QGraphicsOpacityEffect
from UI_resource.Ui_cover import Ui_cover
from UI_resource.Ui_Agent_choose import Ui_Agent_choose
from UI_resource.Ui_choose_model_1 import Ui_choose_model_1
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
        
        
        self.pushButton.clicked.connect(self.be_shy)
        self.label_2.setText("")
        self.text="学长你好，我想竞选今年的学生会会长，您能够给我一点指导吗？"
        self.current_index = 0
        if self.text!="":
            self.start_flow_text()
    def be_shy(self):
        self.text="学长，你这样说人家害羞了"
        self.start_flow_text()
        # self.ui.label_2.setText("学长，你这样说人家害羞了")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
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
            self.label_2.setText(self.text[:self.current_index + 1])
            self.current_index += 1
        else:
            self.timer.stop()

class GameLayout_strength_assign(QMainWindow, Ui_strength_assignment):
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
        self.game_layout_strength_assign= GameLayout_strength_assign()

        
        self.stacked_layout.addWidget(self.game_layout_main_menu) 
        self.stacked_layout.addWidget(self.game_layout_Agent)
        self.stacked_layout.addWidget(self.game_layout_choose_model_1)
        self.stacked_layout.addWidget(self.game_layout_strength_assign)
        
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)
        
        self.bind()
        # 设置当前显示的布局为主菜单
        self.current_layout_index = 0
        self.stacked_layout.setCurrentIndex(self.current_layout_index)
    def bind(self):
        self.game_layout_main_menu.pushButton.clicked.connect(self.choose_model_1)
        self.game_layout_main_menu.pushButton_2.clicked.connect(self.strength_assign)
        #self.game_layout_main_menu.pushButton_3.click.connect()
        self.game_layout_main_menu.pushButton_4.clicked.connect(self.Agent_choose)
        self.game_layout_main_menu.pushButton_5.clicked.connect(self.close)
    def Agent_choose(self):
        
        self.stacked_layout.setCurrentIndex(1)
    def choose_model_1(self):
        self.stacked_layout.setCurrentIndex(2)
    def strength_assign(self):
        self.stacked_layout.setCurrentIndex(3)
        
   
if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()