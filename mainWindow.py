from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSizePolicy

# sub-class QMainWIndow to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me")
        button.setStyleSheet("background-color: green")
        # size methods work on any widget
        # button.setFixedSize(400, 300)
        button.setMinimumSize(100, 100)
        button.setMaximumSize(400, 400)
        # button.setFixedWidth()
        # button.setFixedHeight()
        # button.setMaximumWidth()
        # button.setMaximumHeight()

        # set the widget that goes in the middle of the window
        self.setCentralWidget(button)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
