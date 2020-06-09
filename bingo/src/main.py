import random

from os import path
import sys

import csv
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton

from ballgenerator import BallGenerator

from ui import main, settings
from PyQt5.QtGui import QIcon, QPixmap

"""
def create_balls():
    try:
        ui.textBrowser.clear()

        bg = BallGenerator((1, int(ui.amountOfBallsLineEdit.text())))
        bg.set_codes_path("bingo.csv")

        for ball in bg.generate(int(ui.ballsToPickLineEdit.text())):
            ui.textBrowser.append(ball)
    except ValueError:
        pass
"""

balls = BallGenerator((0, 90))

def new_ball_pool():
    print("new ball pool")
    paint_balls(main_window)

def paint_balls(window):
    upcoming_ball = current_ball = past_ball = QLabel()
    upcoming_ball.setPixmap(QPixmap("bingo/resources/circle grey.svg"))
    current_ball.setPixmap(QPixmap("bingo/resources/disc.svg"))
    current_ball.setPixmap(QPixmap("bingo/resources/circle.svg"))

    print(list(balls.generate(5)))

    for index, ball in enumerate(range(5)):
        icon = current_ball
        icon.setObjectName("icon" + str(index))
        window.drawnBalls.addWidget(icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QDialog()
    main_window = main.Ui_MainWindow()
    settings_window = settings.Ui_Settings()

    #settings_window.setupUi(window)
    main_window.setupUi(window)

    main_window.newDraw.clicked.connect(new_ball_pool)
    window.show()
    sys.exit(app.exec())
