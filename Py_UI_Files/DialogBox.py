# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\UC\EPA\SWMM2PEST\SWMM2PEST\UI_Files\DialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 150)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/EPA1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.checkBox_Fixed = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Fixed.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Fixed.setFont(font)
        self.checkBox_Fixed.setTristate(False)
        self.checkBox_Fixed.setObjectName("checkBox_Fixed")
        self.horizontalLayout_3.addWidget(self.checkBox_Fixed)
        self.checkBox_None = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_None.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_None.setFont(font)
        self.checkBox_None.setObjectName("checkBox_None")
        self.horizontalLayout_3.addWidget(self.checkBox_None)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enter the Range of Parameter"))
        self.lineEdit_UpperLimit.setPlaceholderText(_translate("MainWindow", "Upper Limit"))
        self.checkBox_Fixed.setText(_translate("MainWindow", "Fixed"))
        self.checkBox_None.setText(_translate("MainWindow", "None"))

