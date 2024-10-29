import random
import time
from abc import ABC, abstractmethod
from typing import Tuple
from main import Game



class event(ABC):
    def __init__(self, name:str, description:str, Game:Game, time=time.time()):
        self.name=name
        self.time=time
        self.description=description 
        self.game=Game
        self.input_mode=False
        self.agent_mode=False

        # self.ui=None
        # self.setting=None
        self.probability=1

    # 获取所有子类
    @classmethod
    def get_all_subEvents(cls, Game):

        # from .studentsUnion import event_studentsUnion
        from .crush_atFirstBlush import event_crush_atFirstBlush
        from .lecture_ACM import event_lecture_ACM
        subEvents={}

        subEvents.update({'crush_atFirstBlush':event_crush_atFirstBlush(Game)})
        subEvents.update({'lecture_ACM':event_lecture_ACM(Game)})
        
        return subEvents
    

    # 需要返回一段描述性文字 在下方让用户选择是否参加
    @abstractmethod
    def if_join(self)-> Tuple[str, str]:
        pass
    

    # 事件开始
    @abstractmethod
    def event_start(self):
        # 事件开始 当用户选择参加时触发
        # 接下来可以通过Game控制ui
        # 相当于从现在开始event类接过游戏控制权 结束时再归还给Game类

        pass


    # 点击next按钮触发
    @abstractmethod
    def next(self, pos = None):
        pass


    # 管理美术资源和效果 在event_start和next中调用
    @abstractmethod
    def set_art(self):
        pass


    # 事件结束
    @abstractmethod
    def event_end(self):
        pass


    # 刷新概率，在事件结束时调用
    @abstractmethod
    def refreshProbability(self):
        pass

    
    # 事件影响
    @abstractmethod
    def affection(self,*args):               
        pass

    


# @deprecated
class event_test(event):
    def __init__(self, Game:Game):
        super().__init__(name="测试事件", description="This is a test event", Game=Game)

        self.ui=None
        self.setting=None
        self.probability=1


    # 首先需要返回一段描述性文字 在下方让用户选择是否参加
    def if_join(self) -> Tuple[str, str]:
        random_talk=[
            "天哪，我不敢想象一个程序没有测试样例会怎么样，这可是个大麻烦啊！不过我到底是否要体验一下这个测试事件？这可是个好问题。",
            "这是什么，测试事件，这可是个好机会，我一定要参加！不对，我真的要参加吗？",
            "哇，一个野生的测试事件！这可是一个好机会，让我仔细想想，我要不要参加？"
        ]
        return str(random.choice(random_talk).lstrip()),"要参与测试事件吗？"


    def event_start(self):
        # 事件开始 当用户选择参加时触发
        # 接下来可以通过Game控制ui
        # 相当于从现在开始event类接过游戏控制权 结束时再归还给Game类
        # self.game.Ui.game_layout_allocateEnergy.misson_1.setText("我选择了测试事件，让我看看究竟是怎么回事。好吧，好像也不会发生什么，你知道的，这毕竟只是一个测试事件。当然，这个测试事件也可以控制ui")

        # 还没想好在哪调用 是在这直接调用还是在game类中
        self.event_end()
        pass 

    def event_end(self):

        self.refreshProbability()
        self.affection()
        pass


    # 刷新概率，在事件结束时调用
    def refreshProbability(self):
        pass

    
    # 事件影响
    def affection(self,*args):               
        pass

