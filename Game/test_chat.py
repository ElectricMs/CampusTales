import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QScrollArea, QLabel, QFrame
from PySide6.QtCore import Qt

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('简易聊天界面')
        self.setGeometry(100, 100, 800, 600)

        # 主布局
        main_layout = QVBoxLayout()

        # 消息显示区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_layout = QVBoxLayout(self.scroll_area_content)
        self.scroll_area.setWidget(self.scroll_area_content)
        main_layout.addWidget(self.scroll_area)

        # 输入框和发送按钮
        input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.send_button = QPushButton('发送')
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)
        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

    def send_message(self):
        message = self.message_input.text().strip()
        if message:
            self.add_message(message, is_me=True)
            self.message_input.clear()

    def add_message(self, message, is_me=False):
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("background-color: {}; padding: 5px; border-radius: 10px;".format("#DCF8C6" if is_me else "#ECECEC"))
        message_label.setAlignment(Qt.AlignmentFlag.AlignLeft if is_me else Qt.AlignmentFlag.AlignRight)

        frame = QFrame()
        frame_layout = QHBoxLayout()
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignLeft if is_me else Qt.AlignmentFlag.AlignRight)
        frame_layout.addWidget(message_label)
        frame.setLayout(frame_layout)

        self.scroll_area_layout.addWidget(frame)
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec_())