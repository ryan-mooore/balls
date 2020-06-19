# Ryan Moore - AS91986
# 15/06/20
# Bingo Generator
# Version 2.0.0

import sys
from enum import Enum

from PyQt5.QtWidgets import QApplication

from bingo.src.ui.src.main import MainWindow

__version__ = "3.0.0"
__path__ = ""

if __name__ == "__main__":
    # create QApplication
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
