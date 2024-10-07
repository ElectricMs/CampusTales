import random
import time
from Code_Ui import MainMenu


class Game:
    def __init__(self,Ui:MainMenu):
        from Event.event import event

        print("class Game initiating...")
        self.Ui=Ui

        # 存放游戏创建时间
        self.createTime=time.time()

        # 存放游戏重载时间
        self.reloadTime=time.time()

        # 存放所有事件，包括目前的可选事件和不可选事件，格式为 {事件名:事件实例}
        self.allEvents=event.get_all_subEvents(self)

        # 当前正在进行的事件
        self.currentEvent:event
        # 存放所有可选事件的概率，格式为 {事件名:概率}
        self.eventProbablity={}
        
        # 存放已经完成的事件和时间  用什么结构存再议
        self.completedEvents={}

        # 加载可选事件概率
        self.loadEventProbability()
        
        # 存放已加入主线的事件，格式为 [事件名（字符串）]
        self.mainlineEvents=["studies"]

        # 存放时间点，开始时为第一周
        self.timePoint=1

        # 存放每周操作节点，0：展示文字：1：选择事件：2：分配能量 ：3：事件进度状态
        self.weekPoint=0

        # 存放显示属性
        self.displaySetting={"gender":0, "study":60, "health": 60, "mood":60 , "social":60, "ability":60, "money":0}


    # 开始游戏
    def start(self):
        return dialogue.get_random_welcoming()


    # 重新加载游戏
    def reload(self):
        self.reloadTime=time.time()


    # 下一个时间与操作点  点击next的时候调用
    def next(self):
        if self.weekPoint==0:
            print("选择事件状态")
            self.weekPoint=1 # 选择事件状态
            print(self.weekPoint)

            # 这里需要选定一个加载的事件
            if self.loadEvent():
                # 加载成功
                pass
            else:
                self.loadRandomEvent()
            result = self.currentEvent.if_join()
            if result is not None:
                text1, text2 = result
                self.Ui.game_layout_1.label_Text.setText(text1+'\n'+text2)
            else:
                # 处理 None 的情况，例如：
                text1, text2 = "好像出了点问题", "默认文本"
                self.Ui.game_layout_1.label_Text.setText(text1+'\n'+text2)

            print(self.currentEvent.name)

            text1, text2=self.currentEvent.if_join()
            self.Ui.game_layout_1.label_Text.setText(text1)


            # 在这里需要出现随机事件并选择是否进行 默认选no
            self.Ui.game_layout_1.radioButton_NO.show() 
            self.Ui.game_layout_1.radioButton_Yes.show()
            self.Ui.game_layout_1.radioButton_NO.setChecked(True)
            self.Ui.game_layout_1.radioButton_Yes.setChecked(False)

            pass

        elif self.weekPoint==1:
            if self.Ui.game_layout_1.radioButton_Yes.isChecked():
                # 选择了yes
                self.weekPoint=3
                self.next()
                return
            print("分配精力状态")
            self.weekPoint=2 #分配能量状态
            # 在这里需要分配能量
            self.Ui.game_layout_1.radioButton_NO.hide() 
            self.Ui.game_layout_1.radioButton_Yes.hide()
            self.Ui.game_layout_1.label_Text.setText("该如何安排任务呢···")
            self.allocateEnergy()

            self.timePoint+=1
            pass

        elif self.weekPoint==2:
            print("展示文字状态")
            self.weekPoint=0 #展示文字状态
            # 在这里需要展示每周随机的一段文字
            self.Ui.game_layout_1.label_Text.setText(dialogue.get_random_talk())

            pass

        elif self.weekPoint==3:
            self.weekPoint=1 #点击next后分配能量
            self.Ui.game_layout_1.radioButton_NO.hide() 
            self.Ui.game_layout_1.radioButton_Yes.hide()
            self.Ui.game_layout_1.radioButton_NO.setChecked(True)
            self.Ui.game_layout_1.radioButton_Yes.setChecked(False)

            print("进入支线")   # 选择了yes
            self.currentEvent.event_start()

            
            pass

        pass


    # 分配能量
    def allocateEnergy(self):
        # 这里需要分配精力
        # 学习 运动 社交 娱乐





        pass


    # 加载随机事件
    def loadRandomEvent(self):
        if self.eventProbablity=={}:
            self.loadEventProbability()
        
        # 获取所有事件的列表和对应的权重列表
        event_keys = list(self.eventProbablity.keys())
        weights = list(self.eventProbablity.values())

        # 使用 random.choices 进行加权随机选择
        # 参数 k 表示抽取的次数，这里我们只抽取一次
        selected_event = random.choices(event_keys, weights=weights, k=1)

        # 判断选择的事件是否可行
        if selected_event[0].require():
            self.currentEvent=selected_event[0]
            return
        else:
            self.loadRandomEvent()
            return


    # 加载特定事件
    def loadEvent(self):
        if self.timePoint==1:
            # 第一周的事件
            self.currentEvent=self.allEvents["test"]
            return True
        elif self.timePoint==2:
            # 第二周的事件
            self.currentEvent=self.allEvents["test"]
            return True
        elif self.timePoint==3:
            # 第三周的事件
            self.currentEvent=self.allEvents["test"]
            return True
        return False

        
    # 刷新事件概率
    def loadEventProbability(self):

        for event in self.allEvents.values():
            self.eventProbablity[event.name]=event.probability
        pass

    # 结束一周
    def endWeek(self):
        self.timePoint+=1
        # 这里需要有更多的操作
        pass







class dialogue:
    welcoming=[
        "这是我上大学的第一天。天哪，我可不能摆烂。",
        "这是我的第一天大学生活，我得好好准备一下。",
        "今天是我大学的第一天，我要好好学习。",
        "这是我上大学的第一天，烦死了这学我真是上不了一点。"
    ]

    @classmethod
    def get_random_welcoming(cls):
        return random.choice(dialogue.welcoming)


    random_talk=[
        """
            今天我7:50才起床，好险，差点赶不上八点的课了。昨天晚上和室友一起熬夜玩游戏，一不小心就到了凌晨两点。
        """,
        """
            今天天气不错，阳光明媚，适合户外活动。早上没有课，我决定早起去操场跑步，顺便呼吸一下新鲜空气。
        """,
        """
            昨晚和室友一起看了部电影，不知不觉就到了深夜。匆忙洗漱后，一路小跑到教室，还好最后赶上了。
        """,
        """
            今天天气特别好，阳光明媚。早上起来后，我决定去校园里散散步，享受一下早晨的宁静。
        """,
        """
            今天是周五，心情特别好。早上8点的课是文学欣赏，老师讲了一篇经典的短篇小说，让我们受益匪浅。
        """,
    ]

    @classmethod
    def get_random_talk(cls):
        return random.choice(dialogue.random_talk).lstrip()
    


class RandomEvents:
    def __init__(self, game):
        self.game = game
        self.events = []
        self.weight = []
        

    def add_random_events(self):
        self.events.extend([
            self.RandomEvent("外卖被偷", 0.1, "期待的美食被偷走，心情大受打击，感到非常失落。", mood=-5),
            self.RandomEvent("崴脚", 0.05, "不小心崴到脚，影响了日常活动，身体状况明显下降，去医院看病花费200。", health=-15, money=-200),
            self.RandomEvent("参加志愿活动", 0.2, "参与志愿活动不仅帮助了他人，还结识了志同道合的新朋友。", social=10),
            self.RandomEvent("遇到难以相处的室友", 0.15, "室友情侣生活习惯不合，造成矛盾，影响了居住环境的舒适度。", social=-10, mood=-5),
            self.RandomEvent("偶遇校园流浪猫", 0.1, "在校园里遇到一只可爱的流浪猫，瞬间治愈了烦躁的心情。", mood=5),
            self.RandomEvent("完成重要作业", 0.2, "按时完成了一项重要的作业，感到非常有成就感和轻松。", study=10, mood=5),
            self.RandomEvent("旷课点上名", 0.1, "原本打算请假，没想到被点名，感到既尴尬又懊恼。", study=-5, mood=-5),
            self.RandomEvent("突如其来的考试", 0.15, "突然得知有考试，心里没底，焦虑感上升，学习进度受影响。", study=-10, mood=-5),
            self.RandomEvent("失物招领", 0.1, "找到了之前丢失的书籍或电子产品，心情立刻变得愉悦。", mood=5),
            self.RandomEvent("好友请客", 0.1, "好友请你一起吃饭，增进了友谊，心情倍感愉悦。", mood=10, social=5),
            self.RandomEvent("突发的生病", 0.05, "生病让无法参加课程和活动，心情也因此变得低落，去医院看病费300。", health=-10, study=-5, mood=-5, money=-300),
            self.RandomEvent("校园活动取消", 0.1, "本以为期待已久的校园活动会很有趣，却因取消而失望。", social=-5, mood=-5),
            self.RandomEvent("遇到老朋友", 0.1, "偶然与老朋友重逢，回忆起往昔美好时光，心情愉悦。", social=10, mood=5),
            self.RandomEvent("借书未归还", 0.05, "忘记归还的书，受到催促，感到有些尴尬和愧疚。", study=-5, mood=-5),
            self.RandomEvent("收到意外的情书", 0.1, "收到暗恋对象的情书，心情欢喜，觉得自己被重视和喜欢。", mood=10, social=5)
        ])

        for event in self.events:
            self.weight.append(event.probability)


    def get_random_event(self):
        return random.choices(self.events, weights=self.weight, k=1)[0]


    class RandomEvent:
        def __init__(self, name: str, probability: float, description: str, **kwargs) -> None:
            self.name = name
            self.probability = probability
            self.description = description
            self.kwargs = kwargs
            # 要求kwargs有效参数如下：
            # study health mood social ability money

        def impact(self, outer_instance):
            if "study" in self.kwargs:
                outer_instance.game.displaySetting["study"] += self.kwargs["study"]
            if "health" in self.kwargs:
                outer_instance.game.displaySetting["health"] += self.kwargs["health"]
            if "mood" in self.kwargs:
                outer_instance.game.displaySetting["mood"] += self.kwargs["mood"]
            if "social" in self.kwargs:
                outer_instance.game.displaySetting["social"] += self.kwargs["social"]
            if "ability" in self.kwargs:
                outer_instance.game.displaySetting["ability"] += self.kwargs["ability"]
            if "money" in self.kwargs:
                outer_instance.game.displaySetting["money"] += self.kwargs["money"]
    