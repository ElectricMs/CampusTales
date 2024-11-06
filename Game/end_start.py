from PySide6.QtCore import Qt,QEvent,QTimer
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton
from UI_resource.Ui_end import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
    def set_stream_text(self, text):
        from setting_start import AnimationTimerInterval
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        current_index = 0

        def update_text_stream():
            nonlocal current_index
            if current_index < len(text):
                self.ui.label.setText(text[:current_index + 1])
                current_index += 1
            else:
                self.timer.stop()

        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(update_text_stream)
            self.timer.setInterval(AnimationTimerInterval)
            self.timer.start()  # 每50毫秒更新一次
        else:
            self.timer.stop()
            self.timer = QTimer(self)
            self.timer.timeout.connect(update_text_stream)
            self.timer.setInterval(AnimationTimerInterval)
            self.timer.start()
        
   
if __name__=="__main__":
    app=QApplication([])
    window=MyWindow()
    text="""结局一：

你你你你你你你你你你你你你你你你你你你
啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
噢噢噢噢噢噢噢噢噢噢噢噢噢噢噢噢哦哦哦
钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱钱
"""
    window.set_stream_text(text)
    window.show()
    app.exec()