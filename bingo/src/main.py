import sys
import csv
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton
from enum import Enum

from ballgenerator import BallGenerator

from ui import main, settings
from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore.Qt import WA_DeleteOnClose

codes = "../resources/bingo.csv"

app = QApplication(sys.argv)


class Pixmaps(Enum):
    PAST = QPixmap("bingo/resources/disc.svg")
    CURRENT = QPixmap("bingo/resources/circle.svg")
    FUTURE = QPixmap("bingo/resources/circle grey.svg")


def new_ball_pool():

    bg = BallGenerator((int(settings_window.ui.range_min.value()), int(settings_window.ui.range_max.value())))
    bg.set_codes_path(codes)
    main_window.this_sample = list(bg.generate(int(settings_window.ui.sample.value())))

    for index, ball in enumerate(main_window.this_sample):
        icon = QLabel(str(index))
        icon.setPixmap(Pixmaps.FUTURE.value)
        main_window.ui.drawnBallContainer.addWidget(icon)

    main_window.current_ball_index = 0
    paint_balls()


def paint_balls():

    main_window.ui.ballNumber.setText(str(main_window.this_sample[main_window.current_ball_index].value))

    for index in range(main_window.ui.drawnBallContainer.count()):
        icon = main_window.ui.drawnBallContainer.itemAt(index).widget()
        if index < main_window.current_ball_index:
            icon.setPixmap(Pixmaps.PAST.value)
        elif index == main_window.current_ball_index:
            icon.setPixmap(Pixmaps.CURRENT.value)
        else:
            icon.setPixmap(Pixmaps.FUTURE.value)



def next_ball():
    main_window.current_ball_index += 1
    paint_balls()

def prev_ball():
    main_window.current_ball_index -= 1
    paint_balls()


if __name__ == "__main__":

    bggenerator = None



    # main window setup
    main_window = QDialog()
    main_window.ui = main.Ui_MainWindow()
    main_window.ui.setupUi(main_window)

    # settings window setup
    settings_window = QDialog()
    settings_window.ui = settings.Ui_Balls()
    settings_window.ui.setupUi(settings_window)

    # signal slots
    main_window.ui.settings_3.clicked.connect(settings_window.exec)
    main_window.ui.newDraw.clicked.connect(new_ball_pool)
    main_window.ui.forward.clicked.connect(next_ball)
    main_window.ui.back.clicked.connect(prev_ball)

    # start app
    main_window.show()
    sys.exit(app.exec())
