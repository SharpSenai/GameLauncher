from libs import *
from Objects.gamehandler import gameHandler
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    game = gameHandler()
    game.loadGame()
    app.exec()
