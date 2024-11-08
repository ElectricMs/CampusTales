from PySide6.QtCore import Qt,QEvent,QTimer, QEasingCurve, QPropertyAnimation, QVariantAnimation,QRect,QCoreApplication,QUrl
from PySide6.QtGui import QMouseEvent,QFont
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QStackedLayout, QGraphicsOpacityEffect, QGraphicsBlurEffect, QFrame,QLabel, QVBoxLayout
# from UI_resource.Ui_cover import Ui_cover
from UI_resource.Ui_Agent_choose import Ui_Agent_choose
from UI_resource.Ui_choose_model_1 import Ui_MainWindow as Ui_choose_model_1
from UI_resource.Ui_allocateEnergy import Ui_allocateEnergy
from Animation.yinru_start import MyWindow as GameLayout_initialAnimation
from UI_resource.new_cover import MyWindow as GameLayout_MainMenu
from Animation.write_widget import TypewriterEffectWidget as new_widget
from setting_start import MyWindow as GameLayout_setting
from end_start import MyWindow as GameLayout_end
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
# Agent对话事件界面


class GameLayout_choose_model_1(QMainWindow, Ui_choose_model_1):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #目前的三张人物图片，都存放在resource1_rc中
        self.img_path_list=["url(:/people/resource/girl_smile-removebg-preview.png)","url(:/people/resource/girl_shy-removebg-preview (2).png)","url(:/people/resource/boy_normal_-removebg-preview.png)"]
        self.change_background_img_left(self.img_path_list[1])
        
        self.islock = True
        #初始好感度为0
        self.progressBar_second.setVisible(False)
        self.progressBar.setVisible(False)
        
        #给这两个label设置透明度
        self.opacity_effect_6 = QGraphicsOpacityEffect()
        self.opacity_effect_8 = QGraphicsOpacityEffect()
        
        self.label_img_left.setGraphicsEffect(self.opacity_effect_6)
        self.label_8.setGraphicsEffect(self.opacity_effect_8)
        self.opacity_effect_8.setOpacity(0)
        self.opacity_effect_6.setOpacity(1)
        
        
#此处参考zly上周五的人物解锁思想，如果好感度小于60，则未解锁人物，此时展示好感度条progressBar(这个条比较短，最大范围100）；
#如果好感度大于等于60，则解锁人物，此时展示好感度条progressBar_second(这个条更长，最大范围600）。
    def favorite_level_change(self,favorite_level):
        num=int(favorite_level)
        if favorite_level>=60:
            self.islock=False
            self.progressBar_second.setValue(num)
            self.progressBar_second.setVisible(True)
            self.progressBar.setVisible(False)
        else:
            self.islock=True
            self.progressBar.setValue(num)
            self.progressBar_second.setVisible(False)
            self.progressBar.setVisible(True)
        
    #更换self.label_img_left背景图片的函数
    def change_background_img_left(self,img_path):
        self.label_img_left.setStyleSheet(f'border-image: {img_path};')
    
        
    def set_stream_text(self, text):
        from setting_start import InteractionTimerInterval
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        current_index = 0

        def update_text_stream():
            nonlocal current_index
            if current_index < len(text):
                self.label_content.setText(text[:current_index + 1])
                current_index += 1
            else:
                self.timer.stop()

        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(update_text_stream)
            self.timer.setInterval(InteractionTimerInterval)
            self.timer.start()  # 每50毫秒更新一次
        else:
            self.timer.stop()
            self.timer = QTimer(self)
            self.timer.timeout.connect(update_text_stream)
            self.timer.setInterval(InteractionTimerInterval)
            self.timer.start()

    
  
class GameLayout_allocateEnergy(QMainWindow, Ui_allocateEnergy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.frame_modal.setVisible(False)
        self.add_diary_widget()
        self.label_5.setText("你还没有给自己取名字哦~")
        self.label_5.setWordWrap(True)
        self.frame_selectArea.setGeometry(QRect(0,120,500,500))
        #目前的三张人物图片，都存放在resource1_rc中
        self.img_path_list=["url(:/people/resource/boy_normal_-removebg-preview.png)","url(:/people/resource/girl_shy-removebg-preview (2).png)","url(:/people/resource/girl_smile-removebg-preview.png)"]
        ###此处是用来更换主人公头像的,性别选女用女生图，性别男用男生图
        self.change_graphicsView(self.img_path_list[1])

    
    def change_name(self,new_name):
        self.label_5.setText(new_name)

    def change_graphicsView(self,img_path):
        self.graphicsView.setStyleSheet(f'border-image: {img_path};'"background-color:grey;")
    def add_diary_widget(self):
        #每周展示diary的widget，包含许多组件
        self.widget_diary = new_widget(self)


        self.widget_diary.setVisible(False)
        self.widget_diary.setGeometry(0, 0, 1280, 720)
       #每周执行任务的内容widget,模糊背景
        self.pushButton_diary_next = QPushButton(self.widget_diary)
        self.pushButton_diary_next.setObjectName(u"pushButton_diary_next")
        self.pushButton_diary_next.setGeometry(QRect(700, 620, 171, 41))
        self.pushButton_diary_next.setText("Next")
        font10 = QFont()
        font10.setPointSize(16)
        font10.setBold(True)
        self.pushButton_diary_next.setFont(font10)
        self.pushButton_diary_next.setStyleSheet("#pushButton_diary_next{color:brown;\n"
            "background-color: rgb(255, 230, 0);}"
                    "#pushButton_diary_next:hover{color:brown;\n"
            "background-color: rgb(255, 200, 0);}"
                    "#pushButton_diary_next:pressed{color:brown;\n"
            "background-color: rgb(255, 170, 0);}"
        )

    
        
    # 点击nextWeek后，模糊背景，显示diary页面
    def blur(self):
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(20)
        self.blur_effect.setBlurHints(QGraphicsBlurEffect.BlurHint.PerformanceHint)
        self.centralwidget.setGraphicsEffect(self.blur_effect)
        self.widget_diary.setVisible(True) # diary widget显示
        #在此处向label_diary_content传入文字，并start_animate()
        
        # self.widget_diary.label_diary_content.setTextToDraw(text)
        self.widget_diary.label_diary_content.start_animate()

    # 展示完最后一张日记后diary页面消失，显示能量分配界面
    def blur_recover(self):
        self.centralwidget.setGraphicsEffect(None)  # type: ignore
        self.widget_diary.setVisible(False)







class GameLayout_Agent(QMainWindow, Ui_Agent_choose):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
     






class MyWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        
        self.resize(1280,720)
        self.player = QMediaPlayer()
        # 创建音频输出对象
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(0.6)
        # 将媒体播放器与音频输出连接起来
        self.player.setAudioOutput(self.audio_output)
         # 设置要播放的音频文件路径
        audio_file_path = 'Game/Animation/水月陵 - Raised bed.flac'
        self.player.setSource(QUrl.fromLocalFile(audio_file_path))

        # 设置循环播放
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        self.player.play()
        self.stacked_layout = QStackedLayout()
        self.game_layout_main_menu = GameLayout_MainMenu()
        self.game_layout_Agent= GameLayout_Agent()
        self.game_layout_choose_model_1= GameLayout_choose_model_1()
        self.game_layout_allocateEnergy= GameLayout_allocateEnergy()
        self.game_layout_end= GameLayout_end()

        self.game_layout_setting=GameLayout_setting()
        self.game_layout_setting.set_mainWindow_instance(self)
        self.game_layout_setting.set_allocateEnergy_instance(self.game_layout_allocateEnergy)


        self.game_layout_initialAnimation = GameLayout_initialAnimation(callback = lambda: self.stacked_layout.setCurrentIndex(3))
        self.game_layout_initialAnimation.set_mainwindow_instance(self)
        

        self.stacked_layout.addWidget(self.game_layout_main_menu) # 0
        self.stacked_layout.addWidget(self.game_layout_Agent) # 1
        self.stacked_layout.addWidget(self.game_layout_choose_model_1) # 2
        self.stacked_layout.addWidget(self.game_layout_allocateEnergy) # 3
        self.stacked_layout.addWidget(self.game_layout_initialAnimation) # 4
        self.stacked_layout.addWidget(self.game_layout_setting)#5
        self.stacked_layout.addWidget(self.game_layout_end) # 6

        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

        self.first_start_game=True
        self.game: Game
        
        self.bind()
        # 设置当前显示的布局为主菜单
        self.current_layout_index = 0
        self.stacked_layout.setCurrentIndex(self.current_layout_index)
    
    def keyPressEvent(self, event):
        # 将键盘事件传递给子窗口
        self.game_layout_initialAnimation.keyPressEvent(event)

    def bind(self):
        self.game_layout_main_menu.pushButton.clicked.connect(self.game_start)
        self.game_layout_main_menu.pushButton_3.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(5))
        self.game_layout_main_menu.pushButton_4.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(1))
        self.game_layout_main_menu.pushButton_5.clicked.connect(self.close)
       


        self.game_layout_Agent.exit_button.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        self.game_layout_setting.ui.exit_button.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        self.game_layout_allocateEnergy.pushButton_exit.clicked.connect(lambda: self.stacked_layout.setCurrentIndex(0))
        self.game_layout_allocateEnergy.pushButton_next.clicked.connect(self.nextWeek)
        self.game_layout_Agent.pushButton.clicked.connect(self.agent_girlfriend)
        self.game_layout_allocateEnergy.pushButton_yes.clicked.connect(lambda: self.game.event_true())
        self.game_layout_allocateEnergy.pushButton_no.clicked.connect(lambda: self.game.event_false())
        self.game_layout_choose_model_1.pushButton_next.clicked.connect(lambda: self.agent_next(pos = 0))
        self.game_layout_choose_model_1.pushButton_option1.clicked.connect(lambda: self.agent_next(pos = 1))
        self.game_layout_choose_model_1.pushButton_option2.clicked.connect(lambda: self.agent_next(pos = 2))
        self.game_layout_choose_model_1.pushButton_option3.clicked.connect(lambda: self.agent_next(pos = 3))

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
        #这里没太看明白
        self.game_layout_allocateEnergy.pushButton_diary_next.clicked.connect(lambda: self.game.next())


    def game_start(self):
        if self.first_start_game:
            self.game.start()
            self.game_layout_main_menu.pushButton.setText("                       继续游戏          CONTINUE")
            self.first_start_game=False
        else:
            self.game.reload()


    def agent_next(self, pos=None):
        self.game.currentEvent.next(pos=pos)


    def nextWeek(self):
        print("next week")
        self.game.nextWeek()


    def agent_girlfriend(self):
        from Event.crush_atFirstBlush import CrushAtFirstBlushEvent
        # 这里的处理不太好，只是为了调试方便
        # from main import Game
        # if hasattr(self, 'game'):
        #     if isinstance(self.game, Game):
        #         self.event_crush_atFirstBlush = event_crush_atFirstBlush(self.game)
        # else:
        #     self.game = Game(self)
        #     self.event_crush_atFirstBlush = event_crush_atFirstBlush(Game(self), agent_mode=True)
        #     self.game.currentEvent = self.event_crush_atFirstBlush
        # self.event_crush_atFirstBlush.event_start()
        
        if 'crush_atFirstBlush' in self.game.allEvents:
            CrushAtFirstBlushEvent=self.game.allEvents['crush_atFirstBlush']
            CrushAtFirstBlushEvent.event_start(agent_mode=True)
        else:
            print("event_crush_atFirstBlush not found")
    def change_sound(self,value):
        self.audio_output.setVolume(value/100.0)
        self.game_layout_initialAnimation.sound_effect.setVolume(value/100.0)
        self.game_layout_allocateEnergy.widget_diary.label_diary_content.audio_output.setVolume(value/100.0)  
    def change_name(self,new_name):
        self.game_layout_allocateEnergy.label_5.setText(new_name)
        self.game_layout_setting.name_lineEdit.setText(new_name)

if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    from main import Game
    if hasattr(window, 'game'):
        if isinstance(window.game, Game):
            pass
        else:
            window.game = Game(window)
            print(window.game)      
    else:
        window.game = Game(window)     
        print(window.game)
    window.show()
    app.exec()