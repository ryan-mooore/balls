# Ryan Moore - AS91986
# 15/06/20
# Bingo Generator
# Version 2.0.0


import sys
import csv
from enum import Enum

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import \
    QApplication, QDialog, QLabel, QPushButton, QMainWindow
from PyQt5 import QtCore

from ballgenerator import BallGenerator
from ui import main, settings

__version__ = '2.0.0'

codes = "../resources/bingo.csv"
app = QApplication(sys.argv)


class Pixmaps(Enum):
    DRAWN = QPixmap("bingo/resources/drawn.svg")
    CURRENT = QPixmap("bingo/resources/current.svg")
    NOT_DRAWN = QPixmap("bingo/resources/not-drawn.svg")


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = settings.Ui_Balls()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ballName.hide()
        self.ui.ballNumber.hide()
        self.ui.modeText.setText("None")

        self.settings_window = SettingsWindow()
        self._load_settings()
        self.ui.settings_3.clicked.connect(self.settings)
        self.ui.newDraw.clicked.connect(self.new_ball_pool)
        self.ui.forward.clicked.connect(self.next_ball)
        self.ui.back.clicked.connect(self.prev_ball)
        self.ui.recall.clicked.connect(self.recall)

    @QtCore.pyqtSlot()
    def settings(self):
        self.settings_window.exec()
        self._load_settings()

        self.ui.statusBar.showMessage(
            "Settings edited. Changes will apply for next ball pool", 3000
        )

    @QtCore.pyqtSlot()
    def recall(self):
        self.current_ball_index = 0
        self._paint_balls()

    @QtCore.pyqtSlot()
    def new_ball_pool(self):

        self.ui.ballNumber.show()
        self.ui.ballName.show()
        container = self.ui.drawnBallContainer

        # use setParent to delete old widgets
        # (once a widget has no parent it is deleted)
        for index in reversed(range(container.count())):
            container.itemAt(index).widget().setParent(None)

        self.ui.statusBar.showMessage("Generated new ball pool", 2000)

        bg = BallGenerator((self.balls_min, self.balls_max))
        bg.set_codes_path(codes)
        self.this_sample = list(bg.generate(self.balls_sample))

        for ball in self.this_sample:
            icon = QLabel()
            icon.setPixmap(Pixmaps.NOT_DRAWN.value)
            self.ui.drawnBallContainer.addWidget(icon)

        # main_window.ui.drawnBallContainer.addWidget(QSpacerItem())

        self.current_ball_index = 0
        self.drawn_number = 0

        self._paint_balls()

    @QtCore.pyqtSlot()
    def prev_ball(self):
        if self.current_ball_index == 0:
            self.ui.statusBar.showMessage(
                "Already at the first generated ball", 2000
            )
            return

        try:
            self.current_ball_index -= 1
            self._paint_balls()
        except AttributeError:
            self.ui.statusBar.showMessage(
                "Cannot go to previous ball; no ball pool!", 2000
            )

    @QtCore.pyqtSlot()
    def next_ball(self):
        try:
            if self.drawn_number == self.current_ball_index:
                self.drawn_number += 1
            self.current_ball_index += 1
            self._paint_balls()
        except IndexError:
            self.current_ball_index -= 1
            self.drawn_number -= 1
            self.ui.statusBar.showMessage(
                "Already at the last generated ball", 2000
            )
        except AttributeError:
            self.ui.statusBar.showMessage(
                "Cannot go to next ball; no ball pool!", 2000
            )

    def _load_settings(self):
        self.balls_min = int(self.settings_window.ui.range_min.value())
        self.balls_max = int(self.settings_window.ui.range_max.value())
        self.balls_sample = int(self.settings_window.ui.sample.value())

    def _paint_balls(self):
        self.ui.ballNumber.setText(str(
            self.this_sample[self.current_ball_index].value)
        )
        self.ui.ballName.setText(str(
            self.this_sample[self.current_ball_index].code)
        )

        self.ui.statusBar.clearMessage()

        for index in range(self.ui.drawnBallContainer.count()):
            icon = self.ui.drawnBallContainer.itemAt(index).widget()
            if index <= self.drawn_number:
                if index == self.current_ball_index:
                    icon.setPixmap(Pixmaps.CURRENT.value)
                    self.ui.modeText.setText("Current")
                else:
                    icon.setPixmap(Pixmaps.DRAWN.value)
                    self.ui.modeText.setText("Recall")
            else:
                icon.setPixmap(Pixmaps.NOT_DRAWN.value)


if __name__ == "__main__":
    MainWindow = MainWindow()

    # start app
    MainWindow.show()
    sys.exit(app.exec())
