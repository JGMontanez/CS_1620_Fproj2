# logic file
from PyQt6.QtWidgets import *
from gui import *
import os.path
import csv


class Logic(QStackedWidget, Ui_StackedWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.game_setup()

        self.button_start.clicked.connect(lambda: self.go_to_game())
        self.button_back.clicked.connect(lambda: self.go_to_game())

        self.button_reset.clicked.connect(lambda: self.reset_game())
        self.button_stats.clicked.connect(lambda: self.go_to_stats())

    def game_setup(self) -> None:
        """
        method to initialize game parameters
        :return: nothing
        """
        self.turn_num: int = 0
        self.player_symbols: list[str] = ['X', 'O']
        # creating a 2d list of buttons
        self.board: list = [[self.space_1x1, self.space_1x2, self.space_1x3],
                      [self.space_2x1, self.space_2x2, self.space_2x3],
                      [self.space_3x1, self.space_3x2, self.space_3x3]]
        for row in range(3):
            for column in range(3):
                self.board[row][column].clicked.connect(lambda: self.player_turn())

    def go_to_game(self) -> None:
        """
        method to take user to game page
        :return: nothing
        """
        self.setCurrentIndex(1)

    def go_to_stats(self) -> None:
        """
        method to take user to stats page, calls read stats function
        :return: nothing
        """
        self.setCurrentIndex(2)
        self.read_stats()

    def player_turn(self):
        """
        method to execute a player turn,
        :return:
        """
        if self.turn_num % 2 == 0:
            current_player = self.player_symbols[0]
            next_player = self.player_symbols[1]
        else:
            current_player = self.player_symbols[1]
            next_player = self.player_symbols[0]
        self.turn_num +=1
        self.label_turn.setText(f"Player {current_player} turn:")
        # find which button was clicked
        button = self.sender()
        # disable button
        button.setEnabled(False)
        # write in symbols determined by current turn
        button.setText(current_player)

        # determine winner
        if self.find_winner():
            self.label_turn.setText(f'{current_player} wins')
            # disable the rest of buttons
            for spaces in self.board:
                for val in spaces:
                    val.setEnabled(False)
            self.send_to_csv(current_player)
        # if board is full without win, draw
        elif self.turn_num == 9:
            self.label_turn.setText(f'Draw')
        else:
            self.label_turn.setText(f"Player {next_player} turn:")

    def reset_game(self) -> None:
        """
        method to reset game, sets all game parameters to default
        :return: nothing
        """
        self.turn_num = 0
        self.label_turn.setText(f'Player X turn:')
        # enable all board buttons, erase text
        for spaces in self.board:
            for val in spaces:
                val.setText('')
                val.setEnabled(True)

    def find_winner(self) -> bool:
        """
        method to determine if a player wins
        :return: Bool value: True
        """
        # checking rows
        for row in range(3):
            if (self.board[row][0].text() == self.board[row][1].text() == self.board[row][2].text()) \
                    and self.board[row][0].text() != '':
                return True
        # checking columns
        for c in range(3):
            if (self.board[0][c].text() == self.board[1][c].text() == self.board[2][c].text()) \
                    and self.board[0][c].text()  != '':
                return True
        # top left - bttm right diag
        if (self.board[0][0].text() == self.board[1][1].text() == self.board[2][2].text()) \
                and self.board[1][1].text() != "":
            return True
        # bottom left - top right diag
        if (self.board[2][0].text() == self.board[1][1].text() == self.board[0][2].text()) \
                and self.board[1][1].text() != "":
            return True

    def read_stats(self):
        """
        method to read of statistics from 'stats.csv' file
        :return:
        """
        if os.path.isfile('stats.csv'):
            with open('stats.csv', 'r') as data_file:
                reader = csv.reader(data_file)

        # check for stats.csv
        # read if found
        # display "no info found, play some rounds first"

    def send_to_csv(self,result):
        """
        method to write game results to 'stats.csv'
        :param result: game result, 'x' (win), 'o' (win), or 'draw'
        :return:
        """
        games = [0,0,0]
        if result == 'X':
            games[0] +=1
        elif result == 'O':
            games[1] +=1
        else:
            games[2] +=1
        # check for stats.csv
        # update if found
        # create new if not
        if os.path.isfile('stats.csv'):
            with open('stats.csv','r+', newline="") as output_file:
                lines = csv.reader(output_file, delimiter=',')
                #get stats
                #add point to sum
                #write total into place

        else:
            with open('stats.csv', 'w', newline="") as output_file:
                writer = csv.writer(output_file)
                writer.writerow(['X wins', 'O Wins', 'Draws'])
                writer.writerow(games)
