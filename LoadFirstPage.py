from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from Py_UI_Files import FirstPage, SecondPage, ParametersWindow, DialogBox
from subcatchments import Subcatchment, DataField
import sys
from readsections import ReadSections
from write_sections import write_sections


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

        dir = '/Users/surajkamble/Documents/SWMM2PEST'

        print(dir)

        fname = QFileDialog.getOpenFileName(self, 'Select file', dir)
        print(str(fname[0][-3:]))

        if str(fname[0][-4:]) == ".inp":
            print("Second page")
            self.loadSecondPage(fname[0])

    def loadSecondPage(self, fname):

        self.secondPage = LoadSecondPage()

        # QMainWindow.setCentralWidget(secondPage.centralwidget)

        self.read_file = ReadSections()

        all_data = self.read_file.read_subcatchment_data(fname)

        self.subcatchments_data = all_data[0]

        subcatchments_listItems = []

        for i in range(len(self.subcatchments_data)):

            subcatchments_listItems.append(QtWidgets.QListWidgetItem(self.subcatchments_data[i].name))

        print("Between FOr loops")

        print(subcatchments_listItems)

        for i in range(len(subcatchments_listItems)):

            self.secondPage.listSubcatchments.addItem(subcatchments_listItems[i])
            print("Sub for loop")

        print("after 2nd for loop")

        # self.secondPage.listSubcatchments.setItemSelected(subcatchments_listItems[0], True)

        print("After Set item selected")

        self.secondPage.listSubcatchments.itemClicked[QtWidgets.QListWidgetItem].connect(self.clickedSlotSub)

        lid_controls_data = all_data[1]

        self.loadLIDControlsUI(lid_controls_data)


        self.secondPage.buttonOkParameters.clicked.connect(self.replace_subcatchment_data)

        '''
        print("TESTING: ")
        for sub in self.subcatchments_data:
            for val in vars(sub).keys():
                if type(vars(sub)[val]) is DataField:
                    print(vars(sub)[val].label)
                    print(":")
                    print(vars(sub)[val].value)

        print("Blank")

        for val in vars(lid_controls_data):
            if type(vars(lid_controls_data)[val]) is DataField:
                print(vars(lid_controls_data)[val].label)
                print(":")
                print(vars(lid_controls_data)[val].value)
        '''

        # self.secondPage.show()

        '''
        self.listWidget_2 = QtWidgets.QListWidget(self.tabSubcatchments)
        self.listWidget_2.setMinimumSize(QtCore.QSize(550, 0))
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        '''


    def replace_subcatchment_data(self):

        write_sections_data = write_sections(self.subcatchments_data, self.lid_controls_data)

        write_sections_data.write_template_data(self.subcatchments_data)


    def loadLIDControlsUI(self, lid_controls_data):

        self.lid_controls_data = lid_controls_data

        if self.lid_controls_data.has_surface_layer:
            self.secondPage.listLID_Controls.addItem(QtWidgets.QListWidgetItem("Surface"))

        if self.lid_controls_data.has_pavement_layer:
            self.secondPage.listLID_Controls.addItem(QtWidgets.QListWidgetItem("Pavement"))

        if self.lid_controls_data.has_soil_layer:
            self.secondPage.listLID_Controls.addItem(QtWidgets.QListWidgetItem("Soil"))

        if self.lid_controls_data.has_storage_layer:
            self.secondPage.listLID_Controls.addItem(QtWidgets.QListWidgetItem("Storage"))

        if self.lid_controls_data.has_underdrain_system:
            self.secondPage.listLID_Controls.addItem(QtWidgets.QListWidgetItem("Drain"))

        if self.lid_controls_data.has_drainmat_system:
            self.secondPage.listLID_Controls.addItem(QtWidgets.QListWidgetItem("DrainMat"))

        self.secondPage.listLID_Controls.itemClicked[QtWidgets.QListWidgetItem].connect(self.clickedSlotLID_Controls)

    def clickedSlotLID_Controls(self, item):

        self.loadParametersWindow(item, "LID_Controls")


    def clickedSlotSub(self, item):

        # self.secondPage.formSubcatchmentPars.clear()
        print("Clickedslot")
        print(item.text())

        self.loadParametersWindow(item, "Sub")

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

        line_edit = cQLineEdit(self)
        line_edit.setText(item.value)
        line_edit.setReadOnly(True)

        return line_edit

    def printText(self):
        print("Clicked lineEdit")

    def loadDialogBoxWindow(self, parameter):

        self.dialog_box = LoadDialogBoxWindow()

        self.dialog_box.lineEdit_Value.setText(parameter.value)

        print("Lower limit: " + parameter.lower_limit)

        print(parameter.upper_limit)

        if parameter.lower_limit != '':
            self.dialog_box.lineEdit_LowerLimit.setText(parameter.lower_limit)

        if parameter.upper_limit != '':
            self.dialog_box.lineEdit_UpperLimit.setText(parameter.upper_limit)

        
        self.dialog_box.buttonBox.accepted.connect(lambda: self.saveParameterValues(parameter))

        self.dialog_box.buttonBox.rejected.connect(self.hideDialog)

    def hideDialog(self):
        self.dialog_box.hide()


    def saveParameterValues(self, parameter):

        lower_limit = self.dialog_box.lineEdit_LowerLimit.text()

        upper_limit = self.dialog_box.lineEdit_UpperLimit.text()

        if parameter.name in vars(self.current_sub).keys():

            vars(vars(self.current_sub)[parameter.name])['lower_limit'] = lower_limit
            vars(vars(self.current_sub)[parameter.name])['upper_limit'] = upper_limit

        if parameter.name in vars(self.lid_controls_data).keys():

            vars(vars(self.lid_controls_data)[parameter.name])['lower_limit'] = lower_limit
            vars(vars(self.lid_controls_data)[parameter.name])['upper_limit'] = upper_limit


        print(self.current_sub.area.lower_limit)
        print(self.current_sub.area.upper_limit)

        self.dialog_box.hide()

    def loadParametersWindow(self, item, type_of):

        self.window = LoadParametersWindow()
        #self.current_sub = Subcatchment()

        print("TESTING: ")

        print(len(self.subcatchments_data))

        for sub in self.subcatchments_data:
            if sub.name == item.text():
                self.current_sub = sub
                print("Name: " + self.current_sub.name)
                for val in vars(self.current_sub).keys():
                    if type(vars(self.current_sub)[val]) is DataField:
                        print(vars(sub)[val].label)
                        print(":")
                        print(vars(sub)[val].value)


        if type_of == "LID_Controls":

            if item.text() == "Surface":
                surface_layer_storage_depth_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_storage_depth)
                surface_layer_vegetative_cover_fraction_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_vegetative_cover_fraction)
                surface_layer_surface_roughness_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_surface_roughness)
                surface_layer_surface_slope_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_surface_slope)
                surface_layer_swale_side_slope_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_swale_side_slope)

                surface_layer_storage_depth_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_storage_depth))
                surface_layer_vegetative_cover_fraction_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_vegetative_cover_fraction))
                surface_layer_surface_roughness_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_surface_roughness))
                surface_layer_surface_slope_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_surface_slope))
                surface_layer_swale_side_slope_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_swale_side_slope))

                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_storage_depth.label, surface_layer_storage_depth_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_vegetative_cover_fraction.label, surface_layer_vegetative_cover_fraction_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_surface_roughness.label, surface_layer_surface_roughness_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_surface_slope.label, surface_layer_surface_slope_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_swale_side_slope.label, surface_layer_swale_side_slope_line_edit)

        if type_of == "Sub":

            area_line_edit = self.createLineEdit(self.current_sub.area)

            percent_impervious_line_edit = self.createLineEdit(self.current_sub.percent_impervious)

            width_line_edit = self.createLineEdit(self.current_sub.width)

            percent_slope_line_edit = self.createLineEdit(self.current_sub.percent_slope)

            n_imperv_line_edit = self.createLineEdit(self.current_sub.n_imperv)

            n_perv_line_edit = self.createLineEdit(self.current_sub.n_perv)

            storage_depth_imperv_line_edit = self.createLineEdit(self.current_sub.storage_depth_imperv)

            storage_depth_perv_line_edit = self.createLineEdit(self.current_sub.storage_depth_perv)

            percent_zero_impervious_line_edit = self.createLineEdit(self.current_sub.percent_zero_impervious)

            # --------Infiltration---------

            suction_line_edit = self.createLineEdit(self.current_sub.suction)

            hydraulic_conductivity_line_edit = self.createLineEdit(self.current_sub.hydraulic_conductivity)

            initial_moisture_deficit_line_edit = self.createLineEdit(self.current_sub.initial_moisture_deficit)

                                                                                                                                                                                                                                                                          

            # oneLineEdit1.setObjectName("oneLineEdit1")

            area_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.area))
            percent_impervious_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.percent_impervious))
            width_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.width))
            percent_slope_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.percent_slope))
            n_imperv_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.n_imperv))
            n_perv_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.n_perv))
            storage_depth_imperv_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.storage_depth_imperv))
            storage_depth_perv_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.storage_depth_perv))
            percent_zero_impervious_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.percent_zero_impervious))


            self.window.formLayout.addRow(self.current_sub.area.label, area_line_edit)

            self.window.formLayout.addRow(self.current_sub.percent_impervious.label, percent_impervious_line_edit)

            self.window.formLayout.addRow(self.current_sub.width.label, width_line_edit)

            self.window.formLayout.addRow(self.current_sub.percent_slope.label, percent_slope_line_edit)

            self.window.formLayout.addRow(self.current_sub.n_imperv.label, n_imperv_line_edit)

            self.window.formLayout.addRow(self.current_sub.n_perv.label, n_perv_line_edit)

            self.window.formLayout.addRow(self.current_sub.storage_depth_imperv.label, storage_depth_imperv_line_edit)

            self.window.formLayout.addRow(self.current_sub.storage_depth_perv.label, storage_depth_perv_line_edit)

            self.window.formLayout.addRow(self.current_sub.percent_zero_impervious.label, percent_zero_impervious_line_edit)


            # --------LID USAGE------------

            if self.current_sub.control_name != '':
                number_replicate_units_line_edit = self.createLineEdit(self.current_sub.number_replicate_units)

                area_each_unit_line_edit = self.createLineEdit(self.current_sub.area_each_unit)

                top_width_overland_flow_surface_line_edit = self.createLineEdit(self.current_sub.top_width_overland_flow_surface)

                percent_initially_saturated_line_edit = self.createLineEdit(self.current_sub.percent_initially_saturated)

                percent_impervious_area_treated_line_edit = self.createLineEdit(self.current_sub.percent_impervious_area_treated)

                send_outflow_pervious_area_line_edit = self.createLineEdit(self.current_sub.send_outflow_pervious_area)



                number_replicate_units_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.number_replicate_units))

                area_each_unit_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.area_each_unit))

                top_width_overland_flow_surface_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.top_width_overland_flow_surface))

                percent_initially_saturated_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.percent_initially_saturated))

                percent_impervious_area_treated_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.percent_impervious_area_treated))

                send_outflow_pervious_area_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.send_outflow_pervious_area))



                self.window.formLayout.addRow(self.current_sub.number_replicate_units.label, number_replicate_units_line_edit)

                self.window.formLayout.addRow(self.current_sub.area_each_unit.label, area_each_unit_line_edit)

                self.window.formLayout.addRow(self.current_sub.top_width_overland_flow_surface.label, top_width_overland_flow_surface_line_edit)

                self.window.formLayout.addRow(self.current_sub.percent_initially_saturated.label, percent_initially_saturated_line_edit)

                self.window.formLayout.addRow(self.current_sub.percent_impervious_area_treated.label, percent_impervious_area_treated_line_edit)

                self.window.formLayout.addRow(self.current_sub.send_outflow_pervious_area.label, send_outflow_pervious_area_line_edit)


        print("One")

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

        print("In second page")
        self.setupUi(self)
        self.show()


class LoadParametersWindow(QMainWindow, ParametersWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        print("In Pars window")
        self.setupUi(self)
        self.show()


class LoadDialogBoxWindow(QMainWindow, DialogBox.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        print("In Dialog Box window")
        self.setupUi(self)
        self.show()


class cQLineEdit(QtWidgets.QLineEdit):

    clicked = pyqtSignal()

    def __init__(self, widget):
        super().__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstPage = LoadFirstPage()
    firstPage.show()
    sys.exit(app.exec_())


