import random
import time

class Game:
    def __init__(self):

        # 存放游戏创建时间
        self.createTime=time.time()

        # 存放游戏重载时间
        self.reloadTime=time.time()

        # 存放所有事件，包括目前的可选事件和不可选事件，格式为 {事件名:事件实例}
        self.allEvents=event.get_all_subEvents()

        # 存放所有可选事件，格式为 {事件名:事件对象}
        self.optionalEvents={}

        # 当前正在进行的事件
        self.currentEvent=None

        # 存放所有可选事件的概率，格式为 {事件名:概率}
        self.eventProbablity={}
        
        # 存放已经完成的事件和时间
        self.completedEvents={}

        # 加载可选事件概率
        self.loadEventProbability()
        
        # 存放已加入主线的事件，格式为 [事件名（字符串）]
        self.mainlineEvents=[]

        # 存放时间点，开始时为第一周
        self.timePoints=1



    # 开始游戏
    def start(self):
        pass


    # 重新加载游戏
    def reload(self):
        self.reloadTime=time.time()


    # 下一个时间点
    def next(self):
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







if __name__=="__main__":
    pass







class event:
    def __init__(self,name,time,description,Game):
        self.name=name
        self.time=time
        self.description=description
        self.ui=None
        self.setting=None
        self.probability=1

    # 获取所有子类
    @classmethod
    def get_all_subEvents(cls):
        subEvents = {}

        # 获取当前类所有的直接子类
        direct_subEvents = event.__subclasses__()

        for subEvent in direct_subEvents:
            # 假设子类的构造函数需要这三个参数
            # 你可以根据实际情况调整这些参数的值
            instance = subEvent("事件名称", 0, "事件描述", Game)
            # 将子类实例的名称和实例存入字典
            subEvents[subEvent.__name__] = instance

            # 递归调用以获取该子类的所有子类，并实例化它们
            subEvents.update(subEvent.get_all_subEvents())
        
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











class dialogue:
    welcoming=[
        "这是我上大学的第一天。天哪，我可不能摆烂",
        "这是我的第一天大学生活，我得好好准备一下",
        "今天是我大学的第一天，我要好好学习",
    ]

    random_talk=[
        """
            今天我7:50才起床，好险，差点赶不上八点的课了。昨天晚上和室友一起熬夜讨论期末项目的事情，没想到一不小心就到了凌晨两点。
            匆匆忙忙地洗漱完，抓起书包就往外跑，还好学校不大，最后还是赶上了。上午的课讲的是数据结构，虽然有点困，但还是努力跟上了老师的节奏。
            下午的课程结束后，我和几个同学去了图书馆准备小组作业，一直忙到天黑。晚饭后，我们又聚在一起打了一局游戏，算是对自己一天辛勤学习的奖励吧。
        """,
        """
            今天天气不错，阳光明媚，适合户外活动。早上没有课，我决定早起去操场跑步，顺便呼吸一下新鲜空气。跑了两圈之后，感觉整个人都精神了许多。
            回来的路上，遇到了几个老同学，我们一起去了学校附近的咖啡馆，边喝咖啡边聊起了最近的生活和学习情况。下午参加了社团组织的户外拓展活动，
            不仅锻炼了身体，还加深了同学们之间的友谊。晚上，大家一起去吃了顿烧烤，大家都玩得很开心。
        """,
        """
            昨晚和室友一起看了部电影，不知不觉就到了深夜。匆忙洗漱后，一路小跑到教室，还好最后赶上了。上午的课程是心理学，老师讲得非常生动有趣，
            让我对这门学科产生了浓厚的兴趣。中午和几个同学在学校食堂吃饭，聊了聊各自的兴趣爱好和未来的打算。下午的课程结束后，我去了图书馆，
            准备下周一的小组报告。晚上和室友一起去了学校的篮球场，打了一场激烈的篮球赛，虽然累得气喘吁吁，但感觉非常畅快。
        """,
        """
            今天天气特别好，阳光明媚。早上起来后，我决定去校园里散散步，享受一下早晨的宁静。走了一圈回来，感觉整个人都精神了许多。
            上午的课程是计算机编程，老师布置了一个新的项目任务，需要我们在一周内完成。中午和室友一起去学校附近的咖啡馆吃了午餐，
            咖啡馆的氛围很轻松，让人感觉很舒服。下午的课程结束后，我和几个同学去了实验室，开始着手准备这个项目。晚上回到宿舍，大家一起看了一部喜剧电影，
            笑得前仰后合，心情非常好。
        """,
        """
            今天是周五，心情特别好。早上8点的课是文学欣赏，老师讲了一篇经典的短篇小说，让我们受益匪浅。中午和几个好朋友去学校附近的一家
            餐厅吃了午餐，点了我们最喜欢的菜。下午的课程结束后，我们去了学校的音乐室，一起弹吉他唱歌，度过了一个愉快的下午。晚上，我们去
            了学校的电影院，看了一部新上映的电影，大家都觉得非常精彩。回到宿舍后，我们聊了很久，直到深夜才入睡。
        """,
    ]