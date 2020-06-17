# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Balls(object):
    def setupUi(self, Balls):
        Balls.setObjectName("Balls")
        Balls.resize(241, 193)
        Balls.setStyleSheet("background-color: white")
        self.verticalLayoutWidget = QtWidgets.QWidget(Balls)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 220, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.range_max = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.range_max.setWrapping(False)
        self.range_max.setMinimum(1)
        self.range_max.setMaximum(90)
        self.range_max.setProperty("value", 90)
        self.range_max.setObjectName("range_max")
        self.gridLayout.addWidget(self.range_max, 1, 1, 1, 1)
        self.range_min = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.range_min.setMinimum(1)
        self.range_min.setObjectName("range_min")
        self.gridLayout.addWidget(self.range_min, 1, 0, 1, 1)
        self.amountOfBallsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amountOfBallsLabel.setFont(font)
        self.amountOfBallsLabel.setScaledContents(False)
        self.amountOfBallsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.amountOfBallsLabel.setObjectName("amountOfBallsLabel")
        self.gridLayout.addWidget(self.amountOfBallsLabel, 0, 0, 1, 1)
        self.ballsToPickLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ballsToPickLabel.setFont(font)
        self.ballsToPickLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ballsToPickLabel.setObjectName("ballsToPickLabel")
        self.gridLayout.addWidget(self.ballsToPickLabel, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sample = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.sample.setMinimum(1)
        self.sample.setMaximum(90)
        self.sample.setProperty("value", 8)
        self.sample.setObjectName("sample")
        self.horizontalLayout.addWidget(self.sample)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Balls)
        self.buttonBox.accepted.connect(Balls.accept)
        self.buttonBox.rejected.connect(Balls.reject)
        QtCore.QMetaObject.connectSlotsByName(Balls)
        Balls.setTabOrder(self.range_min, self.range_max)
        Balls.setTabOrder(self.range_max, self.sample)
        Balls.setTabOrder(self.sample, self.checkBox)

    def retranslateUi(self, Balls):
        _translate = QtCore.QCoreApplication.translate
        Balls.setWindowTitle(_translate("Balls", "Settings"))
        self.amountOfBallsLabel.setText(_translate("Balls", "Lower limit"))
        self.ballsToPickLabel.setText(_translate("Balls", "Upper limit"))
        self.label_2.setText(_translate("Balls", "Select"))
        self.label_3.setText(_translate("Balls", "Balls"))
        self.checkBox.setText(_translate("Balls", "Use bingo codes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Balls = QtWidgets.QDialog()
    ui = Ui_Balls()
    ui.setupUi(Balls)
    Balls.show()
    sys.exit(app.exec_())
