#logic file
from PyQt6.QtWidgets import *
from gui import *
import os.path
import csv
# TODO: create start screen, appears before game


# TODO: game screen with 2 player functionality,


# TODO: stats screen that reads data from csv file

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_start.clicked.connect(lambda: self.start())

    def start(self):




