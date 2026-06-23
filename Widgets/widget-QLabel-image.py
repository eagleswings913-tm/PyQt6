
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel()
        widget.setPixmap(QPixmap("../images/otje.jpg"))

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
