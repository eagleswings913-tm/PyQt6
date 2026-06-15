

# Signals - are notifications emitted by widgets when something happens - ie button push, text change in input box
# Signals can also send data to provide additional information about what happened
# ****** programmer can create their own custom signals

# Slots - the signal receivers
# Any function or method can be a receiver
# Some Qt Widgets have their own built-in slots - you can hook Qt widgets together directly

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Click Me")

        # signal = button clicked -------- Slot = the_button_was_clicked
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    # slot to receive the button clicked signal
    def the_button_was_clicked(self):
        print("Clicked!")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
