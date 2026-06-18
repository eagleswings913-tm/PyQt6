
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        # get the current font, modify it, then apply it back
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        # alignment is specified by using a flag from the Qt.namespace
        widget.setAlignment(
            Qt.AlignmentFlag.AlignHCenter
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
