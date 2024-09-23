import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout
from PySide6.QtGui import QFontMetricsF, QTransform
from PySide6.QtCore import Qt
from Ui_MainMenu import Ui_widget  

# class CustomButton(QPushButton):
#     def paintEvent(self, event):
#         painter = super().paintEvent(event)
#         painter.save()
#         transform = QTransform.fromScale(1.2, 1.2) if self.underMouse() else QTransform()
#         painter.setWorldTransform(transform)
#         painter.end()

class MainMenu(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)

        # for button in [self.ui.startButton, self.ui.interactButton, self.ui.optionButton, self.ui.exitButton]:
        #     button.setStyleSheet("background-color: transparent;")
        #     # button.setCursor(Qt.PointingHandCursor)
        #     button.setFlat(True)


        self.ui.startButton.click

app = QApplication([])

window = MainMenu()
window.show()

sys.exit(app.exec())