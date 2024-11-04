import sys
from PySide6.QtWidgets import QApplication, QWidget,QLabel,QPushButton
from PySide6.QtGui import QPainter, QColor, QFont, QImage, QFontMetrics,QTransform,QPixmap
from PySide6.QtCore import QTimer, Qt,QRect,QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

import resource.resource3_rc

def insert_newline_every_21_chars(text):
    result = []
    current_length = 0
    if text[-1]=='\n':
        text=text[:-1]
    for char in text:
        
        if char == '\n':
            current_length = 0
        if current_length >= 21 and char != '\n':
            result.append('\n')
            current_length = 0
        result.append(char)
        current_length += 1

    return ''.join(result)
class CustomLabel(QLabel):
    def __init__(self, parent=None,image_path='', image_width=0, image_height=0):
        super().__init__(parent)
        self.setText('')  # 清空默认文本
        self.text_to_draw = ''
        self.image_path = image_path
        self.image_width = image_width  # 图片的目标宽度
        self.image_height = image_height  # 图片的目标高度
        self.current_index = 0  # 当前显示到第几个字符
        self.current_text=''
        self.angle = 0  # 当前旋转角度
        self.flag=True#旋转方向
        self.image = QImage(self.image_path)
        #self.image = QImage(self.image_path).scaled(self.image_width, self.image_height, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateText)
        self.rotate_timer = QTimer(self)
        self.rotate_timer.timeout.connect(self.updateAngle)
       
        self.player = QMediaPlayer()
        
        # 创建音频输出对象
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(0.6)
        # 将媒体播放器与音频输出连接起来
        self.player.setAudioOutput(self.audio_output)

        # 设置要播放的音频文件路径
        audio_file_path = 'Game/Animation/书写.wav'
        self.player.setSource(QUrl.fromLocalFile(audio_file_path))

        # 设置循环播放
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
      
    def start_animate(self):
        from setting_start import TextTimerInterval
        self.timer.setInterval(TextTimerInterval)
        self.rotate_timer.setInterval(TextTimerInterval)
        self.timer.start()
        self.rotate_timer.start()
        self.play_sound()
    def play_sound(self):
        self.player.play()
        
        
    def updateText(self):
        
        self.current_index += 1
        if self.current_index > len(self.text_to_draw):
            self.timer.stop()# 停止定时器
        self.update()  # 触发重绘
    def updateAngle(self):
        if not self.timer.isActive():
            
            self.player.stop()
            self.rotate_timer.stop()
        if self.flag:
            self.angle +=5
        else:
            self.angle-=5
        if self.angle >=0:
            self.flag=False
        
        if self.angle <= -20:
            self.flag=True
        self.update()  # 触发重绘
    def setTextToDraw(self, text):
        new_text=insert_newline_every_21_chars(text)
        self.text_to_draw = new_text
        self.current_text=''
        """更新文本并重置相关状态"""
        self.current_index = 0  # 重置当前显示字符的索引
        self.list = []  # 清空列表
        self.list2=[]
        self.flag = True  # 重置旋转方向
        self.angle = 0  # 重置旋转角度
        self.flag=True#旋转方向
        self.update()  # 触发重绘
        
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 抗锯齿
        painter.setPen(QColor(0, 0, 0))  # 设置画笔颜色为黑色
        font_diaryWidget = QFont()
        font_diaryWidget.setFamilies([u"\u5343\u56fe\u7b14\u950b\u624b\u5199\u4f53"])
        font_diaryWidget.setPointSize(20)
        font_diaryWidget.setBold(True)
        painter.setFont(font_diaryWidget)  # 设置字体为Arial，大小为20
         # 绘制当前索引之前的字符
        current_text = self.text_to_draw[:self.current_index]

      
            
        lines = current_text.split('\n')  # 将文本按照换行符分割成多行
        for i in range(len(lines)):
            self.list2.append(False)

        for i in range(len(lines)):
            self.list.append(False)
        font_metrics = QFontMetrics(painter.font())
        line_height = font_metrics.height()+1

        # 记录上一行的底部位置，用于计算下一行的顶部位置
        last_line_bottom = 0
        
        image_x=0
        image_y=0
         # 创建旋转变换
        transform = QTransform().translate(self.image.width() / 2, self.image.height() / 2).rotate(self.angle).translate(-self.image.width() / 2, -self.image.height() / 2)
        rotated_image = self.image.transformed(transform, Qt.TransformationMode.SmoothTransformation)

        for i, line in enumerate(lines):
            if i!=0:
                self.list[i-1]=True
            # 计算当前行的绘制位置
            text_x = 10  # 文本的x轴起始位置
            text_y = last_line_bottom + line_height  # 每行的y轴位置，基于上一行底部位置加一行的高度
            if not self.image.isNull():
                image_x = text_x + font_metrics.horizontalAdvance(line)  # 图片的x轴位置，基于当前行文本的宽度
                image_y = text_y - 120+ font_metrics.height()  # 图片的y轴位置，在当前行的底部位置
                if self.list[i]:
                    painter.drawImage(2000,image_y,rotated_image)
                elif i==0 or self.list2[i]==True:
                    painter.drawImage(image_x,image_y,rotated_image)
            self.list2[i]=True
            # 更新上一行的底部位置
            painter.drawText(text_x, text_y, line)
            last_line_bottom = text_y
class TypewriterEffectWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        
       
        # 创建一个 QLabel 控件
        self.label_diary_img = QLabel('', self)
        self.label_diary_img.setObjectName(u"label_diary_img")
        self.label_diary_img.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.label_diary_img.setGeometry(QRect(270, 30, 621, 661))
        self.label_diary_img.setStyleSheet(u"#label_diary_img{border-image: url(:/image/resource/Strength_assign/paper2_yellow_l.png);}")

        # 内容
        self.label_diary_content =CustomLabel(self, "屏幕截图_2024-10-23_140034-removebg-preview.png", 184, 166)
        self.label_diary_content.setObjectName(u"label_diary_content")
        self.label_diary_content.setGeometry(QRect(290, 42, 581, 561))




        # self.label_diary_content.setText("Text")
        # 字体 后面要重命名
        font_diaryWidget = QFont()
        font_diaryWidget.setFamilies([u"\u5343\u56fe\u7b14\u950b\u624b\u5199\u4f53"])
        font_diaryWidget.setPointSize(20)
        font_diaryWidget.setBold(True)
        self.label_diary_content.setFont(font_diaryWidget)
        self.label_diary_content.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        # self.widget_diary.label_content.setText(QCoreApplication.translate("strength_assignment", u"\u661f\u671f\u4e00      5\u670828\u65e5     \u6674", None))
        
        self.label_diary_content.setText("")
        text="""你好
哈哈哈

能促
那就
哈哈

哈哈
哈哈

能促
哈"""
        
        self.label_diary_content.setTextToDraw(text)
        self.list=[]
        
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建一个 TypewriterEffectWidget 实例，指定文字、图片路径以及图片的宽度和高度
    
    widget = TypewriterEffectWidget()
    widget.show()
    # new_text = "这是新的文本"
    # widget.setText(new_text)
    #"Hello, PySide6!\nThis is a typewriter effect with scaled image.\nAnd the image follows each line of text."
    sys.exit(app.exec())