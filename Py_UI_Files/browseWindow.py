# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\UC\EPA\SWMM2PEST\SWMM2PEST\UI_Files\browseWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 100)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\EPA1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButtonBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBrowse.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.pushButtonBrowse.setFont(font)
        self.pushButtonBrowse.setDefault(True)
        self.pushButtonBrowse.setObjectName("pushButtonBrowse")
        self.horizontalLayout_2.addWidget(self.pushButtonBrowse)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Open Output File"))
        self.label.setText(_translate("MainWindow", "            Select SWMM Output File:   "))
        self.pushButtonBrowse.setText(_translate("MainWindow", "Browse..."))

