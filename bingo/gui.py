# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Balls(object):
    def setupUi(self, Balls):
        Balls.setObjectName("Balls")
        Balls.resize(400, 299)
        self.buttonBox = QtWidgets.QDialogButtonBox(Balls)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Balls)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.amountOfBallsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.amountOfBallsLabel.setObjectName("amountOfBallsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.amountOfBallsLabel)
        self.amountOfBallsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.amountOfBallsLineEdit.setObjectName("amountOfBallsLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.amountOfBallsLineEdit)
        self.ballsToPickLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ballsToPickLabel.setObjectName("ballsToPickLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ballsToPickLabel)
        self.ballsToPickLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ballsToPickLineEdit.setObjectName("ballsToPickLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ballsToPickLineEdit)
        self.textBrowser = QtWidgets.QTextBrowser(Balls)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 231, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Balls)
        self.pushButton.setGeometry(QtCore.QRect(250, 100, 141, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Balls)
        self.buttonBox.accepted.connect(Balls.accept)
        self.buttonBox.rejected.connect(Balls.reject)
        QtCore.QMetaObject.connectSlotsByName(Balls)

    def retranslateUi(self, Balls):
        _translate = QtCore.QCoreApplication.translate
        Balls.setWindowTitle(_translate("Balls", "Dialog"))
        self.amountOfBallsLabel.setText(_translate("Balls", "Amount of balls"))
        self.amountOfBallsLineEdit.setWhatsThis(_translate("Balls", "<html><head/><body><p>balls</p></body></html>"))
        self.ballsToPickLabel.setText(_translate("Balls", "Balls to pick"))
        self.pushButton.setText(_translate("Balls", "Generate BALLS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Balls = QtWidgets.QDialog()
    ui = Ui_Balls()
    ui.setupUi(Balls)
    Balls.show()
    sys.exit(app.exec_())
