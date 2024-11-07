from. import event as Event
from main import Game
from typing import Tuple
from abc import ABC, abstractmethod
from Agent.agent import Agent
from Agent.agent2 import Agent as Agent2
import asyncio
from PySide6.QtCore import QEventLoop
import threading



class InternshipEvent(Event.Event):
    def __init__(self, Game:Game):
        super().__init__(name="internship", description="获得实习机会", Game=Game)
        self.probability=0
        self.layout=self.game.Ui.game_layout_choose_model_1
        context1 = """

        """
        
        self.agent = Agent(name="interviewer", personality_traits="友好专业", context=context1)
        #self.agent = Agent2(name=self.name, context=context1)
        self.loop = asyncio.new_event_loop() # 创建一个新的事件循环 用于跑agent
        threading.Thread(target=self.loop.run_forever, daemon=True).start() # 在一个单独的线程中启动事件循环，确保它一直在运行
        self.talk_remaining = 5
        self.emotion_level = 0
        self.first_start = True
        
        
    def if_join(self)-> Tuple[str, str]:
        return "学院将举办一场双选会，据说有实习面试机会","是否要参加呢？"


    def event_start(self, **kwargs):
        print("event_internship start")
        
        
        
        self.step = 0
        for key, value in kwargs.items():
            if key == "agent_mode" and value==True:
                self.agent_mode = True
                self.step = 5
        self.game.Ui.stacked_layout.setCurrentIndex(2)

        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()
        self.layout.plainTextEdit_input.hide()

        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])
        print(self.agent)
        self.set_art()

        pass


    def next(self,pos = None):

        self.step += 1
        if self.step >= len(self.dialogue_list):
            self.event_end()
            return

        self.set_art()
        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])

        
        if self.input_mode:
           
            # 用户自选回答阶段，step不自增，结束用户回答阶段时再自增
            input_text: str
            assert pos in [0, 1, 2, 3], "pos should be 0, 1, 2, 3"
            if pos == 0:
                if self.layout.plainTextEdit_input.toPlainText().strip() == None or self.layout.plainTextEdit_input.toPlainText().strip() == "":
                    self.step -= 1
                    return # 输入内容为空时点击next不做任何操作
                input_text = self.layout.plainTextEdit_input.toPlainText()
            elif pos == 1:
                input_text = self.layout.pushButton_option1.text()
            elif pos == 2:
                input_text = self.layout.pushButton_option2.text()
            elif pos == 3:
                input_text = self.layout.pushButton_option3.text()
            self.talk_remaining -= 1

            # 将内容发送给agent
            self.layout.pushButton_next.hide()
            # await
            # 当收到回答后next显示，代表回答已经通过agent生成，准备完毕
            async def get_response():
                response = await self.agent.user_interact_with_agent(input_text)
                response_text = response["response"]
                self.dialogue_list[self.step+1][1] = response_text
                # 一开始好感度应该为0
                # 要把每次对话返回的好感度，传入这个函数
                self.layout.favorite_level_change(response["emotion_level"])
                self.emotion_level = response["emotion_level"]
                self.layout.pushButton_next.show()
            asyncio.run_coroutine_threadsafe(get_response(), self.loop)
            
            def user_input_end():
                self.layout.pushButton_option1.hide()
                self.layout.pushButton_option2.hide()
                self.layout.pushButton_option3.hide()
                self.layout.pushButton_option1.setText("")
                self.layout.pushButton_option2.setText("")
                self.layout.pushButton_option3.setText("")
                self.layout.plainTextEdit_input.hide()
                self.layout.plainTextEdit_input.clear()
                

            # 将用户回答流式打印
            user_input_end()
            self.layout.set_stream_text(input_text)
            self.input_mode = False
            return


    def set_art(self):
        def user_input(*args):
            
            self.layout.plainTextEdit_input.show()
            self.layout.label_content.clear()
            self.layout.plainTextEdit_input.setPlaceholderText(f"在上方选择你喜欢的选项（如果有的话），或在此输入你想说的吧！\n你还有{self.talk_remaining}次对话机会！")
            
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
        
        if self.step == 0:
            self.layout.label_img_left.hide()
        elif self.step == 3:
            self.layout.label_img_left.show()
        elif self.step == 6:
            self.input_mode = True
            user_input("你好！", "我喜欢你！")
        elif self.step == 8:
            self.input_mode = True
            user_input("你真漂亮", "我好喜欢你呀！", "你愿意和我出去吃饭吗？")
        elif self.step == 10:
            self.input_mode = True
            user_input()
        elif self.step == 12:
            self.input_mode = True
            user_input()
        elif self.step == 14:
            self.input_mode = True
            user_input()

        
    def event_end(self):
        self.refreshProbability()
        if self.first_start:
            if self.emotion_level < 60:
                pass
            else:
                self.game.mainlineEvents.append(["陪Crush", 0])
                self.game.refreshMissionList()
        if self.agent_mode:
            self.game.Ui.stacked_layout.setCurrentIndex(1)
        else:
            self.game.Ui.stacked_layout.setCurrentIndex(3)
            self.game.progress["layout"]=3
        self.agent_mode = False


    def refreshProbability(self):
        pass


    def affection(self,*args):
        if self.emotion_level < 60:
            return "上周去参加了一个迎新晚会，我遇到了一个很漂亮的女生，但我们聊的并不算是顺利，不知道还有没有机会再见面了。"
        else:
            return "上周去参加了一个迎新晚会，我遇到了一个很漂亮的女生，我们聊的很愉快，我也很开心。我们互换了联系方式，我已经准备邀请她出去吃饭了。"


    dialogue_list = [
        ["Narrator", "\"各位大一新生还有学长学姐们，欢迎来到迎新晚会！\""], # 0
        ["Narrator", "舞台上灯光璀璨，音乐欢快。学生会成员正在表演节目，观众席上坐满了新生和老生。你有些紧张而又有点期待地看着四周。"],
        ["你", "\"好多人啊，我有点紧张……不过，听说今晚会有机会认识很多新朋友，我还是鼓起勇气来参加了。\""],
        ["Narrator", "你四处张望，突然他的目光被一个人吸引住了——一位站在不远处，穿着一件简单的白色连衣裙，笑容甜美的女生。"],
        ["你", "\"她好漂亮，感觉很亲切……我从来没有这么心动过。我要不要过去打个招呼？\""],
        ["Narrator", "你深呼吸几下，鼓起勇气向她走去。"], # 5
        ["你", ""],  # 6 这里要输入你自己的对话，发送给Agent
        ["Crush", ""],
        ["你", ""], # 8
        ["Crush", ""],
        ["你", ""], # 10
        ["Crush", ""],
        ["你", ""], # 12
        ["Crush", ""],
        ["你", ""], # 14
        ["Crush", ""],
        ["Narrator", "(End.)"],
    ]
    