
# sending data

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Click Me")
        button.setCheckable(True)
        # signal = button clicked -------- Slot = the_button_was_clicked
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    # slot to receive the button clicked signal
    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, is_checked):
        print("Checked?: ", is_checked)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
