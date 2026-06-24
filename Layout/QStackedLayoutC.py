
from layout_colorwidget import Color

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        for color in ["red", "green", "yellow", "blue"]:
            tabs.addTab(Color(color),color)

        self.setCentralWidget(tabs)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()