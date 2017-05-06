# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/surajkamble/Documents/SWMM2PEST/DialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_LowerLimit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_LowerLimit.setText("")
        self.lineEdit_LowerLimit.setPlaceholderText("Lower Limit")
        self.lineEdit_LowerLimit.setObjectName("lineEdit_LowerLimit")
        self.horizontalLayout_2.addWidget(self.lineEdit_LowerLimit)
        self.lineEdit_Value = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Value.setObjectName("lineEdit_Value")
        self.horizontalLayout_2.addWidget(self.lineEdit_Value)
        self.lineEdit_UpperLimit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_UpperLimit.setText("")
        self.lineEdit_UpperLimit.setObjectName("lineEdit_UpperLimit")
        self.horizontalLayout_2.addWidget(self.lineEdit_UpperLimit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_UpperLimit.setPlaceholderText(_translate("MainWindow", "Upper Limit"))

