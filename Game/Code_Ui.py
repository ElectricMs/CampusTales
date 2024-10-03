import sys
from PySide6 import QtCore, QtGui, QtWidgets, QtQuick
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout, QLabel, QFrame, QHBoxLayout, QSizePolicy
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtGui import QFontMetricsF, QTransform
from PySide6.QtCore import Qt, QRect, QTimer


from Ui_MainMenu import Ui_widget  
from Ui_Game_1 import Ui_Form as Ui_game
from Ui_Interact import Ui_Form as Ui_interact
from Ui_Conversation import Ui_Form as Ui_conversation
import asyncio



class LimitedPlainTextEdit(QPlainTextEdit):
    def __init__(self, max_length):
        super().__init__()
        self.max_length = max_length

    def keyPressEvent(self, event:QtGui.QKeyEvent):
        # if event.key() in (Qt.Key_Escape, Qt.Key_Enter):
        #     if self.parent:
        #         self.parent.send()
        #     return
        if len(self.toPlainText()) >= self.max_length:
            # 如果已经达到最大长度，忽略输入
            return
        super().keyPressEvent(event)



class GameLayout_MainMenu(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



class GameLayout_1(QWidget, Ui_game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



class GameLayout_Interact(QWidget, Ui_interact):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



class GameLayout_Conversation(QWidget, Ui_conversation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scrollArea_layout=QVBoxLayout(self.scrollAreaWidgetContents)
        self.pushButton_Send.clicked.connect(self.send)
        #self.plainTextEdit_Input = LimitedPlainTextEdit(5)
        #self.plainTextEdit_Input.setGeometry(QRect(380, 410, 421, 31))
        #self.plainTextEdit_Input.setPlaceholderText("输入消息")
        

    def loading(self):
        self.plainTextEdit_Input.setEnabled(False)
        self.plainTextEdit_Input.setPlaceholderText("正在建立连接...")
        self.pushButton_Send.setEnabled(False)
        from Agent.talk import Agent
        self.agent=Agent()
        self.add_msg("你好呀",is_me=False)
        self.plainTextEdit_Input.setEnabled(True)
        self.plainTextEdit_Input.setPlaceholderText("开始对话...")
        self.pushButton_Send.setEnabled(True)


    def send(self):
        msg = self.plainTextEdit_Input.toPlainText()
        if msg:
            self.add_msg(msg,is_me=True)
            self.plainTextEdit_Input.clear()
            self.plainTextEdit_Input.setEnabled(False)
            self.plainTextEdit_Input.setPlaceholderText("对方正在输入...")
            self.pushButton_Send.setEnabled(False)

            # 使用 QTimer 来稍作延迟再执行异步任务
            QTimer.singleShot(50, lambda: self.run_async_task(msg))  # 延迟50毫秒


    def run_async_task(self, msg):
        loop = asyncio.new_event_loop()  # 创建新的事件循环
        asyncio.set_event_loop(loop)  # 设置为当前事件循环
        loop.run_until_complete(self.handle_send(msg))  # 运行异步任务
        loop.close()  # 关闭事件循环


    async def handle_send(self, msg):
        answer = await self.agent.talk(msg)
        print(answer)
        self.add_msg(answer, is_me=False)
        print("done")
        self.plainTextEdit_Input.setEnabled(True)
        self.pushButton_Send.setEnabled(True)
        self.plainTextEdit_Input.setPlaceholderText("输入消息")


    def add_msg(self, msg, is_me=False):
        message_label = QLabel(msg)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("background-color: {}; padding: 5px; border-radius: 10px;".format("#DCF8C6" if is_me else "#ECECEC"))
        message_label.setAlignment(Qt.AlignmentFlag.AlignRight if is_me else Qt.AlignmentFlag.AlignLeft)
        message_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        frame = QFrame()
        frame_layout = QHBoxLayout()
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignRight if is_me else Qt.AlignmentFlag.AlignLeft)
        frame_layout.addWidget(message_label)
        frame.setLayout(frame_layout)

        self.scrollArea_layout.addWidget(frame)
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())



class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.game_layout_1 = GameLayout_1()
        self.game_layout_main_menu = GameLayout_MainMenu()
        self.game_layout_interact = GameLayout_Interact()
        self.game_layout_conversation = GameLayout_Conversation()

        self.stacked_layout.addWidget(self.game_layout_main_menu)   # 0
        self.stacked_layout.addWidget(self.game_layout_1)   # 1
        self.stacked_layout.addWidget(self.game_layout_interact)    # 2
        self.stacked_layout.addWidget(self.game_layout_conversation)    # 3

        
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

        self.bind()
        
        # 设置当前显示的布局为主菜单 
        self.current_layout_index = 0
        self.stacked_layout.setCurrentIndex(self.current_layout_index)


    def bind(self):
        self.game_layout_main_menu.startButton.clicked.connect(self.gameStart)
        self.game_layout_main_menu.interactButton.clicked.connect(self.interact)
        self.game_layout_main_menu.optionButton.clicked.connect(self.option)
        self.game_layout_main_menu.exitButton.clicked.connect(self.close)
        self.game_layout_1.radioButton_NO.hide()
        self.game_layout_1.radioButton_Yes.hide()
        self.game_layout_1.pushButton_Next.clicked.connect(self.next)
        self.game_layout_1.pushButton_Back.clicked.connect(self.back)
        self.game_layout_interact.pushButton_Back.clicked.connect(self.back)
        self.game_layout_conversation.pushButton_Back.clicked.connect(self.back)
        self.game_layout_interact.pushButton_PSU.clicked.connect(self.interact_PSU)


    def gameStart(self):
        print("a new game start")
        self.stacked_layout.setCurrentIndex(1)
        from main import Game
        self.game = Game(self)
        self.game_layout_1.label_Text.setText(self.game.start())


    def interact(self):
        self.stacked_layout.setCurrentIndex(2)


    def interact_PSU(self):
        print("interact : PSU")
        self.stacked_layout.setCurrentIndex(3)
        print("loading...")
        QTimer.singleShot(0, self.game_layout_conversation.loading)  # 延迟加载，但是还是没什么用


    def option(self):
        pass


    def next(self):
        self.game.next()


    def back(self):
        self.stacked_layout.setCurrentIndex(0)
        


if __name__ == '__main__':
    app = QApplication([])
    window = MainMenu()
    window.show()
    sys.exit(app.exec())