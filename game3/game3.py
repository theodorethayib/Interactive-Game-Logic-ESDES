'''
1. Replace this block comment with a useful description of what this file is

Make the game start by running this file.

2. Python Objectives:
    a. Implement advanced language features of Python (e.g. lambda functions, itertools, generators, maps, decorators, keyword arguments)
    b. Explore unit testing and different project structure options (setup.py, __init__.py, requirements.txt) 
    c. Experiement with more packages (pillow, requests, opencv, gensim, keras, tensorflow, pytorch, scipy, beautitfulsoup, numpy, pandas, matplotlib, textblob, mahotas)

3. Game Objectives:
    a. Code a complex player vs computer game of your choice
    b. You can program whatever you want here but should still be a game with a win condition, a rule-set, and a player making decisions
    c. Does not need to be turn based (eg Pacman)
    d. Computer decision-making involves sophisticated process or external knowledge (eg Chess or Akinator) 
    e. Computer can be imperfect decision-maker, create different levels of difficulty

Focus on learning something new and don't worry about making the game extremely complicated
    
Author:
'''

# import lichess.api
# from lichess.format import PGN, PYCHESS
# import chess
# import chess.svg
# from chessboard import display
#
# from IPython.display import SVG
#
# def main():
#     print('Hello World')
#
#     game = lichess.api.game('zIm5s2zg', format=PYCHESS)
#     print(game.end().board())
#
#     position = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
#
#     while True:
#         display.start(position)
#         display.start(position)
#
#     # board = chess.Board()
#     # board
#
#     # board = chess.Board()
#     # SVG(chess.svg.board(board=board, size=400))
#     # print('Helo')
#
#
# if __name__ == "__main__":
#     main()


import chess
import chess.svg

from PyQt5.QtSvg import QSvgWidget
# from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QFrame
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

class ChessWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 1100, 1100)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)

        grid = QGridLayout()
        self.setLayout(grid)

        # while True:
        self.chessboard = chess.Board()
        # self.chessboard = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
        # var = input('Test')
        # if var == 'q':
        #     break
        print('Hello there')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        # self.layV = QVBoxLayout(central_widget)  # +++
        # self.layV.addWidget(self.chess)  # +++

        # self.setWindowIcon(QIcon('D:/_Qt/img/py-qt.png'))  # web.png
        # self.resize(440, 440)  # (900,900)



    def initUI(self):
        self.setGeometry(100, 100, 1100, 1100)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

        # central_widget = QWidget()
        # self.board1 = ChessWidget(central_widget)
        # self.setCentralWidget(central_widget)

        # self.widgetSvg = QSvgWidget(parent=self)
        # self.widgetSvg.setGeometry(10, 10, 1080, 1080)
        #
        # grid = QGridLayout()
        # self.setLayout(grid)
        #
        # # while True:
        # self.chessboard = chess.Board()
        # # self.chessboard = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
        # self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        # self.widgetSvg.load(self.chessboardSvg)
        # # var = input('Test')
        # # if var == 'q':
        # #     break
        # print('Hello there')

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        # layout.addWidget(ChessWidget(QWidget()), 0, 0)

        layout.addWidget(ChessWidget(), 0, 0)
        # layout.addWidget(QPushButton('2'), 0, 1)
        # layout.addWidget(QPushButton('3'), 0, 2)
        # layout.addWidget(QPushButton('4'), 1, 0)
        # layout.addWidget(QPushButton('5'), 1, 1)
        # layout.addWidget(QPushButton('6'), 1, 2)
        # layout.addWidget(QPushButton('7'), 2, 0)
        # layout.addWidget(QPushButton('8'), 2, 1)
        # layout.addWidget(QPushButton('9'), 2, 2)

        self.horizontalGroupBox.setLayout(layout)

    def updateboard(self, board):
        self.chessboard = board
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

def main():
    go = True
    app = QApplication([])
    # window = MainWindow(chess.Board())
    # window.show()
    # input('Test')
    # window.chessboard = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    # window.show()
    # app.exec()
    window = MainWindow()
    window.show()
    # while go:
    #     app.exec()
    #     var = input('Thing')
    #     if var == 'Q':
    #         go = False
    #
    # window.updateboard(chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4"))
    # window.show()
    app.exec()

    # window.chessboard = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    # window.show()
    # app.exec()

if __name__ == "__main__":
    main()
