import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout
from PySide6.QtGui import QFontMetricsF, QTransform
from PySide6.QtCore import Qt

from Ui_MainMenu import Ui_widget  
from Ui_Game_1 import Ui_Form as Ui_game


class GameLayout_1(QWidget, Ui_game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class GameLayout_MainMenu(QWidget, Ui_widget):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()


        self.stacked_layout = QStackedLayout()
        self.game_layout_1 = GameLayout_1()
        self.game_layout_main_menu = GameLayout_MainMenu()


        self.stacked_layout.addWidget(self.game_layout_main_menu)
        self.stacked_layout.addWidget(self.game_layout_1)
        
        # self.setLayout(self.stacked_layout)
        central_widget = QWidget()
        central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(central_widget)

        #  startButton 在 GameLayout_MainMenu 中，将其连接放在 GameLayout_MainMenu 中
        self.game_layout_main_menu.startButton.clicked.connect(self.gameStart)
        self.game_layout_main_menu.exitButton.clicked.connect(self.close)
        self.game_layout_1.radioButton_NO.hide()
        self.game_layout_1.radioButton_Yes.hide()
        self.game_layout_1.pushButton_Next.clicked.connect(self.next)

        # 设置当前显示的布局为主菜单 
        self.current_layout_index = 0
        self.stacked_layout.setCurrentIndex(self.current_layout_index)



    def gameStart(self):
        print("game start")
        self.stacked_layout.setCurrentIndex(1)
        from main import Game
        self.game = Game(self)
        self.game_layout_1.label_Text.setText(self.game.start())


    def next(self):
        self.game.next()
        

if __name__ == '__main__':
    app = QApplication([])
    window = MainMenu()
    window.show()
    sys.exit(app.exec())