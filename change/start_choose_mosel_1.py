from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QGraphicsOpacityEffect
from Ui_choose_model_1_2 import Ui_MainWindow as UI_Start
from PySide6.QtCore import Qt, QTimer, QEasingCurve, QPropertyAnimation, QVariantAnimation

#此处的user_turn为True时，是用户的回合；user_turn为False时，是npc的回合
user_turn=False
class MyWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = UI_Start()
        
        self.ui.setupUi(self)
        
        #给这两个label设置透明度
        self.opacity_effect_6 = QGraphicsOpacityEffect()
        self.opacity_effect_8 = QGraphicsOpacityEffect()
        
        self.ui.label_6.setGraphicsEffect(self.opacity_effect_6)
        self.ui.label_8.setGraphicsEffect(self.opacity_effect_8)
        self.opacity_effect_8.setOpacity(0)
        self.opacity_effect_6.setOpacity(1)
        
        self.ui.next_button.clicked.connect(self.next)

        #刚开始时，选项和输入框不可见，这个根据剧情而定，可以改变
        self.ui.plainTextEdit.setVisible(False)
        self.ui.pushButton_2.setVisible(False)
        self.ui.pushButton_3.setVisible(False)
        self.ui.pushButton.setVisible(False)
        
        self.ui.pushButton.clicked.connect(self.result1)
        self.ui.label_2.setText("")
        self.text="学长你好，我想竞选今年的学生会会长，您能够给我一点指导吗？"
        self.current_index = 0
        if self.text!="":
            self.start_flow_text()
    def result1(self):
        self.ui.label_2.setVisible(True)
        self.ui.plainTextEdit.setVisible(False)
        self.ui.plainTextEdit.clear()
        self.ui.pushButton_2.setVisible(False)
        self.ui.pushButton_3.setVisible(False)
        self.ui.pushButton.setVisible(False)
        self.be_shy()
    def be_shy(self):
        self.text="学长，你这样说人家害羞了"
        self.start_flow_text()
        # self.ui.label_2.setText("学长，你这样说人家害羞了")
        self.ui.pushButton.setText("")
        self.ui.pushButton_2.setText("")
        self.ui.pushButton_3.setText("")
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
    def next(self):
        global user_turn
        if user_turn:
            user_turn=False
        else:
            user_turn=True
        #如果user_turn为True，则显示输入框和上方按钮
        if user_turn:
            self.ui.label_2.setVisible(False)
            self.ui.label_2.setText("")
            
            self.ui.plainTextEdit.setVisible(True)
            self.ui.pushButton_2.setVisible(True)
            self.ui.pushButton_3.setVisible(True)
            self.ui.pushButton.setVisible(True)
        else:
            
            self.ui.plainTextEdit.setVisible(False)
            self.ui.plainTextEdit.clear()
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_3.setVisible(False)
            self.ui.pushButton.setVisible(False)
            #下面就是调用大模型回答的函数
            #self.text=模型的返回文字
            #self.start_flow_text()流式输出文字
           
    
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
            self.ui.label_2.setText(self.text[:self.current_index + 1])
            self.current_index += 1
        else:
            self.timer.stop()

        
if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow1()
    window.show()
    app.exec()