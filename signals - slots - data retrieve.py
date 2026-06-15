
# sending data

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the default value for the variable
        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Click Me")
        self.button.setCheckable(True)

        self.button.released.connect(self.the_button_was_released)

        # use the default value to set the initial state of the widget
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        # .isChecked returns the check state or the button
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
