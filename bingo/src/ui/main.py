# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bingo/src/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 243)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainContainer = QtWidgets.QHBoxLayout()
        self.mainContainer.setObjectName("mainContainer")
        self.ballInfoContainer = QtWidgets.QVBoxLayout()
        self.ballInfoContainer.setObjectName("ballInfoContainer")
        self.drawnBallContainer = QtWidgets.QHBoxLayout()
        self.drawnBallContainer.setObjectName("drawnBallContainer")
        self.ballInfoContainer.addLayout(self.drawnBallContainer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ballInfoContainer.addItem(spacerItem)
        self.ballGridContainer = QtWidgets.QGridLayout()
        self.ballGridContainer.setObjectName("ballGridContainer")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ballGridContainer.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ballGridContainer.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ballGridContainer.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ballGridContainer.addItem(spacerItem4, 1, 0, 1, 1)
        self.ballFrame = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ballFrame.sizePolicy().hasHeightForWidth())
        self.ballFrame.setSizePolicy(sizePolicy)
        self.ballFrame.setMinimumSize(QtCore.QSize(200, 200))
        self.ballFrame.setStyleSheet("border: 0px solid;\n"
"border-radius: 100px;\n"
"\n"
"background: #55b9f3;")
        self.ballFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ballFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ballFrame.setObjectName("ballFrame")
        self.ballNumber = QtWidgets.QLabel(self.ballFrame)
        self.ballNumber.setGeometry(QtCore.QRect(0, 0, 200, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ballNumber.sizePolicy().hasHeightForWidth())
        self.ballNumber.setSizePolicy(sizePolicy)
        self.ballNumber.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ballNumber.setFont(font)
        self.ballNumber.setStyleSheet("color: white;")
        self.ballNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.ballNumber.setObjectName("ballNumber")
        self.ballGridContainer.addWidget(self.ballFrame, 1, 1, 1, 1)
        self.ballInfoContainer.addLayout(self.ballGridContainer)
        self.mainContainer.addLayout(self.ballInfoContainer)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.back_2 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_2.sizePolicy().hasHeightForWidth())
        self.back_2.setSizePolicy(sizePolicy)
        self.back_2.setStyleSheet("color: none;\n"
"border: 0px;")
        self.back_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bingo/src/ui/../../resources/arrow-left-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_2.setIcon(icon)
        self.back_2.setIconSize(QtCore.QSize(32, 32))
        self.back_2.setObjectName("back_2")
        self.verticalLayout_3.addWidget(self.back_2)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("color: none;\n"
"border: 0px;")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bingo/src/ui/../../resources/refresh-ccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.settings_3 = QtWidgets.QPushButton(self.centralWidget)
        self.settings_3.setStyleSheet("color: none;\n"
"border: 0px;")
        self.settings_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bingo/src/ui/../../resources/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_3.setIcon(icon2)
        self.settings_3.setIconSize(QtCore.QSize(32, 32))
        self.settings_3.setObjectName("settings_3")
        self.verticalLayout_3.addWidget(self.settings_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.mainContainer.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.mainContainer)
        self.bottomButtons = QtWidgets.QHBoxLayout()
        self.bottomButtons.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.bottomButtons.setContentsMargins(10, 10, 10, 10)
        self.bottomButtons.setSpacing(10)
        self.bottomButtons.setObjectName("bottomButtons")
        self.back = QtWidgets.QPushButton(self.centralWidget)
        self.back.setStyleSheet("color: none;\n"
"border: 0px;")
        self.back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("bingo/src/ui/../../resources/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon3)
        self.back.setIconSize(QtCore.QSize(32, 32))
        self.back.setObjectName("back")
        self.bottomButtons.addWidget(self.back)
        self.forward = QtWidgets.QPushButton(self.centralWidget)
        self.forward.setStyleSheet("color: none;\n"
"border: 0px;")
        self.forward.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("bingo/src/ui/../../resources/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward.setIcon(icon4)
        self.forward.setIconSize(QtCore.QSize(32, 32))
        self.forward.setObjectName("forward")
        self.bottomButtons.addWidget(self.forward)
        self.newDraw = QtWidgets.QPushButton(self.centralWidget)
        self.newDraw.setStyleSheet("color: none;\n"
"border: 0px;")
        self.newDraw.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("bingo/src/ui/../../resources/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newDraw.setIcon(icon5)
        self.newDraw.setIconSize(QtCore.QSize(32, 32))
        self.newDraw.setObjectName("newDraw")
        self.bottomButtons.addWidget(self.newDraw)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomButtons.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.bottomButtons)
        #MainWindow.setCentralWidget(self.centralWidget)
        #self.toolBar = QtWidgets.QToolBar(MainWindow)
        #self.toolBar.setObjectName("toolBar")
        #MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ballNumber.setText(_translate("MainWindow", "0"))
        #self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
