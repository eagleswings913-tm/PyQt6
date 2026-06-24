import sys

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QMainWindow,
    QSpinBox,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()

        self.name = QLineEdit()
        self.age = QSpinBox()
        self.age.setRange(0, 200)
        self.icecream = QComboBox()
        self.icecream.addItems(
            ["Vanilla", "Strawberry", "Chocolate"]
        )

        layout.addRow("Name", self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favorite Icecream", self.icecream)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()