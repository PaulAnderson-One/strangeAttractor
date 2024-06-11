# Form implementation generated from reading ui file '/Users/paulanderson/projects/python/ml/strange/ui/sim.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 818)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 9, 1071, 801))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWithdrawals = QtWidgets.QTabWidget(parent=self.gridLayoutWidget)
        self.tabWithdrawals.setObjectName("tabWithdrawals")
        self.tabSimulation = QtWidgets.QWidget()
        self.tabSimulation.setObjectName("tabSimulation")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.tabSimulation)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 781, 781))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.simulationGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.simulationGrid.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.simulationGrid.setContentsMargins(0, 0, 0, 0)
        self.simulationGrid.setObjectName("simulationGrid")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.btnRun = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.btnRun.setObjectName("btnRun")
        self.gridLayout_2.addWidget(self.btnRun, 1, 1, 1, 1)
        self.simulationGrid.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.simulationGrid.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.gridLayoutWidget_2)
        self.graphicsView.setObjectName("graphicsView")
        self.simulationGrid.addWidget(self.graphicsView, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=self.gridLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.simulationGrid.addWidget(self.progressBar, 1, 0, 1, 1)
        self.sldAlpha = QtWidgets.QSlider(parent=self.tabSimulation)
        self.sldAlpha.setGeometry(QtCore.QRect(910, 90, 148, 27))
        self.sldAlpha.setMinimum(1)
        self.sldAlpha.setMaximum(101)
        self.sldAlpha.setPageStep(10)
        self.sldAlpha.setProperty("value", 20)
        self.sldAlpha.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sldAlpha.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldAlpha.setObjectName("sldAlpha")
        self.label = QtWidgets.QLabel(parent=self.tabSimulation)
        self.label.setGeometry(QtCore.QRect(790, 90, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sldBeta = QtWidgets.QSlider(parent=self.tabSimulation)
        self.sldBeta.setGeometry(QtCore.QRect(910, 130, 147, 27))
        self.sldBeta.setMinimum(1)
        self.sldBeta.setMaximum(101)
        self.sldBeta.setSingleStep(1)
        self.sldBeta.setPageStep(10)
        self.sldBeta.setProperty("value", 20)
        self.sldBeta.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sldBeta.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldBeta.setObjectName("sldBeta")
        self.label_2 = QtWidgets.QLabel(parent=self.tabSimulation)
        self.label_2.setGeometry(QtCore.QRect(790, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=self.tabSimulation)
        self.label_4.setGeometry(QtCore.QRect(790, 170, 101, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sldGamma = QtWidgets.QSlider(parent=self.tabSimulation)
        self.sldGamma.setGeometry(QtCore.QRect(910, 170, 151, 27))
        self.sldGamma.setMinimum(1)
        self.sldGamma.setMaximum(101)
        self.sldGamma.setPageStep(10)
        self.sldGamma.setProperty("value", 20)
        self.sldGamma.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sldGamma.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldGamma.setObjectName("sldGamma")
        self.label_7 = QtWidgets.QLabel(parent=self.tabSimulation)
        self.label_7.setGeometry(QtCore.QRect(790, 210, 101, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.sldDelta = QtWidgets.QSlider(parent=self.tabSimulation)
        self.sldDelta.setGeometry(QtCore.QRect(910, 210, 151, 27))
        self.sldDelta.setMinimum(1)
        self.sldDelta.setMaximum(101)
        self.sldDelta.setPageStep(10)
        self.sldDelta.setProperty("value", 20)
        self.sldDelta.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sldDelta.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldDelta.setObjectName("sldDelta")
        self.lblPercent = QtWidgets.QLabel(parent=self.tabSimulation)
        self.lblPercent.setGeometry(QtCore.QRect(790, 50, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lblPercent.setFont(font)
        self.lblPercent.setObjectName("lblPercent")
        self.spnNPeriods = QtWidgets.QSpinBox(parent=self.tabSimulation)
        self.spnNPeriods.setGeometry(QtCore.QRect(910, 50, 59, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnNPeriods.sizePolicy().hasHeightForWidth())
        self.spnNPeriods.setSizePolicy(sizePolicy)
        self.spnNPeriods.setMinimum(100)
        self.spnNPeriods.setMaximum(2000)
        self.spnNPeriods.setSingleStep(100)
        self.spnNPeriods.setProperty("value", 200)
        self.spnNPeriods.setObjectName("spnNPeriods")
        self.sldFreq = QtWidgets.QSlider(parent=self.tabSimulation)
        self.sldFreq.setGeometry(QtCore.QRect(910, 250, 151, 27))
        self.sldFreq.setMinimum(1)
        self.sldFreq.setMaximum(101)
        self.sldFreq.setSingleStep(1)
        self.sldFreq.setPageStep(10)
        self.sldFreq.setProperty("value", 20)
        self.sldFreq.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sldFreq.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldFreq.setObjectName("sldFreq")
        self.label_8 = QtWidgets.QLabel(parent=self.tabSimulation)
        self.label_8.setGeometry(QtCore.QRect(790, 250, 101, 24))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tabWithdrawals.addTab(self.tabSimulation, "")
        self.tabTabulation = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabTabulation.sizePolicy().hasHeightForWidth())
        self.tabTabulation.setSizePolicy(sizePolicy)
        self.tabTabulation.setObjectName("tabTabulation")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.tabTabulation)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, -1, 1091, 781))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.tableGrid = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.tableGrid.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.tableGrid.setContentsMargins(0, 0, 0, 0)
        self.tableGrid.setObjectName("tableGrid")
        self.tableView = QtWidgets.QTableView(parent=self.gridLayoutWidget_3)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setGridStyle(QtCore.Qt.PenStyle.DotLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setSortIndicatorShown(True)
        self.tableGrid.addWidget(self.tableView, 0, 0, 1, 1)
        self.tabWithdrawals.addTab(self.tabTabulation, "")
        self.withdrawals = QtWidgets.QWidget()
        self.withdrawals.setObjectName("withdrawals")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.withdrawals)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(-1, -1, 941, 771))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tblWithdrawals = QtWidgets.QTableView(parent=self.gridLayoutWidget_4)
        self.tblWithdrawals.setObjectName("tblWithdrawals")
        self.gridLayout_3.addWidget(self.tblWithdrawals, 0, 0, 1, 1)
        self.tabWithdrawals.addTab(self.withdrawals, "")
        self.gridLayout.addWidget(self.tabWithdrawals, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWithdrawals.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRun.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "alpha"))
        self.label_2.setText(_translate("MainWindow", "beta"))
        self.label_4.setText(_translate("MainWindow", "gamma"))
        self.label_7.setText(_translate("MainWindow", "delta"))
        self.lblPercent.setText(_translate("MainWindow", "nPeriods"))
        self.label_8.setText(_translate("MainWindow", "frequency /s"))
        self.tabWithdrawals.setTabText(self.tabWithdrawals.indexOf(self.tabSimulation), _translate("MainWindow", "simulation"))
        self.tabWithdrawals.setTabText(self.tabWithdrawals.indexOf(self.tabTabulation), _translate("MainWindow", "tabulation 1"))
        self.tabWithdrawals.setTabText(self.tabWithdrawals.indexOf(self.withdrawals), _translate("MainWindow", "withdrawals"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
