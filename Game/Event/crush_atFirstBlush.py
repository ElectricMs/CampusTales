from. import event as Event
from main import Game
from typing import Tuple

class event_crush_atFirstBlush(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="crush at first blush", description="在迎新晚会上遇到的crush", Game=Game)
        self.probability=0
        self.layout=self.game.Ui.game_layout_choose_model_1


    def if_join(self)-> Tuple[str, str]:
        return "",""


    def event_start(self):
        self.game.Ui.stacked_layout.setCurrentIndex(2)
        self.step = 0
        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()

        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])
        

        pass



    def next(self):
        self.step += 1
        if self.step >= len(self.dialogue_list):
            self.event_end()
            return
        
        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])


        pass


    def event_end(self):

        self.refreshProbability()
        self.affection()
        pass


    def refreshProbability(self):
        pass


    def affection(self,*args):
        pass


    dialogue_list = [
        ("Narrator", "你好，我是Narrator，欢迎来到迎新晚会。"),
        ("Narrator", "今天的活动是《crush at first blush》，你是否愿意参加？"),
        ("Player", "当然愿意！"),
    ]
    