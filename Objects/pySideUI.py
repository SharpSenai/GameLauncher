from libs import *
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl

class GameWindow(QWidget):
    def __init__(self, gameName, gameUrl):
        super().__init__()
        self.setWindowTitle(f"Jogo HTML {gameName}")
        self.gameUrl = gameUrl

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        file_url = QUrl.fromLocalFile(self.gameUrl.replace('\\', '/'))
        self.browser = QWebEngineView()
        self.browser.setUrl(file_url)
        layout.addWidget(self.browser)
