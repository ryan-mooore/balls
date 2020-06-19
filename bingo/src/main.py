# Ryan Moore - AS91986
# 15/06/20
# Bingo Generator
# Version 2.0.0

import sys
from os import path
from enum import Enum

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import \
    QApplication, QDialog, QLabel, QPushButton, QMainWindow
from PyQt5 import QtCore

from ballgenerator import BallGenerator

from ui.src.main import MainWindow
from ui.src.settings import SettingsWindow

__version__ = '2.0.0'




if __name__ == "__main__":
    # path to bingo codes file
    codes = "../resources/bingo.csv"

    # create QApplication
    app = QApplication(sys.argv)

    MainWindow = MainWindow(
        settings_window=SettingsWindow(),
        ball_generator = BallGenerator,
        codes_path=codes
    )

    # show the main window and exec QT
    MainWindow.show()
    sys.exit(app.exec())
