from. import event as Event
from main import Game
from typing import Tuple

class event_studentsUnion(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="the name of the event", description="the description of the event", Game=Game)
        self.probability=0


    def if_join(self)-> Tuple[str, str]:
        return "",""


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