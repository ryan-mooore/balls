import random
import csv
from os import path
from PyQt5.QtWidgets import QApplication, QDialog
import gui
import sys
from ballgenerator import BallGenerator

def create_balls():
    try:
        ui.textBrowser.clear()

        bg = BallGenerator((1, int(ui.amountOfBallsLineEdit.text())))
        bg.set_codes_path("bingo.csv")

        for ball in bg.generate(int(ui.ballsToPickLineEdit.text())):
            ui.textBrowser.append(ball)
    except ValueError:
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Balls = QDialog()
    ui = gui.Ui_Balls()
    ui.setupUi(Balls)
    ui.pushButton.clicked.connect(create_balls)

    Balls.show()
    sys.exit(app.exec_())