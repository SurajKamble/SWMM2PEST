import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, qApp)

# from Py_UI_Files import *  # FirstPage, SecondPage, ParametersWindow, DialogBox, browseWindow, PESTOutputWindow

from Core.readsections import ReadSections
from Py_UI_Files import FirstPage, DialogBox, browseWindow, PESTOutputWindow, SecondPage, ParametersWindow, HelpWindow
from Core.write_sections import write_sections
from Core.subcatchments import DataField
import os
'''
from .subcatchments import DataField
from .readsections import ReadSections
from .write_sections import write_sections
'''
from numpy import linspace

import pyqtgraph as pg


# Separate thread that calls pest and runs it in the background
class PestThread(QThread):

    def __init__(self, pst_fname):
        QThread.__init__(self)

        self.pst_fname = pst_fname

    def __del__(self):
        self.wait()

    def run_pest_command(self, pst_fname):

        print("In run thread")
        cmd_line = "pest " + pst_fname

        # self.running_PEST = LoadRunningPESTWindow()

        # self.running_PEST.labelPESTOuput.setText("Running...")

        print(cmd_line)

        os.system(cmd_line)


        #self.output = os.popen(cmd_line).readlines()
        # print(self.output)
        #self.output = re.sub("\x08.", "", ''.join(self.output))
        # print(self.output)

        # return self.output


    def run(self):

        self.run_pest_command(self.pst_fname)

        # return output


# Run PEST and check if PEST ran successfully or not.
# If yes, display a graph for Measured values Vs. Output values before calibration Vs. Output values after calibration.
# Get the output values before calibration from the .txt before running PEST and get the output values after calibration
# from the .txt after running PEST.


# This class contains all the functionalities required for the UI

class LoadFirstPage(QMainWindow, FirstPage.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.btnBrowse.clicked.connect(self.openFileDialog)

        self.secondPage = None

        self.window = None

        self.subcatchments_data = []

        self.current_sub = None

    # First window prompting to provide SWMM input file

    def openFileDialog(self):


        dir = '/Users/surajkamble/Documents/SWMM2PEST'

        # print(dir)

        fname = QFileDialog.getOpenFileName(self, 'Select input file', dir)
        # print(str(fname[0][-3:]))


        self.inp_fname = fname[0]

        if str(fname[0][-4:]) == ".inp":
            # print("Second page")
            self.loadSecondPage(fname[0])

    def loadHelpWindow(self):

        self.helpWindow = LoadHelpWindow()


    # Loads second window after getting SWMM input file

    def loadSecondPage(self, fname):

        self.secondPage = LoadSecondPage()

        self.secondPage.actionExit.triggered.connect(qApp.quit)

        self.secondPage.actionHelp.triggered.connect(self.loadHelpWindow)

        # pg.plot([1, 2, 3])

        # QMainWindow.setCentralWidget(secondPage.centralwidget)


        # self.secondPage.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # self.secondPage.pushButtonRunPEST.clicked.connect(self.run_pest)


        self.read_file = ReadSections()

        all_data = self.read_file.read_subcatchment_data(fname)

        self.subcatchments_data = all_data[0]

        subcatchments_listItems = []

        for i in range(len(self.subcatchments_data)):

            subcatchments_listItems.append(QtWidgets.QListWidgetItem(self.subcatchments_data[i].name))

        # print("Between FOr loops")

        # print(subcatchments_listItems)

        for i in range(len(subcatchments_listItems)):

            self.secondPage.listSubcatchments.addItem(subcatchments_listItems[i])
            # print("Sub for loop")

        # print("after 2nd for loop")

        # self.secondPage.listSubcatchments.setItemSelected(subcatchments_listItems[0], True)

        # print("After Set item selected")

        self.secondPage.listSubcatchments.itemClicked[QtWidgets.QListWidgetItem].connect(self.clickedSlotSub)

        lid_controls_data = all_data[1]

        self.loadLIDControlsUI(lid_controls_data)
        self.hide()


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

        self.secondPage.tabOuter.setCurrentIndex(1)

        self.browseOutFileWindow = LoadBrowseWindow()

        self.browseOutFileWindow.pushButtonBrowse.clicked.connect(self.outputFileDialog)

    # Provide SWMM output file

    def outputFileDialog(self):

        dir = '/Users/surajkamble/Documents/SWMM2PEST'

        print(dir)

        out_fname = QFileDialog.getOpenFileName(self, 'Select Output File', dir)
        print(str(out_fname[0][-3:]))

        if str(out_fname[0][-4:]) == ".txt":
            print("Second page")
            self.browseOutFileWindow.hide()
        out_fname = out_fname[0]

        self.secondPage.pushButtonTotalEvap.clicked.connect(lambda: self.readOutputFile(out_fname, 2))
        self.secondPage.pushButtonSurfInfil.clicked.connect(lambda: self.readOutputFile(out_fname, 3))
        self.secondPage.pushButtonSoilPerc.clicked.connect(lambda: self.readOutputFile(out_fname, 4))
        self.secondPage.pushButtonBottomInfil.clicked.connect(lambda: self.readOutputFile(out_fname, 5))
        self.secondPage.pushButtonSurfRunoff.clicked.connect(lambda: self.readOutputFile(out_fname, 6))
        self.secondPage.pushButtonDrainOut.clicked.connect(lambda: self.readOutputFile(out_fname, 7))
        self.secondPage.pushButtonSurfDepth.clicked.connect(lambda: self.readOutputFile(out_fname, 8))
        self.secondPage.pushButtonSoilMoist.clicked.connect(lambda: self.readOutputFile(out_fname, 9))
        self.secondPage.pushButtonStorageDepth.clicked.connect(lambda: self.readOutputFile(out_fname, 10))





    def readOutputFile(self, out_fname, index_needed):

        self.out_fname = out_fname

        index_needed += 1

        with open(self.out_fname, 'r') as out_file:
            lines = out_file.readlines()

        for line_num in range(len(lines)):
            if lines[line_num].startswith("-------"):
                start_line = line_num + 1

        split_lines = lines[start_line].split(" ")

        '''
        index = 0

        print(' '.join(split_lines))

        for i in range(len(split_lines)):

            if split_lines[i] != '':
                split_lines[i] += " "

        l = ' '.join(split_lines)

        print("L: " + l)

        split_lines = l.split(" ")

        print(split_lines)

        index_got = 0

        for i in range(len(split_lines)):

            if index == index_needed + 1:
                print(i)
                index_got = i - 1
                print(split_lines[i - 1])
                break

            if split_lines[i] != '':
                print(index)
                index += 1

        location_start = 0

        location_end = 0

        for i in range(len(split_lines)):
            if i < index_got:
                if split_lines[i] == '':
                    location_start += 1
                else:
                    location_start += len(split_lines[i])
            if i == index_got:
                location_end = location_start + len(split_lines[i])

        '''

        self.writeInsFile(lines, start_line, index_needed - 1)

    # Write Instruction file based on the output parameter selected

    def writeInsFile(self, lines, start_line, index):

        ins_lines = "pif #\n#-------#\n"

        self.ins_fname = self.out_fname[:-3] + "ins"

        print("In writeInsFile")

        obs_name = ""

        if index == 2:
            self.secondPage.pushButtonTotalEvap.setEnabled(False)
            obs_name = "tevap"
            location_start = 35
            location_end = 42
        if index == 3:
            self.secondPage.pushButtonSurfInfil.setEnabled(False)
            obs_name = "sinfil"
            location_start = 44
            location_end = 52
        if index == 4:
            self.secondPage.pushButtonSoilPerc.setEnabled(False)
            obs_name = "sperc"
            location_start = 54
            location_end = 62
        if index == 5:
            self.secondPage.pushButtonBottomInfil.setEnabled(False)
            obs_name = "binfil"
            location_start = 64
            location_end = 72
        if index == 6:
            self.secondPage.pushButtonSurfRunoff.setEnabled(False)
            obs_name = "srunoff"
            location_start = 74
            location_end = 82
        if index == 7:
            self.secondPage.pushButtonDrainOut.setEnabled(False)
            obs_name = "dflow"
            location_start = 84
            location_end = 92
        if index == 8:
            self.secondPage.pushButtonSurfDepth.setEnabled(False)
            obs_name = "sudepth"
            location_start = 94
            location_end = 102
        if index == 9:
            self.secondPage.pushButtonSoilMoist.setEnabled(False)
            obs_name = "smoist"
            location_start = 104
            location_end = 112
        if index == 10:
            self.secondPage.pushButtonStorageDepth.setEnabled(False)
            obs_name = "stdepth"
            location_start = 114
            location_end = 122

        print("After Switch Case")

        line_num = start_line

        self.out_lines = lines[start_line:]

        self.output_location_start = location_start
        self.output_location_end = location_end

        # Output values before calibration:

        self.output_values_before_calibration = []

        for line in self.out_lines:
            self.output_values_before_calibration.append(line[location_start:(location_end+1)])



        print(self.output_values_before_calibration)

        temp = []

        for i in self.output_values_before_calibration:
            temp.append(float(i.strip()))

        print("out of for loop")
        self.output_values_before_calibration = temp
        print(self.output_values_before_calibration)



        self.obs_name = obs_name
        '''

        while line_num < len(lines):

            dstamp = lines[line_num].split()[0]

            dstamp = dstamp.split("/")[0] + dstamp.split("/")[1]

            tstamp = lines[line_num].split()[1]

            tstamp = tstamp.split(":")[0] + tstamp.split(":")[1]

            print(dstamp + tstamp)


            # obs_name += tstamp

            line = "l1  [" + obs_name + dstamp + tstamp + "]" + str(location_start) + ":" + str(location_end) + "\n"

            ins_lines += line

            line_num += 1
        '''

        while line_num < len(lines):
            dstamp = lines[line_num].split()[0]

            dstamp = dstamp.split("-")[0] + dstamp.split("-")[1]

            tstamp = lines[line_num].split()[1]

            tstamp = tstamp.split(":")[0] + tstamp.split(":")[1]

            print(dstamp + tstamp)

            # obs_name += tstamp

            line = "l1  [" + obs_name + dstamp + tstamp + "]" + str(location_start) + ":" + str(location_end) + "\n"

            ins_lines += line

            line_num += 1
        print(ins_lines)

        with open(self.ins_fname, 'w') as f:
            f.write(ins_lines)


        self.secondPage.tabOuter.setCurrentIndex(2)
        self.enterControlSection(obs_name)

    # Provide observation file

    def enterControlSection(self, obs_name):

        self.browseObsFileWindow = LoadBrowseWindow()

        self.browseObsFileWindow.label.setText("                Select Observation data File for " + obs_name + ":")

        self.browseObsFileWindow.pushButtonBrowse.clicked.connect(self.readObsFile)

    # Read observation file and create control file based on all the data provided

    def readObsFile(self):

        dir = '/Users/surajkamble/Documents/SWMM2PEST'

        print(dir)

        obs_fname = QFileDialog.getOpenFileName(self, 'Select Observation Data File', dir)
        print(str(obs_fname[0][-3:]))


        self.browseObsFileWindow.hide()
        obs_fname = obs_fname[0]

        '''
        Read observation file
        '''

        with open(obs_fname, 'r') as f:
            obs_data = f.readlines()

        '''
        Add control data
        '''

        '''
        pcf	
        * control data
        restart	estimation
           15   580    1     0     1
            1     1 single point 1 0 0
          5.0   2.0   0.3    0.01  10
          5.0   5.0   0.001
          0.1
           30  0.01     4     3  0.01     3
            1     1     1
        
        '''

        self.measured_data = obs_data

        '''
        * control data
        RSTFLE PESTMODE
        NPAR NOBS NPARGP NPRIOR NOBSGP [MAXCOMPDIM] [DERZEROLIM]
        NTPLFLE NINSFLE PRECIS DPOINT [NUMCOM JACFILE MESSFILE] [OBSREREF]
        RLAMBDA1 RLAMFAC PHIRATSUF PHIREDLAM NUMLAM [JACUPDATE] [LAMFORGIVE] [DERFORGIVE]
        RELPARMAX FACPARMAX FACORIG [IBOUNDSTICK UPVECBEND] [ABSPARMAX]
        PHIREDSWH [NOPTSWITCH] [SPLITSWH] [DOAUI] [DOSENREUSE] [BOUNDSCALE]
        NOPTMAX PHIREDSTP NPHISTP NPHINORED RELPARSTP NRELPAR [PHISTOPTHRESH] [LASTRUN] [PHIABANDON]
        ICOV ICOR IEIG [IRES] [JCOSAVE] [VERBOSEREC] [JCOSAVEITN] [REISAVEITN] [PARSAVEITN] [PARSAVERUN]
        
        '''
        control_file_data = "pcf\n* control data\nrestart estimation\n"

        all_selected_pars = []

        for sub in self.subcatchments_data:
            all_selected_pars.extend(sub.get_all_selected_pars())


        all_selected_pars.extend(self.lid_controls_data.get_all_selected_pars())


        num_of_pars = len(all_selected_pars)

        print(obs_data[:50])

        num_of_obs = len(obs_data)


        control_file_data += "   " + str(num_of_pars) + "    " + str(num_of_obs) + "    " + "1    0    1\n"

        control_file_data +=  "    1     1 single point 1 0 0\n"

        control_file_data += "  5.0   2.0   0.3    0.01  10\n"

        control_file_data += "  5.0   5.0   0.001\n"

        control_file_data += "  0.1\n"

        control_file_data += "   30  0.01     4     3  0.01     3\n"

        control_file_data += "    1     1     1\n"


        '''
        Parameter data
        '''

        control_file_data += "* parameter groups\nparagroup  relative 0.01  0.0  switch  2.0 parabolic\n\n"

        control_file_data += "* parameter data\n"



        #  ldu_wdth  fixed  factor   90.1   30.0  110.0  paragroup  1.0   0.0  1

        for par in all_selected_pars:

            par_short_name = par.get_short_name()[1:-1]

            par_val = par.get_value()
            par_low_limit = par.get_lower_limit()
            par_up_limit = par.get_upper_limit()

            control_file_data += par_short_name + "           "

            if par.is_checked_fixed:
                control_file_data += "fixed"
            if par.is_checked_none:
                control_file_data += "none"

            control_file_data += "  factor    " + par_val + "    " + par_low_limit + "    " + \
                par_up_limit + "    paragroup  1.0  0.0  1\n"

        '''
        Observation data
        '''
        control_file_data += "* observation groups\nobsgroup\n\n"

        control_file_data += "* observation data\n"

        line_num = 0

        lines = self.out_lines

        obs_name = self.obs_name

        obs_lines = ""

        while line_num < len(lines):

            dstamp = lines[line_num].split()[0]

            dstamp = dstamp.split("-")[0] + dstamp.split("-")[1]

            tstamp = lines[line_num].split()[1]

            tstamp = tstamp.split(":")[0] + tstamp.split(":")[1]

            print(dstamp + tstamp)


            # obs_name += tstamp

            line = obs_name + dstamp + tstamp + "               " + str(obs_data[line_num].strip('\n')) + "    1.0  obsgroup" "\n"

            obs_lines += line

            line_num += 1

        control_file_data += obs_lines + "\n"

        '''
        Model Command Line Section
        '''

        control_file_data += "* model command line\n"

        self.rpt_fname = self.inp_fname[:-3] + "rpt"
        self.out_fname1 = self.inp_fname[:-3] + "out"
        command_line_data = "swmm5110_test " + self.inp_fname + " " + self.rpt_fname + " " + self.out_fname1 + "\n\n"

        control_file_data += command_line_data

        '''
        Model Input Output Data Section
        '''

        control_file_data += "* model input/output\n"

        self.tpl_fname = self.inp_fname[:-3] + "tpl"

        control_file_data += self.tpl_fname + " " + self.inp_fname + "\n"

        control_file_data += self.ins_fname + " " + self.out_fname + "\n\n"

        control_file_data += "* prior information\n\n"

        self.control_fname = self.inp_fname[:-3] + "pst"

        with open(self.control_fname, 'w') as f:
            f.write(control_file_data)

        '''
        # Loading GIF

        self.gif = QMovie("LoadingGif.gif", QByteArray(), self)

        self.gif.setCacheMode(QMovie.CacheAll)
        self.gif.setSpeed(100)

        self.secondPage.lableLoading.setMovie(self.gif)

        self.gif.start()
        self.gif.loopCount()
        '''

        self.secondPage.pushButtonRunPEST.clicked.connect(self.run_pest)

    # Run PEST when button clicked

    def run_pest(self):

        self.secondPage.pushButtonRunPEST.setEnabled(False)


        self.pest_thread = PestThread(self.control_fname)

        self.secondPage.labelLoading.setText("     Running...")

        # print(self.measured_data)

        self.pest_thread.start()

        print("After calling thread")

        self.pest_thread.finished.connect(self.finished_pest_thread)

    # After running PEST

    def finished_pest_thread(self):

        self.secondPage.pushButtonRunPEST.setEnabled(True)

        self.secondPage.labelLoading.setText(" ")

        # print(self.output_values_before_calibration)

        with open(self.out_fname, 'r') as out_file:
            out_lines = out_file.readlines()

        for line_num in range(len(out_lines)):
            if out_lines[line_num].startswith("-------"):
                start_line = line_num + 1

        # Output values after calibration:

        out_lines = out_lines[start_line:]

        self.output_values_after_calibration = []

        for line in out_lines:
            self.output_values_after_calibration.append(line[self.output_location_start:(self.output_location_end + 1)])

        # print(self.output_values_after_calibration)




        '''
        # figure = Figure(figsize=(4, 2), dpi=100)

        self.graph_window = Graph(self.output_values_before_calibration, self.output_values_after_calibration, self.measured_data)
        self.graph_window.setWindowTitle("Before Calibration Vs. After Calibration")

        self.graph_window.show()
        '''
        # x = linspace(0, 5, 5)

        self.plot_graphs()

    # Display graphs

    def plot_graphs(self):
        # print(len(self.measured_data))
        # m = self.output_values_before_calibration[0:10]



        # -----------------------------------------

        temp = []
        for i in self.output_values_after_calibration:
            temp.append(float(i.strip()))

        self.output_values_after_calibration = temp

        temp1 = []

        for i in self.measured_data:
            temp1.append(float(i.strip()))

        self.measured_data = temp1

        print("Measured data: ")
        print(self.measured_data)

        print("Before calibration: ")
        print(self.output_values_before_calibration)

        print("After calibration: ")
        print(self.output_values_after_calibration)

        self.measured_data = self.measured_data[:len(self.output_values_after_calibration)]

        # print(len(self.measured_data))
        # print(len(self.output_values_after_calibration))

        x = linspace(min(self.measured_data), max(self.measured_data), len(self.measured_data))


        self.win = pg.GraphicsWindow(title="Output Graphs")

        p = self.win.addPlot(title="Measured data Vs. Output data before calibration")

        p.addLegend(offset=100)
        p.setLabel("left", "Drain Outflow")
        p.setLabel("bottom", "Time Series")

        p.plot(self.measured_data, pen='b', name="Measured data")
        p.plot(self.output_values_before_calibration, pen='g', name="Output before calibration")

        self.win1 = pg.GraphicsWindow(title="Output Graphs")

        p1 = self.win1.addPlot(title="Measured data Vs. Output data after calibration")

        p1.addLegend(offset=100)
        p1.setLabel("left", "Drain Outflow")
        p1.setLabel("bottom", "Time Series")

        p1.plot(self.measured_data, pen='b', name="Measured data")
        p1.plot(self.output_values_after_calibration, pen='g', name="Output after calibration")

        '''

        self.win = pg.GraphicsWindow(title="Output Graphs")

        p = self.win.addPlot(title="Measured data Vs. Output data before calibration")
        p.plot(x, self.measured_data, pen='b')
        p.plot(x, self.output_values_before_calibration, pen='r')

        p = self.win.addPlot(title="Measured data Vs. Output data after calibration")
        p.plot(x, self.measured_data, pen='b')
        p.plot(x, self.output_values_after_calibration, pen='g')

        '''

        # ----------------------------------------------------

        '''

        # E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Time_Series.txt
        # E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\After_Calibration.txt
        # E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Before_Calibration.txt
        # E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Measured.txt

        time_series = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Time_Series.txt"
        measured = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Measured.txt"
        before_calibration = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\Before_Calibration.txt"
        after_calibration = "E:\\UC\EPA\SWMM2PEST\SWMM2PEST\Demo\After_Calibration.txt"

        with open(time_series, 'r') as time_series_fname:

            time_series_data = time_series_fname.readlines()

        for i in range(len(time_series_data)):
            time_series_data[i] = (time_series_data[i].strip())

        print("Time Series Data:")
        print(time_series_data)

        with open(measured, 'r') as measured_fname:

            measured_data = measured_fname.readlines()

        for i in range(len(measured_data)):
            measured_data[i] = float(measured_data[i].strip())

        print("Measured Data:")
        print(measured_data)

        with open(before_calibration, 'r') as before_calibration_fname:

            before_calibration_data = before_calibration_fname.readlines()

        for i in range(len(before_calibration_data)):
            before_calibration_data[i] = float(before_calibration_data[i].strip())

        print("Before Calibration Data:")
        print(before_calibration_data)

        with open(after_calibration, 'r') as after_calibration_fname:

            after_calibration_data = after_calibration_fname.readlines()

        for i in range(len(after_calibration_data)):
            temp = (after_calibration_data[i].strip("-\n"))

            after_calibration_data[i] = float((float(temp) * 75)/100)

        print("After Calibration Data:")
        print(after_calibration_data)

        # x = time_series_data


        # print(len(self.measured_data))
        # print(len(self.output_values_after_calibration))

        x = len(measured_data)

        self.win = pg.GraphicsWindow(title="Output Graphs")


        p = self.win.addPlot(title="Measured data Vs. Output data after calibration")

        p.addLegend(offset=100)
        p.setLabel("left", "Drain Outflow")
        p.setLabel("bottom", "Time Series")

        p.plot(measured_data, pen='b', name="Measured data")
        p.plot(after_calibration_data, pen='g', name="Output after calibration")


        self.win1 = pg.GraphicsWindow(title="Output Graphs")

        p1 = self.win1.addPlot(title="Measured data Vs. Output data before calibration")

        p1.addLegend(offset=100)
        p1.setLabel("left", "Drain Outflow")
        p1.setLabel("bottom", "Time Series")

        p1.plot(measured_data, pen='b', name="Measured data")
        p1.plot(before_calibration_data, pen='g', name="Output before calibration")


        # pg.plot(self.measured_data, self.output_values_after_calibration, title="Measured data Vs. Post Calibration data")

        '''

        '''

        self.running_window = LoadPESTOutputWindow()

        print(self.pest_thread.output)

        self.running_window.labelPESTOutput.setText(self.pest_thread.output)
        '''




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

        if parameter.is_checked_fixed:
            self.dialog_box.checkBox_Fixed.setChecked(True)
        if parameter.is_checked_none:
            self.dialog_box.checkBox_None.setChecked(True)


        self.dialog_box.buttonBox.accepted.connect(lambda: self.saveParameterValues(parameter))

        self.dialog_box.buttonBox.rejected.connect(self.hideDialog)

    def hideDialog(self):
        self.dialog_box.hide()

    # Save upper and lower limit of the parameter value whenever changed

    def saveParameterValues(self, parameter):

        lower_limit = self.dialog_box.lineEdit_LowerLimit.text()

        upper_limit = self.dialog_box.lineEdit_UpperLimit.text()

        is_checked_fixed = self.dialog_box.checkBox_Fixed.checkState()

        is_checked_none = self.dialog_box.checkBox_None.checkState()

        if (self.current_sub is not None) and (parameter.name in vars(self.current_sub).keys()):

            vars(vars(self.current_sub)[parameter.name])['lower_limit'] = lower_limit
            vars(vars(self.current_sub)[parameter.name])['upper_limit'] = upper_limit

            vars(vars(self.current_sub)[parameter.name])['is_checked_fixed'] = is_checked_fixed
            vars(vars(self.current_sub)[parameter.name])['is_checked_none'] = is_checked_none

        if parameter.name in vars(self.lid_controls_data).keys():

            vars(vars(self.lid_controls_data)[parameter.name])['lower_limit'] = lower_limit
            vars(vars(self.lid_controls_data)[parameter.name])['upper_limit'] = upper_limit

            vars(vars(self.lid_controls_data)[parameter.name])['is_checked_fixed'] = is_checked_fixed
            vars(vars(self.lid_controls_data)[parameter.name])['is_checked_none'] = is_checked_none


        # print(self.current_sub.area.lower_limit)
        # print(self.current_sub.area.upper_limit)

        self.dialog_box.hide()

    # Load the parameters window for subcatchments and LID controls

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
                surface_layer_roughness_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_roughness)
                surface_layer_slope_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_slope)
                surface_layer_swale_side_slope_line_edit = self.createLineEdit(self.lid_controls_data.surface_layer_swale_side_slope)

                surface_layer_storage_depth_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_storage_depth))
                surface_layer_vegetative_cover_fraction_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_vegetative_cover_fraction))
                surface_layer_roughness_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_roughness))
                surface_layer_slope_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_slope))
                surface_layer_swale_side_slope_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.surface_layer_swale_side_slope))

                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_storage_depth.label, surface_layer_storage_depth_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_vegetative_cover_fraction.label, surface_layer_vegetative_cover_fraction_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_roughness.label, surface_layer_roughness_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_slope.label, surface_layer_slope_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.surface_layer_swale_side_slope.label, surface_layer_swale_side_slope_line_edit)

                print(self.lid_controls_data.has_drainmat_system)

            if item.text() == "Pavement":
                pavement_layer_thickness_line_edit = self.createLineEdit(self.lid_controls_data.pavement_layer_thickness)
                pavement_layer_void_ratio_line_edit = self.createLineEdit(self.lid_controls_data.pavement_layer_void_ratio)
                pavement_layer_impervious_surface_fraction_line_edit = self.createLineEdit(self.lid_controls_data.pavement_layer_impervious_surface_fraction)
                pavement_layer_permeability_line_edit = self.createLineEdit(self.lid_controls_data.pavement_layer_permeability)
                pavement_layer_clogging_factor_line_edit = self.createLineEdit(self.lid_controls_data.pavement_layer_clogging_factor)

                pavement_layer_thickness_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.pavement_layer_thickness))
                pavement_layer_void_ratio_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.pavement_layer_void_ratio))
                pavement_layer_impervious_surface_fraction_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.pavement_layer_impervious_surface_fraction))
                pavement_layer_permeability_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.pavement_layer_permeability))
                pavement_layer_clogging_factor_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.pavement_layer_clogging_factor))

                self.window.formLayout.addRow(self.lid_controls_data.pavement_layer_thickness.label, pavement_layer_void_ratio_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.pavement_layer_void_ratio.label, pavement_layer_void_ratio_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.pavement_layer_impervious_surface_fraction.label, pavement_layer_impervious_surface_fraction_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.pavement_layer_permeability.label, pavement_layer_permeability_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.pavement_layer_clogging_factor.label, pavement_layer_clogging_factor_line_edit)

            if item.text() == "Soil":
                soil_layer_thickness_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_thickness)
                soil_layer_porosity_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_porosity)
                soil_layer_field_capacity_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_field_capacity)
                soil_layer_wilting_point_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_wilting_point)
                soil_layer_conductivity_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_conductivity)
                soil_layer_slope_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_slope)
                soil_layer_suction_head_line_edit = self.createLineEdit(self.lid_controls_data.soil_layer_suction_head)

                soil_layer_thickness_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_thickness))
                soil_layer_porosity_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_porosity))
                soil_layer_field_capacity_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_field_capacity))
                soil_layer_wilting_point_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_wilting_point))
                soil_layer_conductivity_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_conductivity))
                soil_layer_slope_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_slope))
                soil_layer_suction_head_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.soil_layer_suction_head))

                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_thickness.label, soil_layer_thickness_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_porosity.label, soil_layer_porosity_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_field_capacity.label, soil_layer_field_capacity_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_wilting_point.label, soil_layer_wilting_point_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_conductivity.label, soil_layer_conductivity_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_slope.label, soil_layer_slope_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.soil_layer_suction_head.label, soil_layer_suction_head_line_edit)

            if item.text() == "Storage":
                storage_layer_height_line_edit = self.createLineEdit(self.lid_controls_data.storage_layer_height)
                storage_layer_void_ratio_line_edit = self.createLineEdit(self.lid_controls_data.storage_layer_void_ratio)
                storage_layer_filtration_rate_line_edit = self.createLineEdit(self.lid_controls_data.storage_layer_filtration_rate)
                storage_layer_clogging_factor_line_edit = self.createLineEdit(self.lid_controls_data.storage_layer_clogging_factor)

                storage_layer_height_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.storage_layer_height))
                storage_layer_void_ratio_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.storage_layer_void_ratio))
                storage_layer_filtration_rate_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.storage_layer_filtration_rate))
                storage_layer_clogging_factor_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.storage_layer_clogging_factor))

                self.window.formLayout.addRow(self.lid_controls_data.storage_layer_height.label, storage_layer_height_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.storage_layer_void_ratio.label, storage_layer_void_ratio_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.storage_layer_filtration_rate.label, storage_layer_filtration_rate_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.storage_layer_clogging_factor.label, storage_layer_clogging_factor_line_edit)

            if item.text() == "Drain":
                drain_coefficient_line_edit = self.createLineEdit(self.lid_controls_data.drain_coefficient)
                drain_exponent_line_edit = self.createLineEdit(self.lid_controls_data.drain_exponent)
                drain_offset_height_line_edit = self.createLineEdit(self.lid_controls_data.drain_offset_height)
                drain_delay_line_edit = self.createLineEdit(self.lid_controls_data.drain_delay)

                drain_coefficient_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drain_coefficient))
                drain_exponent_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drain_exponent))
                drain_offset_height_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drain_offset_height))
                drain_delay_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drain_delay))

                self.window.formLayout.addRow(self.lid_controls_data.drain_coefficient.label, drain_coefficient_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.drain_exponent.label, drain_exponent_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.drain_offset_height.label, drain_offset_height_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.drain_delay.label, drain_delay_line_edit)

            if item.text() == "DrainMat":

                print("In Drain Mat")
                drainmat_thickness_line_edit = self.createLineEdit(self.lid_controls_data.drainmat_thickness)
                drainmat_void_fraction_line_edit = self.createLineEdit(self.lid_controls_data.drainmat_void_fraction)
                drainmat_roughness_line_edit = self.createLineEdit(self.lid_controls_data.drainmat_roughness)

                drainmat_thickness_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drainmat_thickness))
                drainmat_void_fraction_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drainmat_void_fraction))
                drainmat_roughness_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.lid_controls_data.drainmat_roughness))

                self.window.formLayout.addRow(self.lid_controls_data.drainmat_thickness.label, drainmat_thickness_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.drainmat_void_fraction.label, drainmat_void_fraction_line_edit)
                self.window.formLayout.addRow(self.lid_controls_data.drainmat_roughness.label, drainmat_roughness_line_edit)




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

            suction_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.suction))
            hydraulic_conductivity_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.hydraulic_conductivity))
            initial_moisture_deficit_line_edit.clicked.connect(lambda: self.loadDialogBoxWindow(self.current_sub.initial_moisture_deficit))




            self.window.formLayout.addRow(self.current_sub.area.label, area_line_edit)

            self.window.formLayout.addRow(self.current_sub.percent_impervious.label, percent_impervious_line_edit)

            self.window.formLayout.addRow(self.current_sub.width.label, width_line_edit)

            self.window.formLayout.addRow(self.current_sub.percent_slope.label, percent_slope_line_edit)


            self.window.formLayout.addRow(self.current_sub.n_imperv.label, n_imperv_line_edit)

            self.window.formLayout.addRow(self.current_sub.n_perv.label, n_perv_line_edit)

            self.window.formLayout.addRow(self.current_sub.storage_depth_imperv.label, storage_depth_imperv_line_edit)

            self.window.formLayout.addRow(self.current_sub.storage_depth_perv.label, storage_depth_perv_line_edit)

            self.window.formLayout.addRow(self.current_sub.percent_zero_impervious.label, percent_zero_impervious_line_edit)


            self.window.formLayout.addRow(self.current_sub.suction.label, suction_line_edit)

            self.window.formLayout.addRow(self.current_sub.hydraulic_conductivity.label, hydraulic_conductivity_line_edit)

            self.window.formLayout.addRow(self.current_sub.initial_moisture_deficit.label, initial_moisture_deficit_line_edit)


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
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()


class LoadParametersWindow(QMainWindow, ParametersWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        print("In Pars window")
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()


class LoadDialogBoxWindow(QMainWindow, DialogBox.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        print("In Dialog Box window")
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()


class cQLineEdit(QtWidgets.QLineEdit):

    clicked = pyqtSignal()

    def __init__(self, widget):
        super(cQLineEdit, self).__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


class LoadBrowseWindow(QMainWindow, browseWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()


class LoadPESTOutputWindow(QMainWindow, PESTOutputWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()


class LoadHelpWindow(QMainWindow, HelpWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    firstPage = LoadFirstPage()
    # firstPage.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    # firstPage.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    firstPage.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    firstPage.show()
    sys.exit(app.exec_())


