from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget

# window holds the user-interface of the application
# every application needs one, but can have more
# applications will, by default, exit when the last window is closed

# need one and only one QApplication instance per application
# can pass in sys.argv to allow command line arguments for the app
# QApplication(sys.argv)
app = QApplication([])

# create a Qt widget for the app window
window = QWidget()

# set window title
window.setWindowTitle("My First Window")

# SEARCH pyqt6 QWidget() methods for other possibilities

# set window size
window.resize(500, 500)

# change color, etc. using .setStyleSheet
window.setStyleSheet("background-color: #3498db")

# background-image:

# change color of title bar, harder
# search if you need/want to use this

# set window icon
window.setWindowIcon(QIcon('images/cool.png'))
# windows are hidden by default, .show makes it visible
window.show()

# start the event loop
# handles all user interactions
# event loop will call the appropriate event handles for an event, then control passes back to the event loop
app.exec()

# application will not reach here until you exit and the event loop has stopped
