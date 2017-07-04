# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 409)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\EPA1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textHelp = QtWidgets.QTextBrowser(self.centralwidget)
        self.textHelp.setObjectName("textHelp")
        self.horizontalLayout.addWidget(self.textHelp)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help"))
        self.textHelp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">Open SWMM2PEST.exe file to run the application. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt; font-weight:600;\">Prerequisites</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Add PEST to path in environmental variables. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Add SWMM to path in environmental variables. SWMM2PEST is not compatible with the latest version of SWMM i.e., 5.1.012 because of some issues. Please use the previous version of SWMM or use SWMM5110_test.exe provided with SWMM2PEST. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt; font-weight:600;\">Parameter Data Section</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Provide SWMM input file (.inp). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Make sure the output file name mentioned in the input file represents the output file location. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><img src=\"file:///C:\\Users\\Suraj\\AppData\\Local\\Temp\\msohtmlclip1\\01\\clip_image002.jpg\" width=\"624\" height=\"101\" /><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Click on the subcatchment/LID name to display the parameter and their values. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Click on the parameter value label that you want to select for estimation. A dialog box will be displayed. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">5.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Enter the lower and upper bound for the selected parameter. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">6.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">After finishing click “Ok”. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt; font-weight:600;\">Observation Data Section</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Provide SWMM output file (.txt). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Select the output parameter for PEST to calibrate against i.e., the output parameter for which you have the measured or field values. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt; font-weight:600;\">Control Data Section</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">Provide the file containing measured or field values for the selected output parameter. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:8pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">       </span><span style=\" font-size:8pt;\">The field values’ time stamp must begin with start time of the output file. </span></p></body></html>"))

