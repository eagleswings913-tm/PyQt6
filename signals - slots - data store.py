
# sending data

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the default value for the variable
        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Click Me")
        button.setCheckable(True)

        button.clicked.connect(self.the_button_was_toggled)
        # use the default value to set the initial state of the widget
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, is_checked):
        # when the state changes, update the variable
        self.button_is_checked = is_checked
        print(self.button_is_checked)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
