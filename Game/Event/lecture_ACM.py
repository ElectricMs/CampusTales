from. import event as Event
from main import Game
from typing import Tuple
from abc import ABC, abstractmethod
import asyncio
from PySide6.QtCore import QEventLoop
from .DirectedGraph import DirectedGraph



class event_lecture_ACM(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="lecture ACM", description="ACM竞赛讲座，不用agent", Game=Game)
        self.probability=0
        self.layout=self.game.Ui.game_layout_choose_model_1
       

    def if_join(self)-> Tuple[str, str]:
        return "听说学校组织了ACM竞赛讲座","我要不要去看看呢？"


    def event_start(self, **kwargs):
        print("event_lecture_ACM start")
        
        
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


    def next(self, pos = None):

        self.step += 1
        if self.step >= len(self.dialogue_list) or self.step == 20:
            self.event_end()
            return
        
        elif self.step == 6:
            if pos == 1:# Yes
                pass
            elif pos == 2:# No
                self.step = 20
        
        elif self.step == 11:
            if pos ==1:
                pass
            elif pos == 2:
                self.step = 13
            elif pos == 3:
                self.step = 15

        elif self.step == 13:
            self.step = 18
        elif self.step == 15:
            self.step = 18


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
        
        self.layout.pushButton_next.show()
        self.layout.pushButton_option1.hide()
        self.layout.pushButton_option2.hide()
        self.layout.pushButton_option3.hide()

        if self.step == 5:
            user_choice("Yes", "No")# 6/20
            self.layout.pushButton_next.hide()
        elif self.step == 10:
            user_choice("询问竞赛准备", "探讨团队协作", "分享个人经历")
            self.layout.pushButton_next.hide()
   

        
    def event_end(self):
        self.refreshProbability()
        self.affection()
        self.game.Ui.stacked_layout.setCurrentIndex(3)
        


    def refreshProbability(self):
        pass


    def affection(self,*args):
        self.game.mainlineEvents.append(["ACM竞赛", 0])
        self.game.refreshMissionList()

        pass

    

    dialogue_list = [
        ["Narrator", "在一个秋意渐浓的午后，阳光斑驳地洒在校园的每一个角落，为即将开始的ACM竞赛讲座增添了几分热烈与期待。"] # 0
        ,["Narrator", "在学生活动中心，一个由横幅和海报装饰的讲台格外引人注目，上面写着：“ACM竞赛深度解析——编程与智慧的较量”。"] # 1
        ,["Narrator", "此时，一位身着整洁校服、眼神坚定的学生代表站上了讲台，他满怀激情地向围观的同学们介绍着。"] # 2
        ,["学生代表", "“大家好！欢迎各位来到我们的ACM竞赛讲座！这是一个了解编程竞赛、提升编程能力的绝佳机会。无论你是编程新手，还是已经在ACM竞赛中摸爬滚打的老将，今天这场讲座都将为你带来全新的视角和启发。快来加入我们，一起探索编程的奥秘吧！”"] # 3
        ,["Narrator", "你站在讲台前，仔细聆听着学生代表的介绍，心中充满了对ACM竞赛的好奇与向往。你环顾四周，发现许多同学都露出了跃跃欲试的表情。"] # 4
        ,["Narrator", "你思考着要不要参加这场讲座。"] # 5

        ,["Narrator", "随着讲座主持人的一声“感谢大家的聆听”，整场ACM竞赛讲座缓缓落下了帷幕。你坐在讲座的最后一排，目光紧紧跟随着主持人的身影，直到他完全消失在视线之外。此刻，你的心中充满了满足与感慨。"] # 6
        ,["Narrator", "在讲座的这段时间里，你仿佛进入了一个全新的世界，一个由编程、算法和逻辑构成的奇妙空间。讲座的内容丰富多彩，从ACM竞赛的历史背景到比赛规则，从编程技巧的提升到团队协作的重要性，每一个细节都让你受益匪浅。"] # 7
        ,["Narrator", "你记得讲座中那些生动有趣的案例，它们让你深刻理解了ACM竞赛的魅力所在。你也记得主持人分享的那些竞赛经验，它们如同一盏明灯，照亮了你前行的道路。此刻，你仿佛已经看到了自己在未来的ACM竞赛中奋力拼搏的身影。"] # 8
        ,["Narrator", "你缓缓站起身来，手中紧握着记满了讲座要点的笔记本，心中充满了对ACM竞赛的浓厚兴趣与热情。你决定抓住这次难得的机会，去咨询讲座的老师，进一步了解这个充满挑战与机遇的领域。"] # 9
        ,["Narrator", "你走向讲台，礼貌地向老师表达了你的意愿。老师微笑着看着你，眼中闪烁着鼓励的光芒。你们开始了一段深入的交流："] # 10
        
        ,["你", "“老师，请问在准备ACM竞赛时，有哪些方面是需要特别注意的？比如，是否需要提前学习某些特定的编程语言或算法？”"] # 11
        ,["老师", "“确实，团队协作在ACM竞赛中扮演着至关重要的角色。一个优秀的团队应该根据成员的特点和优势进行合理的分工。比如，有的人擅长算法设计，有的人则擅长编程实现。在比赛中，大家要紧密配合、相互支持，共同面对挑战和解决问题。”"] # 12
        ,["你", "“老师，您在ACM竞赛中有哪些难忘的经历或感悟可以分享给我吗？这些经历对我未来参与竞赛会有很大的帮助。”"] # 13
        ,["老师", "“确实，团队协作在ACM竞赛中扮演着至关重要的角色。一个优秀的团队应该根据成员的特点和优势进行合理的分工。比如，有的人擅长算法设计，有的人则擅长编程实现。在比赛中，大家要紧密配合、相互支持，共同面对挑战和解决问题。”"] # 14
        ,["你", "“老师，您在ACM竞赛中有哪些难忘的经历或感悟可以分享给我吗？这些经历对我未来参与竞赛会有很大的帮助。”"] # 15
        ,["老师", "“当然可以。我记得在我第一次参加ACM竞赛时，面对复杂的题目和紧张的比赛氛围，我感到非常迷茫和焦虑。但是，在团队成员的相互鼓励和支持下，我逐渐找到了自己的节奏和信心。最终，我们团队取得了不错的成绩。这次经历让我深刻体会到了团队协作的重要性，也让我更加坚定了自己参与竞赛的决心。”"] # 16
        
        ,["Narrator", "在交谈中，你感受到了老师对ACM竞赛的热爱与执着，也更加坚定了自己参与竞赛的决心。你明白，虽然讲座已经结束，但你的编程之路和竞赛之旅才刚刚开始。"] # 17
        ,["Narrator", "你相信，只要不断努力、不断进取，总有一天，你也会在ACM竞赛的舞台上展现出自己的实力，绽放属于自己的光芒。"] # 18
        ,["Narrator", "End.\n(解锁事件：ACM竞赛)"] # 19
        
        ,["Narrator", "尽管你对ACM竞赛讲座充满了好奇与期待，但经过深思熟虑后，你还是决定暂时不参加。你认为目前自己需要更多时间来准备作业，同时也想先巩固自己的编程基础。"] # 20
        ,["Narrator", "在广场上，你与同学们挥手告别，并约定未来有机会再一起参加ACM竞赛的活动。虽然这次没有参加讲座，但这次预告让你更加了解了ACM竞赛的魅力和挑战，也为你的编程之路指明了一个方向。"] # 21
        ,["Narrator", "End."] # 22
    ]


    
    dialogue = DirectedGraph()
    dialogue.add_node(1, "Narrator", "在一个秋意渐浓的午后，阳光斑驳地洒在校园的每一个角落，为即将开始的ACM竞赛讲座增添了几分热烈与期待。")
    dialogue.add_node(2, "Narrator", "在学生活动中心，一个由横幅和海报装饰的讲台格外引人注目，上面写着：“ACM竞赛深度解析——编程与智慧的较量”。")
    dialogue.add_node(3, "Narrator", "此时，一位身着整洁校服、眼神坚定的学生代表站上了讲台，他满怀激情地向围观的同学们介绍着。")
    dialogue.add_node(4, "学生代表", "“大家好！欢迎各位来到我们的ACM竞赛讲座！这是一个了解编程竞赛、提升编程能力的绝佳机会。无论你是编程新手，还是已经在ACM竞赛中摸爬滚打的老将，今天这场讲座都将为你带来全新的视角和启发。快来加入我们，一起探索编程的奥秘吧！”")
    dialogue.add_node(5, "Narrator", "你站在讲台前，仔细聆听着学生代表的介绍，心中充满了对ACM竞赛的好奇与向往。你环顾四周，发现许多同学都露出了跃跃欲试的表情。")
    dialogue.add_node(6, "Narrator", "你思考着要不要参加这场讲座。")
    # Yes
    dialogue.add_node(7, "Narrator", "随着讲座主持人的一声“感谢大家的聆听”，整场ACM竞赛讲座缓缓落下了帷幕。你坐在讲座的最后一排，目光紧紧跟随着主持人的身影，直到他完全消失在视线之外。此刻，你的心中充满了满足与感慨。")
    dialogue.add_node(8, "Narrator", "在讲座的这段时间里，你仿佛进入了一个全新的世界，一个由编程、算法和逻辑构成的奇妙空间。讲座的内容丰富多彩，从ACM竞赛的历史背景到比赛规则，从编程技巧的提升到团队协作的重要性，每一个细节都让你受益匪浅。")
    dialogue.add_node(9, "Narrator", "你记得讲座中那些生动有趣的案例，它们让你深刻理解了ACM竞赛的魅力所在。你也记得主持人分享的那些竞赛经验，它们如同一盏明灯，照亮了你前行的道路。此刻，你仿佛已经看到了自己在未来的ACM竞赛中奋力拼搏的身影。")
    dialogue.add_node(10, "Narrator", "你缓缓站起身来，手中紧握着记满了讲座要点的笔记本，心中充满了对ACM竞赛的浓厚兴趣与热情。你决定抓住这次难得的机会，去咨询讲座的老师，进一步了解这个充满挑战与机遇的领域。")
    dialogue.add_node(11, "Narrator", "你走向讲台，礼貌地向老师表达了你的意愿。老师微笑着看着你，眼中闪烁着鼓励的光芒。你们开始了一段深入的交流：")
    # A
    dialogue.add_node(12, "你", "“老师，请问在准备ACM竞赛时，有哪些方面是需要特别注意的？比如，是否需要提前学习某些特定的编程语言或算法？”")
    dialogue.add_node(13, "老师", "“确实，团队协作在ACM竞赛中扮演着至关重要的角色。一个优秀的团队应该根据成员的特点和优势进行合理的分工。比如，有的人擅长算法设计，有的人则擅长编程实现。在比赛中，大家要紧密配合、相互支持，共同面对挑战和解决问题。”")
    # B
    dialogue.add_node(14, "你", "“老师，您在ACM竞赛中有哪些难忘的经历或感悟可以分享给我吗？这些经历对我未来参与竞赛会有很大的帮助。”")
    dialogue.add_node(15, "老师", "“确实，团队协作在ACM竞赛中扮演着至关重要的角色。一个优秀的团队应该根据成员的特点和优势进行合理的分工。比如，有的人擅长算法设计，有的人则擅长编程实现。在比赛中，大家要紧密配合、相互支持，共同面对挑战和解决问题。”")
    # C
    dialogue.add_node(16, "你", "“老师，您在ACM竞赛中有哪些难忘的经历或感悟可以分享给我吗？这些经历对我未来参与竞赛会有很大的帮助。”")
    dialogue.add_node(17, "老师", "“当然可以。我记得在我第一次参加ACM竞赛时，面对复杂的题目和紧张的比赛氛围，我感到非常迷茫和焦虑。但是，在团队成员的相互鼓励和支持下，我逐渐找到了自己的节奏和信心。最终，我们团队取得了不错的成绩。这次经历让我深刻体会到了团队协作的重要性，也让我更加坚定了自己参与竞赛的决心。”")
    # End 1
    dialogue.add_node(18, "Narrator", "在交谈中，你感受到了老师对ACM竞赛的热爱与执着，也更加坚定了自己参与竞赛的决心。你明白，虽然讲座已经结束，但你的编程之路和竞赛之旅才刚刚开始。")
    dialogue.add_node(19, "Narrator", "你相信，只要不断努力、不断进取，总有一天，你也会在ACM竞赛的舞台上展现出自己的实力，绽放属于自己的光芒。")
    dialogue.add_node(20, "Narrator", "End.\n(解锁事件：ACM竞赛)")
    # End 2
    dialogue.add_node(21, "Narrator", "尽管你对ACM竞赛讲座充满了好奇与期待，但经过深思熟虑后，你还是决定暂时不参加。你认为目前自己需要更多时间来准备作业，同时也想先巩固自己的编程基础。")
    dialogue.add_node(22, "Narrator", "在广场上，你与同学们挥手告别，并约定未来有机会再一起参加ACM竞赛的活动。虽然这次没有参加讲座，但这次预告让你更加了解了ACM竞赛的魅力和挑战，也为你的编程之路指明了一个方向。")
    dialogue.add_node(23, "Narrator", "End.")

    dialogue.add_edge(1, 2)
    dialogue.add_edge(2, 3)
    dialogue.add_edge(3, 4)
    dialogue.add_edge(4, 5)
    dialogue.add_edge(5, 6)

    dialogue.add_edge(6, 7)
    dialogue.add_edge(6, 21)
    dialogue.add_edge(21, 22)
    dialogue.add_edge(22, 23)

    dialogue.add_edge(7, 8)
    dialogue.add_edge(8, 9)
    dialogue.add_edge(9, 10)
    dialogue.add_edge(10, 11)

    dialogue.add_edge(11, 12)
    dialogue.add_edge(12, 13)
    dialogue.add_edge(11, 14)
    dialogue.add_edge(14, 15)
    dialogue.add_edge(11, 16)
    dialogue.add_edge(16, 17)

    dialogue.add_edge(13, 18)
    dialogue.add_edge(15, 18)
    dialogue.add_edge(17, 18)
    dialogue.add_edge(18, 19)
    dialogue.add_edge(19, 20)



