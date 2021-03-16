# Snake game
# Autors: D1N3SHh; dzidek; Naris404

# modules
from main_window import main_window

# libraries
import sys, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# init function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_window()
    window.showFullScreen()
    sys.exit(app.exec())