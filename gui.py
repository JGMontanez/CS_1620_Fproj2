# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(743, 720)
        self.screen_start = QtWidgets.QWidget()
        self.screen_start.setObjectName("screen_start")
        self.button_start = QtWidgets.QPushButton(parent=self.screen_start)
        self.button_start.setGeometry(QtCore.QRect(420, 420, 93, 28))
        self.button_start.setObjectName("button_start")
        self.label_title = QtWidgets.QLabel(parent=self.screen_start)
        self.label_title.setGeometry(QtCore.QRect(440, 140, 271, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label_title.setObjectName("label_title")
        StackedWidget.addWidget(self.screen_start)
        self.screen_game = QtWidgets.QWidget()
        self.screen_game.setObjectName("screen_game")
        self.label_turn = QtWidgets.QLabel(parent=self.screen_game)
        self.label_turn.setGeometry(QtCore.QRect(130, 10, 201, 71))
        self.label_turn.setObjectName("label_turn")
        self.frame_board = QtWidgets.QFrame(parent=self.screen_game)
        self.frame_board.setGeometry(QtCore.QRect(130, 70, 480, 480))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.frame_board.setFont(font)
        self.frame_board.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_board.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_board.setObjectName("frame_board")
        self.space_2x1 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_2x1.setGeometry(QtCore.QRect(10, 165, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.space_2x1.setFont(font)
        self.space_2x1.setText("")
        self.space_2x1.setObjectName("space_2x1")
        self.space_2x2 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_2x2.setGeometry(QtCore.QRect(165, 165, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.space_2x2.setFont(font)
        self.space_2x2.setText("")
        self.space_2x2.setObjectName("space_2x2")
        self.space_2x3 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_2x3.setGeometry(QtCore.QRect(320, 165, 150, 150))
        self.space_2x3.setText("")
        self.space_2x3.setObjectName("space_2x3")
        self.space_1x1 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_1x1.setGeometry(QtCore.QRect(10, 10, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.space_1x1.setFont(font)
        self.space_1x1.setText("")
        self.space_1x1.setObjectName("space_1x1")
        self.space_1x2 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_1x2.setGeometry(QtCore.QRect(165, 10, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.space_1x2.setFont(font)
        self.space_1x2.setText("")
        self.space_1x2.setObjectName("space_1x2")
        self.space_3x1 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_3x1.setGeometry(QtCore.QRect(10, 320, 150, 150))
        self.space_3x1.setText("")
        self.space_3x1.setObjectName("space_3x1")
        self.space_3x2 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_3x2.setGeometry(QtCore.QRect(165, 320, 150, 150))
        self.space_3x2.setText("")
        self.space_3x2.setObjectName("space_3x2")
        self.space_1x3 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_1x3.setGeometry(QtCore.QRect(320, 10, 150, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.space_1x3.setFont(font)
        self.space_1x3.setText("")
        self.space_1x3.setObjectName("space_1x3")
        self.space_3x3 = QtWidgets.QPushButton(parent=self.frame_board)
        self.space_3x3.setGeometry(QtCore.QRect(320, 320, 150, 150))
        self.space_3x3.setText("")
        self.space_3x3.setObjectName("space_3x3")
        self.button_stats = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_stats.setGeometry(QtCore.QRect(520, 590, 93, 28))
        self.button_stats.setObjectName("button_stats")
        self.button_reset = QtWidgets.QPushButton(parent=self.screen_game)
        self.button_reset.setGeometry(QtCore.QRect(60, 630, 93, 28))
        self.button_reset.setObjectName("button_reset")
        StackedWidget.addWidget(self.screen_game)
        self.screen_stats = QtWidgets.QWidget()
        self.screen_stats.setObjectName("screen_stats")
        self.label_stats = QtWidgets.QLabel(parent=self.screen_stats)
        self.label_stats.setGeometry(QtCore.QRect(290, 20, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_stats.setFont(font)
        self.label_stats.setObjectName("label_stats")
        self.button_back = QtWidgets.QPushButton(parent=self.screen_stats)
        self.button_back.setGeometry(QtCore.QRect(90, 520, 93, 28))
        self.button_back.setObjectName("button_back")
        self.frame = QtWidgets.QFrame(parent=self.screen_stats)
        self.frame.setGeometry(QtCore.QRect(180, 140, 431, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_player1_wins = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_player1_wins.setFont(font)
        self.label_player1_wins.setObjectName("label_player1_wins")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_player1_wins)
        self.label_player2_wins = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_player2_wins.setFont(font)
        self.label_player2_wins.setObjectName("label_player2_wins")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_player2_wins)
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_4)
        StackedWidget.addWidget(self.screen_stats)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.button_start.setText(_translate("StackedWidget", "start"))
        self.label_title.setText(_translate("StackedWidget", "tic tac toe"))
        self.label_turn.setText(_translate("StackedWidget", "player 1\'s turn:"))
        self.button_stats.setText(_translate("StackedWidget", "stats"))
        self.button_reset.setText(_translate("StackedWidget", "reset"))
        self.label_stats.setText(_translate("StackedWidget", "stats"))
        self.button_back.setText(_translate("StackedWidget", "back to game"))
        self.label_player1_wins.setText(_translate("StackedWidget", "player 1 [x] wins:"))
        self.label_player2_wins.setText(_translate("StackedWidget", "player 2 = [O] wins:"))
        self.label.setText(_translate("StackedWidget", "Draws:"))
        self.label_2.setText(_translate("StackedWidget", "TextLabel"))
        self.label_3.setText(_translate("StackedWidget", "TextLabel"))
        self.label_4.setText(_translate("StackedWidget", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec())
