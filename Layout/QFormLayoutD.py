
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QSpinBox,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Application")

        layout = QFormLayout()

        self.data = {"name": "Nobody", "age": 18, "favorite_icecream": ""}
        print(self.data)

        self.name = QLineEdit()
        self.name.setPlaceholderText(self.data["name"])
        self.name.textChanged.connect(self.handle_name_changed)
        self.age = QSpinBox()
        self.age.setRange(0, 200)
        self.age.setValue(self.data["age"])
        self.age.valueChanged.connect(self.handle_age_changed)
        self.icecream = QComboBox()
        self.icecream.addItems(
            ["Vanilla", "Strawberry", "Chocolate"]
        )
        self.icecream.setCurrentIndex(-1)
        self.icecream.currentTextChanged.connect(self.handle_icecream_changed)

        layout.addRow("Name", self.name)
        layout.addRow("Age", self.age)
        layout.addRow("Favorite Icecream", self.icecream)

        # Empty label to show error messages
        self.error = QLabel()
        layout.addWidget(self.error)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def handle_name_changed(self, name):
        self.data["name"] = name
        print(self.data)
        self.validate()
        # print(name)

    def handle_age_changed(self, age):
        self.data["age"] = age
        print(self.data)
        self.validate()
        # print(age)

    def handle_icecream_changed(self, icecream):
        self.data["favorite_icecream"] = icecream
        print(self.data)
        self.validate()
        # print(icecream)

    def validate(self):
        if self.data["age"] > 10 and self.data["favorite_icecream"] == "Chocolate":
            self.error.setText("People over 10 aren't allowed chocolate icecream")
            return
        if self.data["age"] > 100:
            self.error.setText("Did you send a telegram?")
            return
        self.error.setText("")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()