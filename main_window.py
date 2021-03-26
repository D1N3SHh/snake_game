#main window module

#modules
import game

#libraries
import sys, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class main_window(QWidget):

    #runing while creating class object
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ssssnake game")
        self.background()
        self.menu()

    #background animation
    def background(self):
        self.background_layer = QLabel(self)
        self.background_layer.setStyleSheet("background-image: url(assets/background.jpg)")
        self.background_layer.resize(1920, 1080)

    #menu container
    def menu(self):
        #start button
        start_button = QPushButton(self.background_layer)
        start_button.setStyleSheet("background-image: url(assets/start_button.jpg)")
        start_button.setGeometry(480, 550, 960, 100)
        start_button.clicked.connect(self.new_game)

        #quit button
        quit_button = QPushButton(self.background_layer)
        quit_button.setStyleSheet("background-image: url(assets/quit_button.jpg)")
        quit_button.setGeometry(480, 710, 960, 100)
        quit_button.clicked.connect(self.quit_function)

    #starting new game
    def new_game(self):
        game.run()
        
    #quit function
    def quit_function(self):
        sys.exit(0)