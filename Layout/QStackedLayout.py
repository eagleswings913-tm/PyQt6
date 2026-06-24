
from layout_colorwidget import Color

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(3)

        # set spacing around the layout, outside margins
        # layout.setContentsMargins(0,0,0,0)
        # # set spacing between elements
        # layout.setSpacing(0)
        # layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()