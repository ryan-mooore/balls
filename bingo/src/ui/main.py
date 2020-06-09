# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 472)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 243)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(530, 10, 61, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settings.setStyleSheet("color: none;\n"
"border: 0px;")
        self.settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bingo/resources/settings (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon)
        self.settings.setIconSize(QtCore.QSize(32, 32))
        self.settings.setObjectName("settings")
        self.verticalLayout.addWidget(self.settings)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("color: none;\n"
"border: 0px;")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bingo/resources/refresh-ccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 400, 160, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newDraw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.newDraw.setStyleSheet("color: none;\n"
"border: 0px;")
        self.newDraw.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bingo/resources/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newDraw.setIcon(icon2)
        self.newDraw.setIconSize(QtCore.QSize(32, 32))
        self.newDraw.setObjectName("newDraw")
        self.horizontalLayout.addWidget(self.newDraw)
        self.back = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.back.setStyleSheet("color: none;\n"
"border: 0px;")
        self.back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("bingo/resources/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon3)
        self.back.setIconSize(QtCore.QSize(32, 32))
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.forward = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.forward.setStyleSheet("color: none;\n"
"border: 0px;")
        self.forward.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("bingo/resources/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon4)
        self.forward.setIconSize(QtCore.QSize(32, 32))
        self.forward.setObjectName("forward")
        self.horizontalLayout.addWidget(self.forward)
        self.ballView = QtWidgets.QGraphicsView(self.centralwidget)
        self.ballView.setGeometry(QtCore.QRect(140, 130, 256, 192))
        self.ballView.setObjectName("ballView")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 10, 371, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.drawnBalls = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.drawnBalls.setContentsMargins(0, 0, 0, 0)
        self.drawnBalls.setObjectName("drawnBalls")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
