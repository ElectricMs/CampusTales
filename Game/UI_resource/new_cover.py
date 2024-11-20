import sys
from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QLabel
from PySide6.QtCore import QTimer,QRect,QCoreApplication
from PySide6.QtGui import QPixmap, QImage,QFont
import numpy as np
from os import listdir
import numpy as np
from PIL import Image,ImageQt
import resource.resoure_main_rc


class DynamicBackgroundLabel(QLabel):
    def __init__(self, total_img_pixmap):
        super().__init__()
        
        # 设置初始大小
        self.setFixedSize(1280, 720)
        
        # 图片列表
        self.img_pixmap= total_img_pixmap
        self.current_image_index = 0
        
        # 初始化背景图片
        self.update_background_image()
        
        # 设置定时器，每100毫秒更换一次背景图片
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_background_image)
        

        self.timer.start(100)  # 每隔100毫秒触发
        

    def update_background_image(self):
        # 设置背景图片
        self.setPixmap(self.img_pixmap[self.current_image_index])

        # 时间循环
        if self.current_image_index>=399:
            self.current_image_index=0
            
        else:
            self.current_image_index+=1

class MyWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setFixedSize(1280,720)
        # 设置窗口标题
        self.setWindowTitle("PySide6 示例")
        central_widget=QWidget()
        

        self.image_files = [fn for fn in listdir('Game/UI_resource/') if fn.startswith('img') and fn.endswith('.png')]
        

        
        self.images = [Image.open(f"Game/UI_resource/{fn}").resize((1280, 720)).convert('RGBA') for fn in self.image_files]
        self.alphas = np.linspace(0, 1, 100)
        
        
        total_image=[]
        for im1, im2 in zip(self.images[:-1], self.images[1:]):
        
            for alpha in self.alphas:
                #im1 * (1 - alpha) + im2 * alpha
                image=Image.blend(im1, im2, alpha)
                pixmap = ImageQt.toqpixmap(image)
                total_image.append(pixmap)
        for alpha in self.alphas:
            image=Image.blend(self.images[3],self.images[0],alpha)
            pixmap = ImageQt.toqpixmap(image)
            total_image.append(pixmap)
        # 创建主窗口
        label = DynamicBackgroundLabel(total_image)
       
        label.setParent(central_widget)
        label.setGeometry(0,0,1280,720)

        self.pushButton = QPushButton(central_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 180, 480, 45))
        font = QFont()
        font.setFamilies([u"\u7ad9\u9177\u5c0f\u8587LOGO\u4f53"])
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"\n"
"#pushButton{\n"
"background-color:transparent;\n"
"border:None;\n"
"color:white;\n"
"text-align:left;\n"
"}\n"
"#pushButton:hover{\n"
"border-image:  url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_2 = QPushButton(central_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 270, 480, 45))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"\n"
"#pushButton_2{\n"
"background-color:transparent;\n"
"border:None;\n"
"color:white;\n"
"text-align:left;\n"
"}\n"
"#pushButton_2:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_3 = QPushButton(central_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 360, 480, 45))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"\n"
"#pushButton_3{\n"
"background-color:transparent;\n"
"border:None;\n"
"color:white;\n"
"text-align:left;\n"
"}\n"
"#pushButton_3:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_4 = QPushButton(central_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 450, 480, 45))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"#pushButton_4{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"color:white;\n"
"}\n"
"#pushButton_4:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        self.pushButton_5 = QPushButton(central_widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        
        self.pushButton_5.setGeometry(QRect(0, 540, 480, 45))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"#pushButton_5{\n"
"background-color:transparent;\n"
"border:None;\n"
"text-align:left;\n"
"color:white;\n"
"}\n"
"#pushButton_5:hover{\n"
"border-image: url(:/image/resource/new_button.png);\n"
"color:white;\n"
"text-align:left;\n"
"}")
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"                             \u5f00\u59cb\u6e38\u620f                  ", None))
        # self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"                             \u8bfb\u53d6\u5b58\u6863                  ", None))
        # self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"                             \u6e38\u620f\u8bbe\u7f6e                  ", None))
        # self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"                             \u89d2\u8272\u4ea4\u6d41                  ", None))
        # self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"                             \u9000\u51fa\u6e38\u620f                  ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"                       \u5f00\u59cb\u6e38\u620f           START", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"                       \u8bfb\u53d6\u5b58\u6863           REVIEW", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"                       \u6e38\u620f\u8bbe\u7f6e          CONFIGS", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"                       \u89d2\u8272\u4ea4\u6d41          INTERACT", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"                       \u9000\u51fa\u6e38\u620f              EXIT", None))


        self.setCentralWidget(central_widget)


if __name__=="__main__":
    gender=0
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()






