#logic file
from PyQt6.QtWidgets import *
from gui import *
import os.path
import csv


# TODO: game screen with 2 player functionality,


# TODO: stats screen that reads data from csv file

class Logic(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_start.clicked.connect(lambda: self.go_to_game())
        self.button_back.clicked.connect(lambda: self.go_to_game())

        self.button_stats.clicked.connect(lambda: self.go_to_stats())

    '''
    create function for
    1. taking user to game page
    
    2. starting/ playing the game
    3. reseting the game
    4. scoring the game
    5. updating stats csv
    
    6. taking user to stats page
    7. reading stats csv
    '''
    def go_to_game(self) -> None:
        """
        method to take user to game page
        :return: nothing
        """
        self.setCurrentIndex(1)
        # call game start function
        self.play_game()

    def go_to_stats(self) -> None:
        """
        method to take user to stats page
        :return: nothing
        """
        self.setCurrentIndex(2)

    def play_game(self):
        """
        method to play game
        :return:
        """
        player1_symbol = "X"
        player2_symbol = "O"
        current_player = player1_symbol
        # games last 9 turns (until spaces are full)
        for turn in range(1,9):
            self.label_turn.setText(f'Player {current_player} turn:')
            self.
        # next button clicked will be marked with current player's symbol

    def reset_game(self):
        """
        method to reset game, available any time
        :return:
        """
        pass

    def score_game(self):
        """
        method to
        :return:
        """