from libs import *
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QWidget

class GameWindow(QWidget):
    def __init__(self, gameName, gameUrl):
        super().__init__()
        self.setWindowTitle(f"Jogo HTML {gameName}")
        self.gameUrl = gameUrl
        
        layout = QVBoxLayout()

        self.setLayout(layout)