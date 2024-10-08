from. import event as Event
from main import Game
from typing import Tuple

class event_welcomeParty(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="迎新晚会", description="入学时触发", Game=Game)
        self.probability=0


    def if_join(self) -> Tuple[str, str]:
        talk1 = "我刚刚在学院的推送上看到了迎新晚会的消息，看上去很有意思，或许这是一个很好的机会？"
        talk2 = "要参加迎新晚会吗？"
        return talk1, talk2


    def event_start(self):

        self.event_end()
        pass


    def event_end(self):

        self.refreshProbability()
        self.affection()
        pass


    def refreshProbability(self):
        pass


    def affection(self,*args):
        pass