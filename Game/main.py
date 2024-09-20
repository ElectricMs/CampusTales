import random
import time

class Game:
    def __init__(self):
        self.createTime=time.time()
        self.reloadTime=time.time()
        self.allEvents=event.get_all_subEvents()
        self.optionalEvents=[]
        self.currentEvent=None
        self.eventProbablity={}
        




        self.loadEventProbability()
        




    def start(self):
        pass

    def reload(self):
        self.reloadTime=time.time()

    def loadRandomEvent(self):
        if self.eventProbablity=={}:
            self.loadEventProbability()
        
        # 获取所有事件的列表和对应的权重列表
        event_keys = list(self.eventProbablity.keys())
        weights = list(self.eventProbablity.values())

        # 使用 random.choices 进行加权随机选择
        # 参数 k 表示抽取的次数，这里我们只抽取一次
        selected_event = random.choices(event_keys, weights=weights, k=1)
        return selected_event[0]


    def loadEvent(self,event):
        pass

    def loadEventProbability(self):
        for event in self.optionalEvents:
            self.eventProbablity[event.name]=event.probability
        pass







if __name__=="__main__":
    pass







class event:
    def __init__(self,name,time,description):
        self.name=name
        self.time=time
        self.description=description
        self.ui=None
        self.setting=None
        self.probability=1

    @classmethod
    def get_all_subEvents(cls):
        subEvents = event.__subclasses__()
        for subEvent in subEvents:
            subEvents.extend(subEvent.get_all_subEvents())
        return subEvents