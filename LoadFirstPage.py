from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5 import QtWidgets
import FirstPage
import SecondPage
import ParametersWindow
from subcatchments import Subcatchment
import sys
from readsections import ReadSections


class LoadFirstPage(QMainWindow, FirstPage.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.btnBrowse.clicked.connect(self.openFileDialog)

        self.secondPage = None

        self.window = None

        self.subcatchments_data = []


        # self.show()

    def openFileDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        print str(fname[0][-3:])

        if str(fname[0][-4:]) == ".inp":
            print "Second page"
            self.loadSecondPage(fname[0])

    def loadSecondPage(self, fname):

        self.secondPage = LoadSecondPage()

        # QMainWindow.setCentralWidget(secondPage.centralwidget)

        read_file = ReadSections()

        self.subcatchments_data = read_file.read_subcatchment_data(fname)

        subcatchments_listItems = []

        for i in range(len(self.subcatchments_data)):

            subcatchments_listItems.append(QtWidgets.QListWidgetItem(self.subcatchments_data[i].name))

        print "Between FOr loops"

        print subcatchments_listItems

        for i in range(len(subcatchments_listItems)):

            self.secondPage.listSubcatchments.addItem(subcatchments_listItems[i])

        print "after 2nd for loop"

        # self.secondPage.listSubcatchments.setItemSelected(subcatchments_listItems[0], True)

        print "After Set item selected"

        self.secondPage.listSubcatchments.itemClicked[QtWidgets.QListWidgetItem].connect(self.clickedSlot)

        # self.secondPage.show()

        '''
        self.listWidget_2 = QtWidgets.QListWidget(self.tabSubcatchments)
        self.listWidget_2.setMinimumSize(QtCore.QSize(550, 0))
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        '''

    def clickedSlot(self, item):

        # self.secondPage.formSubcatchmentPars.clear()
        print "Clickedslot"
        print item.text()

        self.loadParametersWindow(item)

        '''
        for subs in self.subcatchments_data:
            if subs.name == item.text():
                print "Subs.area.name: "
                print subs.area.name
                # self.secondPage.formSubcatchmentPars.addRow(subs.area.label, subs.area.edit_field)




                edit_field = QtWidgets.QLineEdit()

                self.secondPage.formSubcatchmentPars.addRow(subs.area.name, edit_field)


                subs.area.label = QtWidgets.QLabel()

                subs.area.edit_field = QtWidgets.QLineEdit()



                self.secondPage.formSubcatchmentPars.setWidget(0, QtWidgets.QFormLayout.LabelRole, subs.area.label)

                self.secondPage.formSubcatchmentPars.setWidget(0, QtWidgets.QFormLayout.FieldRole, subs.area.edit_field)
                # self.secondPage.listWidget_2.addItem(subs.percent_impervious)
                '''

    def createLineEdit(self, item):

        line_edit = QtWidgets.QLineEdit()
        line_edit.setText(item.value)
        line_edit.setReadOnly(True)
        return line_edit

    def loadParametersWindow(self, item):

        self.window = LoadParametersWindow()
        current_sub = Subcatchment()

        for sub in self.subcatchments_data:
            if sub.name == item.text():
                current_sub = sub
                print "Name: " + current_sub.name

        area_line_edit = self.createLineEdit(current_sub.area)

        percent_impervious_line_edit = self.createLineEdit(current_sub.percent_impervious)

        width_line_edit = self.createLineEdit(current_sub.width)

        percent_slope_line_edit = self.createLineEdit(current_sub.percent_slope)

        n_imperv_line_edit = self.createLineEdit(current_sub.n_imperv)

        n_perv_line_edit = self.createLineEdit(current_sub.n_perv)

        storage_depth_imperv_line_edit = self.createLineEdit(current_sub.storage_depth_imperv)

        storage_depth_perv_line_edit = self.createLineEdit(current_sub.storage_depth_perv)

        percent_zero_impervious_line_edit = self.createLineEdit(current_sub.percent_zero_impervious)

        # oneLineEdit1.setObjectName("oneLineEdit1")

        self.window.formLayout.addRow(current_sub.area.name, area_line_edit)

        self.window.formLayout.addRow(current_sub.percent_impervious.name, percent_impervious_line_edit)

        self.window.formLayout.addRow(current_sub.percent_slope.name, percent_slope_line_edit)

        self.window.formLayout.addRow(current_sub.n_imperv.name, n_imperv_line_edit)

        self.window.formLayout.addRow(current_sub.n_perv.name, n_perv_line_edit)

        self.window.formLayout.addRow(current_sub.storage_depth_imperv.name, storage_depth_imperv_line_edit)

        self.window.formLayout.addRow(current_sub.storage_depth_perv.name, storage_depth_perv_line_edit)

        self.window.formLayout.addRow(current_sub.percent_zero_impervious.name, percent_zero_impervious_line_edit)
        # If name = suraj kamble, Job = Google Ceo








        print "One"

        '''
        self.oneLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.oneLabel.setObjectName("oneLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.oneLabel)
        self.oneLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.oneLineEdit.setObjectName("oneLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.oneLineEdit)

        oneLabel1 = QtWidgets.QLabel(self.window.centralwidget)
        oneLabel1.setObjectName("oneLabel1")
        self.window.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, oneLabel1)
        oneLineEdit1 = QtWidgets.QLineEdit(self.window.centralwidget)
        oneLineEdit1.setObjectName("oneLineEdit1")
        self.window.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, oneLineEdit1)
        '''


class LoadSecondPage(QMainWindow, SecondPage.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        print "In second page"
        self.setupUi(self)
        self.show()


class LoadParametersWindow(QMainWindow, ParametersWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        print "In Pars window"
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstPage = LoadFirstPage()
    firstPage.show()
    sys.exit(app.exec_())


