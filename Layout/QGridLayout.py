
from layout_colorwidget import Color

from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        # set spacing around the layout, outside margins
        layout.setContentsMargins(0,0,0,0)
        # # set spacing between elements
        layout.setSpacing(0)
        # layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()