import random
import time
import copy
from cover_start import MyWindow
from PySide6.QtWidgets import QPushButton,QLabel
from PySide6.QtCore import QRect,Qt,Signal
from PySide6.QtGui import QFont
from activity.randoan_read_io import db_connection



class ClickableLabel(QLabel):
    clicked = Signal()  # 定义一个点击信号
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMouseTracking(True)  # 启用鼠标跟踪

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()  # 发送点击信号
        super().mousePressEvent(event)



class Game:
    def __init__(self,Ui:MyWindow):
        from Event.event import Event

        print("class Game initiating...")
        self.Ui=Ui

        # 存放游戏创建时间
        self.createTime=time.time()

        # 存放游戏重载时间
        self.reloadTime=time.time()

        # 存放游戏进度
        self.progress={"layout":-1}

        # 存放所有事件，包括目前的可选事件和不可选事件，格式为 {事件名:事件实例}
        self.allEvents=Event.get_all_subEvents(self)

        # 当前正在进行的事件
        self.currentEvent:Event
        
        # 存放所有可选事件的概率，格式为 {事件名:概率}
        self.eventProbablity={}
        
        # 存放已经完成的事件和时间  用什么结构存再议
        self.completedEvents={}

        # 加载可选事件概率
        self.loadEventProbability()
        
        # 存放已加入主线的事件，格式为 [事件名（字符串）]
        self.mainlineEvents=[["学习",0], ["锻炼",0], ["社交",0],["娱乐",0]]
        
        # 存放每周精力，结束后重新设置为10
        self.energy=10
        
        # 存放时间点，开始时为第一周
        self.week = 0

        # 存放显示属性
        self.displaySetting={"gender":0, "study":10, "health": 60, "mood":60 , "social":40, "ability":60, "money":12000, "club":0, "organization":0, "lecture":0, "beloved":0}

        # 初始化内嵌函数
        self.allocateEnergy()

        # 初始化随机事件
        self.randomEvents=RandomEvents(self)

        # 存放每周精力分配结果
        self.allocateResults=[]

        # 存放每周事件结果
        self.eventResults=[]




    # 开始游戏
    def start(self):
        # 黑屏过场动画
        self.Ui.stacked_layout.setCurrentIndex(4) # Animation
        # self.Ui.stacked_layout.setCurrentIndex(3) # allocateEnergy
        self.Ui.game_layout_initialAnimation.page=1
        self.Ui.game_layout_initialAnimation.start_flow_text()

        self.loadEvent()
        self.progress["layout"]=3
        self.Ui.game_layout_allocateEnergy.label_content.setText(self.currentEvent.if_join()[0] + "," + self.currentEvent.if_join()[1]) 
        self.Ui.game_layout_allocateEnergy.frame_modal.setVisible(True)
        self.Ui.game_layout_allocateEnergy.label_money_value.setText(str(self.displaySetting["money"]))

        def disablePushButton():
            self.Ui.game_layout_allocateEnergy.pushButton_minus1.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus2.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus3.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus4.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus5.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus1.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus2.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus3.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus4.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus5.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_next.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_previousPage.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_nextPage.setEnabled(False)

        disablePushButton()


    # 重新加载游戏
    def reload(self):
        self.reloadTime=time.time()
        if self.progress["layout"]!=-1:
            self.Ui.stacked_layout.setCurrentIndex(self.progress["layout"])
        else:
            print("self.progress['layout']=-1, cannot reload game")


    # 选择True的事件
    def event_true(self):
        self.Ui.game_layout_allocateEnergy.frame_modal.setVisible(False)
        self.progress["layout"]=2
        self.currentEvent.event_start()

        def enablePushButton():
            self.Ui.game_layout_allocateEnergy.pushButton_minus1.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus2.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus3.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus4.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus5.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus1.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus2.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus3.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus4.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus5.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_next.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_previousPage.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_nextPage.setEnabled(True)

        enablePushButton()
        self.allocateEnergy()


    # 选择False的事件
    def event_false(self):
        self.Ui.game_layout_allocateEnergy.frame_modal.setVisible(False)

        def enablePushButton():
            self.Ui.game_layout_allocateEnergy.pushButton_minus1.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus2.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus3.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus4.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus5.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus1.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus2.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus3.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus4.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus5.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_next.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_previousPage.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_nextPage.setEnabled(True)

        enablePushButton()
        self.allocateEnergy()


    # 下一页日记  点击diary next的时候调用
    def next(self):
        # 我暂定日记只会展示一页好了，后面再改成可以展示多页的形式
        self.Ui.game_layout_allocateEnergy.blur_recover()
        self.loadEvent()
        self.Ui.game_layout_allocateEnergy.label_content.setText(self.currentEvent.if_join()[0] + "," + self.currentEvent.if_join()[1]) 
        self.Ui.game_layout_allocateEnergy.frame_modal.setVisible(True)
        self.Ui.game_layout_allocateEnergy.label_money_value.setText(str(self.displaySetting["money"]))
        #wyd加的用于暂停定时器
        self.Ui.game_layout_allocateEnergy.widget_diary.label_diary_content.timer.stop()
        def disablePushButton():
            self.Ui.game_layout_allocateEnergy.pushButton_minus1.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus2.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus3.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus4.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_minus5.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus1.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus2.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus3.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus4.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_plus5.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_next.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_previousPage.setEnabled(False)
            self.Ui.game_layout_allocateEnergy.pushButton_nextPage.setEnabled(False)

        disablePushButton()
        

    # 点击下一周时触发
    def nextWeek(self):
        self.week+=1
        # 首先保存分配结果，清空精力分配
        week_result = copy.deepcopy(self.mainlineEvents)
        week_result.append(["休息",self.energy])
        self.allocateResults.append(week_result)
        # test
        for result in week_result:
            print(result[0],":",result[1],end=" ")
        print()


        # 重新更新精力
        self.energy=10
        for mission in self.mainlineEvents:
            mission[1]=0
        self.refreshMissionList()


        # 返回diary文字
        def returnDiaryText() -> str:
            # 一个基于近3周的事件结果生成日记的算法
            # [["学习",0], ["锻炼",0], ["社交",0],["娱乐",0]]
            allocate_count={}
            for i in range(max(0,len(self.allocateResults)-3),self.week):
                for event in self.allocateResults[i]:
                    allocate_count[event[0]]=allocate_count.get(event[0],0)+event[1]
            compensate = 0 if len(self.allocateResults)>=3 else 3-len(self.allocateResults)
        

            def escape_get_random_activity(category, energy_level)->str:
                if energy_level==0 or energy_level==1:
                    return db_connection.get_random_activity(category, "0~20")
                elif energy_level==2 or energy_level==3:
                    return db_connection.get_random_activity(category, "20~40")
                elif energy_level==4 or energy_level==5:
                    return db_connection.get_random_activity(category, "40~60")
                elif energy_level==6 or energy_level==7:
                    return db_connection.get_random_activity(category, "60~80")
                elif energy_level>=8:
                    return db_connection.get_random_activity(category, "80~100")
                else:
                    return f"Error: {category} {energy_level}"

            text=""
            for key, value in allocate_count.items():
                if key == "学习":
                    text += escape_get_random_activity("认真学习", value+compensate) + "\n"
                    print(text)
                elif key == "锻炼":
                    text += escape_get_random_activity("体育运动", value+compensate) + "\n"
                    print(text)
                elif key == "社交":
                    text += escape_get_random_activity("广泛交友", value+compensate) + "\n"
                    print(text)
                elif key == "娱乐":
                    text += escape_get_random_activity("打游戏娱乐", value+compensate) + "\n"
                    print(text)
                elif key == "休息":
                    text += escape_get_random_activity("休息放松", value+compensate) + "\n"
                    print(text)
                elif key == "陪npy":
                    # 这种事件调用事件的判断函数
                    pass
            return text
        

        # 调整属性
        def adjustSetting(week_result: list[list]) -> None:
            for result in week_result:
                if result[0] == "学习":
                    self.displaySetting["study"]+=result[1]*0.5
                    self.displaySetting["mood"]-=result[1]*0.25
                    self.displaySetting["health"]-=result[1]*0.25
                elif result[0] == "锻炼":
                    self.displaySetting["health"]+=result[1]*1.25
                    self.displaySetting["mood"]+=result[1]*0.75
                elif result[0] == "社交":
                    self.displaySetting["social"]+=result[1]*1
                    self.displaySetting["money"]-=result[1]*100
                elif result[0] == "娱乐":
                    self.displaySetting["mood"]+=result[1]*0.75
                    self.displaySetting["health"]-=result[1]*0.25
                    self.displaySetting["money"]-=result[1]*100
                elif result[0] == "休息":
                    self.displaySetting["health"]+=result[1]*0.5
                    self.displaySetting["mood"]+=result[1]*0.75

        adjustSetting(week_result)

        # 模糊效果，出现日记本
        # 日记本中点击next按钮出现事件modal和能量分配按钮
        self.Ui.game_layout_allocateEnergy.blur()
        
        ui = self.Ui.game_layout_allocateEnergy
        diary_text = ""
        if self.week == 1:
            diary_text += dialogue.get_random_welcoming()
        elif self.week >= 16:
            diary_text += dialogue.get_random_talk_terminal()
        else:
            diary_text += dialogue.get_random_talk()
        # print("diary text1:",diary_text)
        randomEvent = self.randomEvents.get_random_event()
        diary_text += "\n" + randomEvent.description
        # print("diary text2:",diary_text)
        diary_text += "\n" + returnDiaryText()
        ui.widget_diary.label_diary_content.setTextToDraw(diary_text)
        # ui.label_diary_content.setText(diary_text)
        # test
        for k,v in self.displaySetting.items():
            print(k,":",v,end=" ")
        print()


    # 分配能量
    def allocateEnergy(self):
        # 这里需要分配精力
        # 学习 运动 社交 娱乐 
        # 附加：陪npy 竞赛 科研 等
        count = len(self.mainlineEvents)
        page = count//5+1 if count%5!=0 else count//5
        pageNow = 1
        for item in self.Ui.game_layout_allocateEnergy.frame_selectArea.findChildren(ClickableLabel):
            item.setParent(None)
            item.deleteLater()
            item = None
        
                
        #初始y的偏移量
        y_offset = 0
        num=1
        for mission in self.mainlineEvents:
            # 为按钮添加槽函数
            # 还没加
            
            tmp_str=str(num)+"、"+mission[0]

            
            label=ClickableLabel(tmp_str,self.Ui.game_layout_allocateEnergy.frame_selectArea)
            font1 = QFont()
            font1.setFamilies([u"\u5343\u56fe\u7b14\u950b\u624b\u5199\u4f53"])
            font1.setPointSize(17)
            font1.setBold(True)
            label.setGeometry(QRect(0,0,100,30))
            label.setFont(font1)
            label.setStyleSheet(u"background-color: transparent;\n")
            label.move(350,y_offset)
            #self.Ui.game_layout_allocateEnergy.frame_selectArea_layout.addWidget(label)
            y_offset+=28
            label.show()
            num+=1
        # print("nihao")
           

        def pageTuning(value):
            assert value in [1, -1], "Value must be either 1 or -1"
            nonlocal pageNow
            nonlocal page
            if value==1:
                if pageNow<page:
                    print("next page")
                    pageNow+=1
                    refreshMissionList()
                pass
            else: # value==-1
                if pageNow>1:
                    print("previous page")
                    pageNow-=1
                    refreshMissionList()
                pass


        def modifyEnergy(value, position):
            assert value in [1, -1], "Value must be either 1 or -1"
            assert position in [1, 2, 3, 4, 5], "Position must be between 1 and 5"
            nonlocal pageNow
            if value==1:
                if self.energy > 0:
                    self.mainlineEvents[(pageNow-1)*5+position-1][1]+=1
                    self.energy-=1
            else: # value==-1
                if self.mainlineEvents[(pageNow-1)*5+position-1][1]>0:
                    self.mainlineEvents[(pageNow-1)*5+position-1][1]-=1
                    self.energy+=1
            refreshMissionList()

        
        def refreshMissionList():
            nonlocal count
            nonlocal pageNow
            maxMission = count if count < pageNow * 5 else pageNow * 5
            missionList = self.mainlineEvents[(pageNow-1)*5:maxMission]
            for  item in missionList:
                print(item[0], ' ', item[1])
            self.Ui.game_layout_allocateEnergy.label_energy_value.setText(str(self.energy))

            self.Ui.game_layout_allocateEnergy.label_mission1_listed.setText(missionList[0][0]+' '+str(missionList[0][1]))
            if len(missionList)>4:
                self.Ui.game_layout_allocateEnergy.label_mission5_listed.setText(missionList[4][0]+' '+str(missionList[4][1]))
                self.Ui.game_layout_allocateEnergy.pushButton_plus5.show()
                self.Ui.game_layout_allocateEnergy.pushButton_minus5.show()
            else:
                self.Ui.game_layout_allocateEnergy.label_mission5_listed.setText("")
                self.Ui.game_layout_allocateEnergy.pushButton_plus5.hide()
                self.Ui.game_layout_allocateEnergy.pushButton_minus5.hide()
            
            if len(missionList)>3:
                self.Ui.game_layout_allocateEnergy.label_mission4_listed.setText(missionList[3][0]+' '+str(missionList[3][1]))
                self.Ui.game_layout_allocateEnergy.pushButton_plus4.show()
                self.Ui.game_layout_allocateEnergy.pushButton_minus4.show()
            else:
                self.Ui.game_layout_allocateEnergy.label_mission4_listed.setText("")
                self.Ui.game_layout_allocateEnergy.pushButton_plus4.hide()
                self.Ui.game_layout_allocateEnergy.pushButton_minus4.hide()
          
            if len(missionList)>2:
                self.Ui.game_layout_allocateEnergy.label_mission3_listed.setText(missionList[2][0]+' '+str(missionList[2][1]))
                self.Ui.game_layout_allocateEnergy.pushButton_plus3.show()
                self.Ui.game_layout_allocateEnergy.pushButton_minus3.show()
            else:
                self.Ui.game_layout_allocateEnergy.label_mission3_listed.setText("")
                self.Ui.game_layout_allocateEnergy.pushButton_plus3.hide()
                self.Ui.game_layout_allocateEnergy.pushButton_minus3.hide()

            if len(missionList)>1:
                self.Ui.game_layout_allocateEnergy.label_mission2_listed.setText(missionList[1][0]+' '+str(missionList[1][1]))
                self.Ui.game_layout_allocateEnergy.pushButton_plus2.show()
                self.Ui.game_layout_allocateEnergy.pushButton_minus2.show()
            else:
                self.Ui.game_layout_allocateEnergy.label_mission2_listed.setText("")
                self.Ui.game_layout_allocateEnergy.pushButton_plus2.hide()
                self.Ui.game_layout_allocateEnergy.pushButton_minus2.hide()

        refreshMissionList()
        self.pageTuning = pageTuning
        self.modifyEnergy = modifyEnergy
        self.refreshMissionList = refreshMissionList

        def enablePushButton():
            self.Ui.game_layout_allocateEnergy.pushButton_minus1.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus2.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus3.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus4.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_minus5.setEnabled(True)

            self.Ui.game_layout_allocateEnergy.pushButton_plus1.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus2.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus3.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus4.setEnabled(True)
            self.Ui.game_layout_allocateEnergy.pushButton_plus5.setEnabled(True)

        enablePushButton()
        

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
        if self.week==0:
            # 第零周的事件
            self.currentEvent=self.allEvents["secondary_market"]
            return True
        elif self.week==1:
            # 第一周的事件
            self.currentEvent=self.allEvents["lecture_ACM"]
            return True
        # elif self.week==2:
        #     # 第二周的事件
        #     self.currentEvent=self.allEvents["test"]
        #     return True
        # elif self.week==3:
        #     # 第三周的事件
        #     self.currentEvent=self.allEvents["test"]
        #     return True
        else:
            self.currentEvent=self.allEvents["crush_atFirstBlush"]
            return True
        return False

        
    # 刷新事件概率
    def loadEventProbability(self):

        for event in self.allEvents.values():
            self.eventProbablity[event.name]=event.probability
        pass


        
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
            昨晚和室友一起看了部电影，不知不觉就到了深夜。早上匆忙洗漱后，一路小跑到教室，还好最后赶上了早八。
        """,
        """
            今天天气特别好，阳光明媚。早上起来后，我决定去校园里散散步，享受一下早晨的宁静。
        """,
        """
            今天是周五，心情特别好。早上8点的课是大学语文，老师讲了一篇经典的短篇小说，让我受益匪浅。
        """,
        """
            今天早上起床后发现窗外下着小雨，心想这天儿真适合赖床。不过想到还有早八的课，只能硬着头皮爬起来。
        """,
        """
            今天早上起床后突然想起昨晚忘记打卡签到，赶紧打开手机补签。还好系统允许补签，不然平时分没了。
        """,
        """
            刚刚在寝室和室友打了一局游戏，结果输得一塌糊涂。室友太菜了下次不和他一起排位了。
        """,
        """
            刚刚收到了妈妈寄来的补给，好多好多的水果！晚上准备和室友一起分享。
        """,
        """
            刚刚在图书馆复习了一上午，感觉大脑快要爆炸了。中午决定去操场跑几圈，放松一下。
        """
    ]

    @classmethod
    def get_random_talk(cls) -> str:
        choice = random.choice(dialogue.random_talk)
        if len(cls.random_talk) != 1:
            cls.random_talk.remove(choice)
        return choice.lstrip()


    random_talk_terminal=[
        """
            不知不觉怎么就期末了啊，感觉还没过几周呢，怎么就要考试了啊。
        """,
        """
            课就要结束了，感觉自己好像学的还不错，不过这学期的课也太多了，感觉没什么时间复习了啊。
        """,
        """
            考试周真的要到了，这学期的课太多了，真的有点看不完了。
        """,
    ]

    @classmethod
    def get_random_talk_terminal(cls) -> str:
        choice = random.choice(dialogue.random_talk_terminal)
        if len(cls.random_talk_terminal) != 1:
            cls.random_talk_terminal.remove(choice)
        return choice.lstrip()
    


class RandomEvents:
    def __init__(self, game):
        self.game = game
        self.events = []
        self.weight = []
        self.add_random_events()
        

    def add_random_events(self):
        self.events.extend([
            self.RandomEvent("外卖被偷", 0.1, "期待的美食被偷走，心情大受打击，感到非常失落。", mood=-5),
            self.RandomEvent("崴脚", 0.05, "不小心崴到脚，影响了日常活动，身体状况明显下降，去医院看病花费200。", health=-15, money=-200),
            self.RandomEvent("参加志愿活动", 0.2, "参与志愿活动不仅帮助了他人，还结识了志同道合的新朋友。", social=10),
            self.RandomEvent("遇到难以相处的室友", 0.15, "和室友生活习惯不合，造成矛盾，影响了居住环境的舒适度。", social=-10, mood=-5),
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


    def get_random_event(self) -> 'RandomEvent':
        choice = random.choices(self.events, weights=self.weight, k=1)[0]
        index = self.events.index(choice)
        self.weight[index] = 0
        return choice




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
    