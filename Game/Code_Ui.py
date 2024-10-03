import sys
from PySide6 import QtCore, QtGui, QtWidgets, QtQuick
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout, QLabel, QFrame, QHBoxLayout, QSizePolicy
from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtGui import QFontMetricsF, QTransform,QFont
from PySide6.QtCore import Qt, QRect
import math

from Ui_MainMenu import Ui_widget
from Ui_Game_1 import Ui_Form as Ui_game
from Ui_Interact import Ui_Form as Ui_interact
from Ui_Conversation import Ui_Form as Ui_conversation



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
        self.scrollArea_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrollArea_layout.setSpacing(10)
        self.pushButton_Send.clicked.connect(self.send)
        #self.plainTextEdit_Input = LimitedPlainTextEdit(5)
        #self.plainTextEdit_Input.setGeometry(QRect(380, 410, 421, 31))
        #self.plainTextEdit_Input.setPlaceholderText("输入消息")

        self.add_msg("你好呀",is_me=False)


    def send(self):
        msg = self.plainTextEdit_Input.toPlainText()
        if msg:
            self.add_msg(msg,is_me=True)
            self.plainTextEdit_Input.clear()


    def add_msg(self, msg, is_me=False):

        def compute_height(msg):
            # newline_count = msg.count('\n')
            # n=1+newline_count
            n=1
            num=0
            for char in msg:
                if char != '\n':
                    num += 1
                    if num == 12:
                        n+=1
                        num=1
                else:
                    num = 0
                    n+=1
            return n
        def compute_width(msg):
            if '\n' in msg:
                max=0
                n=0
                for char in msg:
                    if char != '\n':
                        n+=1
                        if n>max:
                            max=n
                    else:
                        n=0
                return max
            else:
                return len(msg)


        max_width=compute_width(msg)
        height =compute_height(msg)
        if max_width >=11:
            should_width=160
        else:
            should_width=14*max_width+13
        #message_label为消息文本内容
        message_label = QLabel(msg)
        message_label.setWordWrap(True)
        message_label.setFixedWidth(should_width)
        font = QFont('微软雅黑', 10)
        message_label.setFont(font)
        message_label.setStyleSheet("background-color: {}; padding: 5px; border-radius: 10px;".format("#DCF8C6" if is_me else "#ECECEC"))
        message_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        message_label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        message_label.setMaximumHeight(33*height)

        #frame为气泡
        frame = QFrame()
        frame_layout = QHBoxLayout()


        # frame.setStyleSheet("background-color: red;")
        frame_layout.setAlignment( Qt.AlignmentFlag.AlignRight if is_me else Qt.AlignmentFlag.AlignLeft)
        frame_layout.addWidget(message_label)
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame.setLayout(frame_layout)
         # 设置 QFrame 的大小策略
        frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

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
