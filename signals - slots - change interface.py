
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Click Me")

        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Done!")
        self.button.setEnabled(False)
        self.setWindowTitle("My app is done!")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
