from. import event as Event
from main import Game
from typing import Tuple
from abc import ABC, abstractmethod
import asyncio
from PySide6.QtCore import QEventLoop
import threading




class event_club_recruit(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="club recruit", description="学生社团纳新，不用agent", Game=Game)
        self.probability=0
        self.layout=self.game.Ui.game_layout_choose_model_1
        self.club_choosed = None
       

    def if_join(self)-> Tuple[str, str]:
        return "听说学校社团有纳新活动","我要不要去看看呢？"


    def event_start(self, **kwargs):
        print("event_club_recruit start")
        
        
        self.step = 0
        self.game.Ui.stacked_layout.setCurrentIndex(2)

        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()
        self.layout.plainTextEdit_input.hide()

        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])
        self.set_art()

        pass


    def next(self,pos = None):

        self.step += 1
        if self.step >= len(self.dialogue_list):
            self.event_end()
            return
        elif self.step == 4:
            if pos == 1:
                pass
            elif pos == 2:
                self.step += 1 # 5
            elif pos == 3:
                self.step += 2 # 6
        elif self.step == 5: # 学术类社团做完选择
            if pos == 1:
                self.club_choosed = "数学探索社"
            elif pos == 2:
                self.club_choosed = "历史研习会"
            elif pos == 3:
                self.club_choosed = "经济学沙龙"
            self.step = 7
        elif self.step == 6: # 体育类社团做完选择
            if pos == 1:
                self.club_choosed = "篮球精英队"
            elif pos == 2:
                self.club_choosed = "足球联盟"
            elif pos == 3:
                self.club_choosed = "羽毛球飞扬社"
            self.step = 7
        elif self.step == 7: # 公益类社团做完选择
            if pos == 1:
                self.club_choosed = "志愿者行动团"
            elif pos == 2:
                self.club_choosed = "绿色地球环保社"
            elif pos == 3:
                self.club_choosed = "爱心传递协会"
        elif self.step == 8:
            if pos == 1:
                pass
            elif pos == 2:
                self.step += 2 # 10
            elif pos == 3:
                self.step += 4 # 12
        elif self.step == 10:
            self.step = 14
        elif self.step == 12:
            self.step = 14




        self.set_art()
        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        if self.step != 7:
            self.layout.set_stream_text(self.dialogue_list[self.step][1])
        else:
            self.layout.set_stream_text(self.dialogue_list[self.step][1].format(self.club_choosed))

        
        

    def set_art(self):
        def user_choice(*args):
            count = 0
            for arg in args:
                if isinstance(arg, str):
                    count += 1
                    if count == 1:
                        self.layout.pushButton_option1.show()
                        self.layout.pushButton_option1.setText(arg)
                    elif count == 2:
                        self.layout.pushButton_option2.show()
                        self.layout.pushButton_option2.setText(arg)
                    elif count == 3:
                        self.layout.pushButton_option3.show()
                        self.layout.pushButton_option3.setText(arg)
        

        # self.layout.pushButton_next.show()
        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()

        if self.step == 0:
            # self.layout.label_img_left.hide()
            pass
        elif self.step == 3:
            user_choice("学术类社团", "体育类社团", "公益类社团")
            self.layout.pushButton_next.hide()
        elif self.step == 4:
            user_choice("数学探索社", "历史研习会", "经济学沙龙")
        elif self.step == 5:
            user_choice("篮球精英队", "足球联盟", "羽毛球飞扬社")
        elif self.step == 6:
            user_choice("志愿者行动团", "绿色地球环保社", "爱心传递协会")
        elif self.step == 7:
            user_choice("我刚开始接触这方面，想多学习了解", "我已经接触一段时间了", "我只是想加入社团，了解一下")
            self.layout.pushButton_next.hide()
        elif self.step == 8:
            self.layout.pushButton_next.show()
        elif self.step == 10:
            self.layout.pushButton_next.show()
        elif self.step == 12:
            self.layout.pushButton_next.show()

        
    def event_end(self):
        self.refreshProbability()
        self.affection()

        self.game.Ui.stacked_layout.setCurrentIndex(3)
        self.game.progress["layout"]=3



    def refreshProbability(self):
        pass


    def affection(self,*args):
        pass

    
    club_list = [
        "数学探索社", "历史研习会", "经济学沙龙",
        "篮球精英队", "足球联盟", "羽毛球飞扬社",
        "志愿者行动团", "绿色地球环保社", "爱心传递协会"
    ]

    dialogue_list = [
        ["Narrator", "在一个洒满阳光的午后，校园广场汇聚了熙熙攘攘的学生群体，空气中洋溢着欢快与期待的气息。各个社团的展位上，色彩斑斓的海报如磁石般吸引着过往的同学驻足观看。此刻，学生会的社团负责人挺身而出，站在广场中央，满怀激情地向众人宣讲。"], # 0
        ["Narrator", "\"欢迎大家参加我们每年一度的社团纳新活动！这是一个了解各类社团、结交新朋友的好机会。无论你是想在学术上提升自己，还是想在文艺、体育、科技等领域发挥特长，今天都有许多优秀的社团在这里等着你们！快来看看，找到属于你的社团吧！\""],
        ["Narrator", "你在广场上四处浏览，看到各个社团的摊位，各具特色。你感到兴奋，这里有丰富的选择。"],
        ["Narrator", "你在思考要不要选择一个感兴趣的社团加入。"], # 3
        ["Narrator", "那具体选择哪个社团呢？"], # 4
        ["Narrator", "那具体选择哪个社团呢？"], # 5
        ["Narrator", "那具体选择哪个社团呢？"], # 6
        ["社团负责人", "\"太好了！欢迎加入我们{}！请问你是新手还是有一定经验呢？\""], # 7
        ["你", "\"我刚开始接触这方面，想多学习了解。\""], # 8
        ["社团负责人", "\"没问题，我们会提供基础培训，帮助你掌握基本知识。下周我们有一次活动，你一定要参加！\""], # 9
        ["你", "\"我已经接触一段时间了\""], # 10
        ["社团负责人", "\"“那太棒了！我们每个月都会举办一次交流会，期待你的参与！\""], # 11
        ["你", "\"我只是想加入社团，了解一下。\""], # 12
        ["社团负责人", "\"欢迎你！加入社团不仅能学习到东西，还能结识到很多志同道合的朋友！\""], # 13
        ["Narrator", "你与社团负责人进行了愉快的交流，感受到了社团的温暖与热情。这份体验无疑会让你的校园生活更加多彩多姿。"], # 14
        ["Narrator", "(End.)"],
    ]
    
