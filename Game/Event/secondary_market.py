from. import event as Event
from main import Game
from typing import Tuple
from abc import ABC, abstractmethod
import asyncio
from PySide6.QtCore import QEventLoop
import threading




class SecondaryMarketEvent(Event.Event):
    def __init__(self, Game:Game):
        super().__init__(name="secondary market", description="二手市场", Game=Game)
        self.probability=0
        self.layout=self.game.Ui.game_layout_choose_model_1
       

    def if_join(self)-> Tuple[str, str]:
        return "听说学校组织了二手市场活动","我要不要去看看呢？"


    def event_start(self, **kwargs):
        print("SecondaryMarketEvent start")
        
        
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
        if self.step >= len(self.dialogue_list) or self.step == 18:
            self.event_end()
            return
        elif self.step == 5:
            if pos == 1:
                pass
            elif pos == 2:
                self.step = 18
        elif self.step == 9:
            if pos == 1:
                pass
            elif pos == 2:
                self.step = 11
            elif pos == 3:
                self.step = 13
        
        elif self.step == 11:
            self.step = 15
        elif self.step == 13:
            self.step = 15




        self.set_art()
        self.layout.label_name.setText(self.dialogue_list[self.step][0])
        self.layout.set_stream_text(self.dialogue_list[self.step][1])


        
        

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
        

        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()
        self.layout.pushButton_next.show()

        if self.step == 0:
            pass
        elif self.step == 4:
            user_choice("与学长交流，探索书籍的奥秘", "暂时不逛，未来再来探访")
            self.layout.pushButton_next.hide()
        elif self.step == 8:
            user_choice("询问经验", "探讨书籍价值", "分享个人经历")
            self.layout.pushButton_next.hide()
        

        
    def event_end(self):
        self.refreshProbability()
        self.affection()

        self.game.Ui.stacked_layout.setCurrentIndex(3)
        self.game.progress["layout"]=3



    def refreshProbability(self):
        pass


    def affection(self,*args):
        pass

    

    dialogue_list = [
        ["Narrator", "在一个阳光明媚的午后，微风轻拂，为即将开始的二手市场探秘之旅增添了几分惬意与期待。"], # 0
        ["Narrator", "在校园的一角，一个由各式摊位组成的二手市场热闹非凡，每个摊位上都摆满了琳琅满目的商品，从旧书到古董，从手工艺品到复古服饰，应有尽有。"],
        ["Narrator", "你漫步在二手市场的各个摊位间，目光在各式各样的商品间流转，心中充满了对未知的好奇与探索的欲望。"],
        ["Narrator", "你注意到学长的二手书摊位上摆满了各式各样的书籍，从经典文学到专业教材，从科幻小说到历史传记，每一本书都散发着独特的魅力。"],
        ["Narrator", "你思考着要不要在这个摊位前多停留一会儿。"], # 4

        ["Narrator", "你决定在学长的二手书摊位前停下脚步，与他进行一番深入的交流。学长热情地接待了你，并向你介绍了他的藏书和二手市场的趣事。"],  # 5
        ["你", "“学长，你这里的书真多啊！每本书都看起来很有故事。你是怎么收集到这么多好书的？”"],  # 6
        ["学长", "“哈哈，这可是我好几年的积累啊！我从小就爱看书，每次看到好书都忍不住想买下来。后来，我发现自己看的书越来越多，有些书看完后就放在那里积灰，于是就开始在二手市场上卖书，既能腾出空间，又能让好书找到新的主人。”"], 
        ["Narrator", "（向学长提问吧）"],  # 8
        ["你", "“学长，你在读书上一定有很多经验吧？能不能分享一些给我？”"],  # 9
        ["学长", "“当然可以！我觉得学习最重要的是兴趣和坚持。找到自己感兴趣的领域，然后不断地学习和探索，这样才能保持学习的动力。另外，遇到困难时不要轻言放弃，要勇于挑战自己，这样才能不断进步。”"], 
        ["你", "“学长，你觉得这些二手书除了阅读价值外，还有什么特别的意义吗？”"],  # 11
        ["学长", "“当然有！每一本书都承载着作者的思想和情感，它们不仅仅是纸和墨的堆砌，更是文化和智慧的传承。而且，二手书往往有着独特的历史背景和个人印记，它们见证了时代的变迁和个人的成长。所以，我觉得二手书有着无法替代的价值。”"], 
        ["你", "“学长，你在二手市场上一定有很多有趣的经历吧？能不能分享一些给我听听？”"],  # 13
        ["学长", "“可以啊！有一次，我在二手市场上淘到了一本绝版的诗集，当时真是欣喜若狂。后来，我还通过这本书结识了一位同样热爱诗歌的朋友，我们经常一起讨论诗歌和文学。所以，我觉得二手市场不仅是一个买卖商品的地方，更是一个结交朋友、分享快乐的平台。”"], 
        
        ["Narrator", "在交谈中，你感受到了学长对书籍的热爱和对生活的热情，也与他成为了志同道合的朋友。你明白，虽然这次二手市场探秘之旅已经结束，但你的阅读之路和交友之旅才刚刚开始。"], 
        ["Narrator", "你相信，只要保持对知识和友情的追求，总有一天，你也会在这个充满魅力的世界里找到属于自己的位置。"], 
        ["Narrator", "(End.)"], # 17

        ["Narrator", "闲逛一段时间后，你还是决定先回宿舍。你认为目前自己需要更多时间来准备即将到来的作业，同时也想先整理好自己的书架。你打算未来有机会再来继续探访这个充满惊喜的地方。"], 
        ["Narrator", "(End.)"], # 19
    ]
    
