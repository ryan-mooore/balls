import sys
from os import path
from enum import Enum

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import \
    QApplication, QDialog, QLabel, QPushButton, QMainWindow
from PyQt5 import QtCore

from ..generated import settings


# create a class that extends the auto-generated settings window class
class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        # initialise the QDialog class
        super().__init__()

        # extend the class to the auto-generated ui
        self.ui = settings.Ui_Balls()
        self.ui.setupUi(self)
