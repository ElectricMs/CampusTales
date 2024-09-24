import random
import time
from Code_Ui import MainMenu

class Game:
    def __init__(self,Ui:MainMenu):

        print("class Game initiating...")
        self.Ui=Ui

        # 存放游戏创建时间
        self.createTime=time.time()

        # 存放游戏重载时间
        self.reloadTime=time.time()

        # 存放所有事件，包括目前的可选事件和不可选事件，格式为 {事件名:事件实例}
        self.allEvents=event.get_all_subEvents(self)

        # 存放所有可选事件，格式为 {事件名:事件对象}
        self.optionalEvents={}

        # 当前正在进行的事件
        self.currentEvent=None

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
            self.Ui.game_layout_1.label_Text.setText("出现了新的事件")
            # 在这里需要出现随机事件并选择是否进行 默认选no
            self.Ui.game_layout_1.radioButton_NO.show() 
            self.Ui.game_layout_1.radioButton_Yes.show()
            self.Ui.game_layout_1.radioButton_NO.setChecked(True)
            self.Ui.game_layout_1.radioButton_Yes.setChecked(False)
            # 这边想加一点文字函数，注意修改函数调用
            # self.Ui.game_layout_1.radioButton_NO.clicked.connect(self.next)
            # self.Ui.game_layout_1.radioButton_Yes.clicked.connect(self.next)




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

            pass

        elif self.weekPoint==2:
            print("展示文字状态")
            self.weekPoint=0 #展示文字状态
            # 在这里需要展示每周随机的一段文字
            self.Ui.game_layout_1.label_Text.setText(dialogue.get_random_talk())

            pass

        elif self.weekPoint==3:
            print("进入支线")
            self.weekPoint=1 #点击next后分配能量
            self.Ui.game_layout_1.radioButton_NO.hide() 
            self.Ui.game_layout_1.radioButton_Yes.hide()
            self.Ui.game_layout_1.radioButton_NO.setChecked(True)
            self.Ui.game_layout_1.radioButton_Yes.setChecked(False)
            self.Ui.game_layout_1.label_Text.setText("选择参与新的事件，在这里加入aigc，将事件加入主线")
            pass

        pass


    # 分配能量
    def allocateEnergy(self):
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
            return selected_event[0]
        else:
            return None


    # 加载特定事件
    def loadEvent(self,event):
        pass

        
    # 刷新事件概率
    def loadEventProbability(self):

        for event in self.optionalEvents:
            self.eventProbablity[event.name]=event.probability
        pass

    # 结束一周
    def endWeek(self):
        self.timePoint+=1
        # 这里需要有更多的操作
        pass














class event:
    def __init__(self,name=None,time=time.time(),description=None,Game=None):
        self.name=name
        self.time=time
        self.description=description
        self.ui=None
        self.setting=None
        self.probability=1

    # 获取所有子类
    @classmethod
    def get_all_subEvents(cls, Game):
        subEvents={}
        subEvents.update({'studies':event_studies(Game)})
        
        return subEvents
    
    def require(self):
        
        return True
    

    # 刷新概率，在事件结束时调用
    def refreshProbability(self):
        pass

    
    # 事件影响
    def affection(self,*args):
                    
        pass
    



class event_crush_atFirstBlush(event):
    pass


class event_studies(event):
    def __init__(self,Game,name='studies',time=time.time(),description='学习'):
        super().__init__(name,time,description,Game)
        self.probability=0

    def require(self):
        return True

    # 刷新概率，在事件结束时调用
    def refreshProbability(self):
        pass

    # 事件影响
    def affection(self,*args):
        pass







    pass








class dialogue:
    welcoming=[
        "这是我上大学的第一天。天哪，我可不能摆烂",
        "这是我的第一天大学生活，我得好好准备一下",
        "今天是我大学的第一天，我要好好学习",
        "这是我上大学的第一天，烦死了这学我真是上不了一点"
    ]

    @classmethod
    def get_random_welcoming(cls):
        return random.choice(dialogue.welcoming)









    random_talk=[
        """
            今天我7:50才起床，好险，差点赶不上八点的课了。昨天晚上和室友一起熬夜讨论期末项目的事情，没想到一不小心就到了凌晨两点。匆匆忙忙地洗漱完，抓起书包就往外跑，还好学校不大，最后还是赶上了。上午的课讲的是数据结构，虽然有点困，但还是努力跟上了老师的节奏。下午的课程结束后，我和几个同学去了图书馆准备小组作业，一直忙到天黑。晚饭后，我们又聚在一起打了一局游戏，算是对自己一天辛勤学习的奖励吧。
        """,
        """
            今天天气不错，阳光明媚，适合户外活动。早上没有课，我决定早起去操场跑步，顺便呼吸一下新鲜空气。跑了两圈之后，感觉整个人都精神了许多。回来的路上，遇到了几个老同学，我们一起去了学校附近的咖啡馆，边喝咖啡边聊起了最近的生活和学习情况。
        """,
        """
            昨晚和室友一起看了部电影，不知不觉就到了深夜。匆忙洗漱后，一路小跑到教室，还好最后赶上了。上午的课程是心理学，老师讲得非常生动有趣，让我对这门学科产生了浓厚的兴趣。中午和几个同学在学校食堂吃饭，聊了聊各自的兴趣爱好和未来的打算。
        """,
        """
            今天天气特别好，阳光明媚。早上起来后，我决定去校园里散散步，享受一下早晨的宁静。走了一圈回来，感觉整个人都精神了许多。上午的课程是计算机编程，老师布置了一个新的项目任务，需要我们在一周内完成。
        """,
        """
            今天是周五，心情特别好。早上8点的课是文学欣赏，老师讲了一篇经典的短篇小说，让我们受益匪浅。中午和几个好朋友去学校附近的一家餐厅吃了午餐，点了我们最喜欢的菜。
        """,
    ]

    @classmethod
    def get_random_talk(cls):
        return random.choice(dialogue.random_talk).lstrip()