
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget
)

# most Qt widgets have slots available, which you can connect any signal that emits the same type that is accepts
# widget documentation had s the slots for each widget listed under "Public Slots"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        # connect the input to the label
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        # 2 widgets added to the layout
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        # layout added to the window
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()

