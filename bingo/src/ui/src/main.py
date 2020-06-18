import sys
from os import path
from enum import Enum

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import \
    QApplication, QDialog, QLabel, QPushButton, QMainWindow
from PyQt5 import QtCore

from ..generated import main
from . import settings


# create an enum for the pixmaps for the drawn balls
# status dots (in the top left or the window)
class Pixmaps(Enum):
    def create_pixmap(p):
        return path.normpath(path.join(
            path.dirname(__file__), p
        ))

    DRAWN     = create_pixmap("../../../resources/icons/status-dots/drawn.svg")
    CURRENT   = create_pixmap("../../../resources/icons/status-dots/current.svg")
    NOT_DRAWN = create_pixmap("../../../resources/icons/status-dots/not-drawn.svg")


# class that extends the auto-generated main window class
# this class includes all of its own event slots
class MainWindow(QMainWindow):
    def __init__(self, parent=None, settings_window=None, ball_generator=None, codes_path=None):
        # initialise the QDialog class
        super().__init__()

        # extend the class to the auto-generated ui
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

        # intialise the ui assets - hide the bingo ball and set
        # the mode text to "None"
        self.ui.ballName.hide()
        self.ui.ballNumber.hide()
        self.ui.modeText.setText("None")

        self.BallGenerator = ball_generator
        self.codes_path = codes_path
        self.ball_pool = None

        # bind the settings window to the main window class and
        # load the current settings (the defaults in this case)
        if settings_window:
            self.settings_window = settings_window
            self._load_settings()

        # connect signals to the slot functions
        self.ui.settings_3.clicked.connect(self.settings)
        self.ui.newDraw.clicked.connect(self.new_ball_pool)
        self.ui.forward.clicked.connect(self.next_ball)
        self.ui.back.clicked.connect(self.prev_ball)
        self.ui.recall.clicked.connect(self.recall)
        self.ui.delete_2.clicked.connect(self.delete)

    # delete current ball pool
    @QtCore.pyqtSlot()
    def delete(self):
        self.ui.ballName.hide()
        self.ui.ballNumber.hide()
        self.ui.modeText.setText("None")

        # use setParent to  set to None to delete all old
        # drawn balls status dots
        # (once a widget has no parent it is deleted)

        container = self.ui.drawnBallContainer

        for index in reversed(range(container.count())):
            container.itemAt(index).widget().setParent(None)

        self.ball_pool = None

    # open settings dialog and then save what the user entered
    @QtCore.pyqtSlot()
    def settings(self):
        if self.settings_window.exec():
            self._load_settings()

        self.ui.statusBar.showMessage(
            "Settings edited. Changes will apply for next ball pool", 3000
        )

    # the recall button sets the currently viewed ball to the first one
    @QtCore.pyqtSlot()
    def recall(self):
        self.current_ball_index = 0
        self._paint_balls()

    # crate a new ball pool with the saved settings
    @QtCore.pyqtSlot()
    def new_ball_pool(self):
        container = self.ui.drawnBallContainer

        # use setParent to  set to None to delete all old
        # drawn balls status dots
        # (once a widget has no parent it is deleted)
        for index in reversed(range(container.count())):
            container.itemAt(index).widget().setParent(None)

        # create new ball generator class
        bg = self.BallGenerator((self.balls_min, self.balls_max))
        bg.set_codes_path(self.codes_path)

        # create sample generator using settings values
        try:
            self.ball_pool = list(bg.generate(self.balls_sample))
        except ValueError:
            self.ui.statusBar.showMessage("Incorrect values in settings!", 2000)
            self.ui.ballName.hide()
            self.ui.ballNumber.hide()
            return
        else:
            self.ui.statusBar.showMessage("Generated new ball pool", 2000)

        # iterate through the sample and create new status dots
        # for each ball, assigning the not drawn (grey) pixmap
        for ball in self.ball_pool:
            status_dot = QLabel()
            status_dot.setPixmap(QPixmap(Pixmaps.NOT_DRAWN.value))
            self.ui.drawnBallContainer.addWidget(status_dot)

        # set the current view index and
        # the current latest drawn ball to 0
        self.current_ball_index = 0
        self.drawn_number = 0

        # show the neccesary ui assets
        self.ui.ballNumber.show()
        if self.use_codes:
            self.ui.ballName.show()
        else:
            self.ui.ballName.hide()

        # finally, render the current ball and the status dots
        self._paint_balls()

    # previous ball button is pressed
    @QtCore.pyqtSlot()
    def prev_ball(self):
        # test for ball pool not existing
        if self.ball_pool:
            # test for the first ball already
            if self.current_ball_index > 0:
                # go to previous ball
                self.current_ball_index -= 1
                self._paint_balls()
            else:
                self.ui.statusBar.showMessage(
                    "Already at the first generated ball", 2000
                )
        else:
            self.ui.statusBar.showMessage(
                "Cannot go to previous ball; no ball pool!", 2000
            )

    # next ball button is pressed
    # if you're reading this, this bit of code is bad i know
    @QtCore.pyqtSlot()
    def next_ball(self):
        if self.ball_pool:
            if self.current_ball_index < len(self.ball_pool) - 1:
                # if current view is on the latest ball drawn
                # increase ball drawn as well as currint view
                if self.drawn_number == self.current_ball_index:
                    self.drawn_number += 1

                # update current view and render
                self.current_ball_index += 1
                self._paint_balls()

            else:
                self.ui.statusBar.showMessage(
                    "Already at the last generated ball", 2000
                )

        # test for ball pool not existing
        else:
            self.ui.statusBar.showMessage(
                "Cannot go to next ball; no ball pool!", 2000
            )

    # grab values from settings fields and assign to class attributes
    def _load_settings(self):
        self.balls_min    = int(self.settings_window.ui.range_min.value())
        self.balls_max    = int(self.settings_window.ui.range_max.value())
        self.balls_sample = int(self.settings_window.ui.sample.value())
        self.use_codes        = self.settings_window.ui.checkBox.isChecked()

    # the render function - updates the main ball view
    # and the status dots
    def _paint_balls(self):
        # set ball number and code name to current draw
        self.ui.ballNumber.setText(str(
            self.ball_pool[self.current_ball_index].value)
        )
        self.ui.ballName.setText(str(
            self.ball_pool[self.current_ball_index].code)
        )

        # iterate through every status dot
        for index in range(self.ui.drawnBallContainer.count()):
            status_dot = self.ui.drawnBallContainer.itemAt(index).widget()
            # if the dot represents a ball that has been drawn...
            if index <= self.drawn_number:
                # if it is equal to the current user view, set to
                # 'current' icon design and set mode to current
                if index == self.current_ball_index:
                    status_dot.setPixmap(QPixmap(Pixmaps.CURRENT.value))
                    self.ui.modeText.setText("Current")
                # else set to 'recall'
                # icon design and set mode to recall
                else:
                    status_dot.setPixmap(QPixmap(Pixmaps.DRAWN.value))
                    self.ui.modeText.setText("Recall")
            # ret to not trawn (grey) icon
            else:
                status_dot.setPixmap(QPixmap(Pixmaps.NOT_DRAWN.value))
