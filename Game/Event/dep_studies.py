from. import event as Event
from main import Game

class event_studies(Event.event):
    def __init__(self, Game:Game):
        super().__init__(name="学业", description="主线中最初就有的学业部分", Game=Game)
        self.probability=0


    def if_join(self):
        pass


    def event_start(self):
        pass


    def event_end(self):
        pass


    def refreshProbability(self):
        pass


    def affection(self,*args):
        pass



# from deprecated import deprecated

# @deprecated(reason="Use new_function instead", version='1.2.0')
# def old_function():
#     print("This is an old function.")

# def new_function():
#     print("This is a new function.")

# # 调用旧函数
# old_function()  # 会发出 DeprecationWarning

# # 调用新函数
# new_function()  # 不会发出警告