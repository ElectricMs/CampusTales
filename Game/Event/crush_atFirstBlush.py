from. import event as Event
from main import Game
from typing import Tuple

class event_crush_atFirstBlush(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="crush at first blush", description="在迎新晚会上遇到的crush", Game=Game)
        self.probability=0
        self.layout=self.game.Ui.game_layout_choose_model_1


    def if_join(self)-> Tuple[str, str]:
        return "学院将举办一场迎新晚会","是否要参加呢？"


    def event_start(self):
        print("event_crush_atFirstBlush start")
        self.game.Ui.stacked_layout.setCurrentIndex(2)
        self.step = 0
        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()

        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])
        self.set_art()

        pass



    def next(self):
        self.step += 1
        if self.step >= len(self.dialogue_list):
            self.event_end()
            return
        
        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])
        

        self.set_art()

        pass


    def set_art(self):
            if self.step == 0:
                self.layout.label_8.hide()
                self.layout.label_6.hide()
            elif self.step == 4:
                self.layout.label_8.show()
                self.layout.label_6.show()


    def event_end(self):
        # 记得激活按钮
        self.refreshProbability()
        self.affection()
        pass


    def refreshProbability(self):
        pass


    def affection(self,*args):
        pass


    dialogue_list = [
        ("Narrator", "\"各位大一新生还有学长学姐们，欢迎来到迎新晚会！\""),
        ("Narrator", "舞台上灯光璀璨，音乐欢快。学生会成员正在表演节目，观众席上坐满了新生和老生。你有些紧张而又有点期待地看着四周。"),
        ("你", "\"好多人啊，我有点紧张……不过，听说今晚会有机会认识很多新朋友，我还是鼓起勇气来参加了。\""),
        ("Narrator", "\"\""),
        ("你", "你四处张望，突然他的目光被一个人吸引住了——一位站在不远处，穿着一件简单的白色连衣裙，笑容甜美的女生。"), # 4
        ("你", "\"她好漂亮，感觉很亲切……我从来没有这么心动过。我要不要过去打个招呼？\""),
        ("你", "你深呼吸几下，鼓起勇气向林晓走去。"),
        ("你", "\"\""),
    ]
    