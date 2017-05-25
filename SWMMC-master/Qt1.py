# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:41:42 2016

@author: SKamble
"""

import sys
from PyQt4 import QtGui
from One import Create_pst
from PyQt4.QtCore import QThread
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import re
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from numpy import linspace



#Separate thrad that calls pest and runs it in the background
class CallPestThread(QThread):
    
    def __init__(self ,tpl_obj):
        QThread.__init__(self)
        
        self.tpl = tpl_obj
        
    def __del__(self):
        self.wait()
        
    def run(self):
        print "in thread"
        self.done = False
        self.output = self.tpl.call_pest()
        print self.output
        
        return self.done
        
    
    
#Whole GUI in this class
class Example(QtGui.QWidget):
    
    tpl_file_name = ""
    
    par_objs_copy = []
        
    def __init__(self):
        super(Example, self).__init__()
        
        
        self.initUI()
        
    #   Create labels for data in control section
    def create_lbl(self, par_name):
        return QtGui.QLabel(par_name + " :", self)
        
        
                
    def initUI(self):      
                                
        #   Label: Browse Template file 
        tpl_name_lbl = QtGui.QLabel("Template File: ")
        #tpl_name_lbl.move(150,100)
        
        #   Button: Open Template file 
        tpl_btn = QtGui.QPushButton('Browse')
        tpl_btn.setToolTip('Browse Template file')
        tpl_btn.resize(tpl_btn.sizeHint())
        #tpl_btn.move(250, 100)
        tpl_btn.clicked.connect(self.tpl_btn_click)
        
        #   Label: Display Full Name of template file
        self.tpl_file_lbl = QtGui.QLabel(self)
        #self.tpl_file_lbl.move(350,95)
        
        #   Label: Model output file
        out_name_lbl = QtGui.QLabel("Model Output File: ")
        out_name_lbl.resize(out_name_lbl.sizeHint())
        #out_name_lbl.move(150, 150)
        
        #   Button: Open Model Output file 
        out_btn = QtGui.QPushButton('Browse')
        out_btn.setToolTip('Browse Model Output file')
        out_btn.resize(out_btn.sizeHint())
        #out_btn.move(250, 150)
        out_btn.clicked.connect(self.out_btn_click)
        
        #   Label: Display Full Name of output file
        self.out_file_lbl = QtGui.QLabel()
        
        #self.out_file_lbl.move(350,145)
        
        
        #   Label: Model output parameter
        self.out_par_name_lbl = QtGui.QLabel("Model Output Parameter: ")
        #out_par_name_lbl.move(150, 200)
        self.out_par_name_lbl.resize(self.out_par_name_lbl.sizeHint())
        
        #   ComboBox: Model output parameter
        self.out_par = QtGui.QComboBox(self)
        #out_par.move(300, 200)
        #self.out_par.editingFinished.connect(self.pp)
        self.out_par.resize(self.out_par.sizeHint())
        
        self.num_of_out_pars = 1
        
        
        #   Label: field data file
        field_name_lbl = QtGui.QLabel("Field Data File: ")
        field_name_lbl.resize(field_name_lbl.sizeHint())
        
        #   Button: Open Field data file
        field_btn = QtGui.QPushButton('Browse')
        field_btn.resize(field_btn.sizeHint())
        field_btn.clicked.connect(self.field_btn_click)
        
        #   Label: Display full name of field data file
        self.field_file_lbl = QtGui.QLabel()
        
        
        #   Number of observations label
        self.num_obs_lbl = QtGui.QLabel("Number of Observations: ")
        self.num_obs_lbl.resize(300, 150)
        
        #   Number of observations Line Edit
        self.num_obs = QtGui.QLineEdit(self)
        
        
        #   Add button for model output parameter
        add_btn = QtGui.QPushButton('Add')
        add_btn.resize(0, 0)
        add_btn.clicked.connect(self.add_output_par)
        
        #   Main grid layout
        self.grid = QtGui.QGridLayout()
        self.grid.setVerticalSpacing(15)
        self.grid.setHorizontalSpacing(15)
        
        self.grid.addWidget(tpl_name_lbl, 0, 0)
        self.grid.addWidget(tpl_btn, 0, 1, 1, 1)
        self.grid.addWidget(self.tpl_file_lbl, 0, 2, 1, 1)
        
        self.grid.addWidget(add_btn, 1, 0, 1, 1)
                
        self.grid.addWidget(out_name_lbl, 1, 1)
        self.grid.addWidget(out_btn, 1, 2, 1, 1)
        self.grid.addWidget(self.out_file_lbl, 1, 3, 1, 1)
        
        self.grid.addWidget(self.out_par_name_lbl, 2, 1)
        self.grid.addWidget(self.out_par, 2, 2, 1, 2)
        
        self.grid.addWidget(field_name_lbl, 3, 1)
        self.grid.addWidget(field_btn, 3, 2, 1, 1)
        self.grid.addWidget(self.field_file_lbl, 3, 3, 1, 1)
        
        self.grid.addWidget(self.num_obs_lbl, 4, 0)
        self.grid.addWidget(self.num_obs, 4, 1, 1, 2)
        
        
        #   Grid for parameter data
        self.par_grid = QtGui.QGridLayout()
        self.grid.addLayout(self.par_grid, 5, 0, 10, 8)
        self.par_grid.setHorizontalSpacing(15)
        self.par_grid.setVerticalSpacing(1)
        
        #   Label: Running
        self.running_lbl = QtGui.QLabel(self)
        self.running_lbl.resize(self.running_lbl.sizeHint())
        self.grid.addWidget(self.running_lbl, 4, 4, 1, 1)
        
        
        #   Go Button
        self.go_btn = QtGui.QPushButton('GO')
        self.grid.addWidget(self.go_btn, 4, 8, 1, 1)
        self.go_btn.clicked.connect(self.p)
        
        #self.ctl_grid = QtGui.QGridLayout()
        #self.grid.addLayout(self.ctl_grid, 4, 1, 30, 30)
        
        
        self.setLayout(self.grid)
        
        

        
        '''
        #   Control Data Section
        
        self.ctl_data_lbls = []
        self.ctl_data_txt_edits = []
        x, y = 150, 180
        for key in ctl_data.keys()[::-1]:
            x = 150
            print ctl_data.keys()[::-1]
            for par in ctl_data[key]:
                self.create_lbl(par).move(x, y)
                x += 100
            y += 50
        '''       
        
        '''
        self.statusBar()
        
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        '''
        
        self.setGeometry(100, 100, 950, 900)
        self.setWindowTitle('Calibration of SWMM models')
        self.show()
        
        
        
    # Add btn clicked
    def add_output_par(self):
        
        self.num_of_out_pars += 1
        
        
        
        #   Button: Open Model Output file 
        out_btn1 = QtGui.QPushButton('Browse')
        out_btn1.setToolTip('Browse Model Output file')
        out_btn1.resize(out_btn1.sizeHint())
        #out_btn.move(250, 150)
        out_btn1.clicked.connect(self.out_btn_click1)
        
        #   Label: Display Full Name of output file
        self.out_file_lbl1 = QtGui.QLabel()
        
        #self.out_file_lbl.move(350,145)
        
        
        #   ComboBox: Model output parameter
        self.out_par1 = QtGui.QComboBox(self)
        #out_par.move(300, 200)
        #self.out_par.editingFinished.connect(self.pp)
        self.out_par1.resize(self.out_par1.sizeHint())
                
        
        #   Button: Open Field data file
        field_btn1 = QtGui.QPushButton('Browse')
        field_btn1.resize(field_btn1.sizeHint())
        field_btn1.clicked.connect(self.field_btn_click1)
        
        #   Label: Display full name of field data file
        self.field_file_lbl1 = QtGui.QLabel()
        
        self.grid.addWidget(out_btn1, 1, 4, 1, 1)
        self.grid.addWidget(self.out_par1, 2, 4, 1, 2)
        self.grid.addWidget(field_btn1, 3, 4, 1, 1)
        
        self.grid.addWidget(self.out_file_lbl1, 1, 5, 1, 1)
        self.grid.addWidget(self.field_file_lbl1, 3, 5, 1, 1)
        
        
    # Called when Go button is clicked
    def p(self):
        
        
        self.running_lbl.setText("Running...")

        print Example.par_objs_copy
        r = 0
        print "para.rows"
        print self.para_rows
        for row in self.para_rows:
            print "in for loop"
            print "object"
            vals = []
            for col in row:
                print "in 2nd loop"
                
                #Logic for dropdown
                if isinstance(col, QtGui.QComboBox):
                    print col.currentText()
                    vals.append((col.currentText().lower()))
                else:
                    print col.text()
                    vals.append(col.text())
                
            #Set all values for a Parameter object
            (Example.par_objs_copy[r]).set_all_vals(vals)
            r += 1
            
        for par in Example.par_objs_copy:
            par_trans, val, l, h = par.get_all_vals()
            print "These are the parameter values"
            print par_trans, val, l, h
            
            
        self.tpl.fill_ctl_data_section(len(Example.par_objs_copy), self.num_obs.text(),
                                            self.num_of_out_pars)
        self.tpl.fill_par_data_section(Example.par_objs_copy)
        
        self.tpl.generate_ins(self.out_par.currentText(), 
                              self.out_fname, self.num_of_out_pars, self.field_fname)
        
        if self.num_of_out_pars > 1:
            self.tpl.generate_ins(self.out_par1.currentText(), 
                                  self.out_fname1, self.num_of_out_pars, self.field_fname1)
            
                    
        #self.tpl.fill_obs_data_section(self.field_fname, self.out_fname)       
        
        #if self.num_of_out_pars > 1:
            #self.tpl.fill_obs_data_section(self.field_fname1, self.out_fname1)
        
        self.tpl.fill_other_sections(self.num_of_out_pars)
        
        #   Calling thread
        print "Before creating thread"
        self.get_thread = CallPestThread(self.tpl)
        
        
        self.get_thread.start()
        
        self.get_thread.finished.connect(self.ppp)
        
        
    def ppp(self):
        
        print "Output:"
        output = self.get_thread.output
        print output
        
        print "After thread call"
                
        self.running_lbl.setText("Completed")
        
        self.o = Output(output)
        self.o.show()
        
        #rec_file = self.tpl_file_name.split('.')[0] + ".rec"
        out_name = self.out_par.currentText()
        out_file = self.out_fname
        
        field_vals = self.tpl.field_vals
        old_vals = self.tpl.old_vals
        
        new_vals = self.tpl.get_new_vals(out_file, out_name)
        
        x = linspace(0, len(field_vals)-1, len(field_vals))
        
        
        print "old_vals = "
        print old_vals
        
        print "new_vals = "
        print new_vals
        
        self.graph = GraphOutput(field_vals, old_vals, new_vals, x)
        self.graph.setWindowTitle("Before Calibration vs After Calibration")
        self.graph.show()
        
        
        '''
        for row in self.para_rows:
            for col in row:
                print "par vals"
                print col.text()
            
        print "\n"
        '''
            

        
    def pp(self):
        print "EDITED" 
        
            
        print self.out_par.text()
         
            
    
        
            
    
    #   Open template file        
    def tpl_btn_click(self):

        tpl_fname = QtGui.QFileDialog.getOpenFileName(self, 'Open Template file', 
                '/home')
        print tpl_fname
        self.tpl = Create_pst(tpl_fname)
        print "before type"
        print type(self.tpl)
        print "after type"
        print self.tpl.par_objs
        Example.par_objs_copy = self.tpl.par_objs[:]
        print "Example.par_objs_copy"
        print Example.par_objs_copy
        self.tpl_file_lbl.setText(tpl_fname.split('/')[-1])
        Example.tpl_file_name = tpl_fname
        print Example.tpl_file_name
        self.tpl_file_lbl.resize(self.tpl_file_lbl.sizeHint())
        #Error here
        x, y = 0, 0
        print "In method"
        
        #para = Example.par_objs_copy[0]
        
        self.out_par.resize(100, 200)
        
        self.para_rows =[] #Parameter rows in the GUI
        
        count = 0
        for para in Example.par_objs_copy:
            print "In loop"
            print para.get_name()
            
            #   parameter name label
            self.par_grid.addWidget(QtGui.QLabel(para.get_name(), self), x, y, 1, 1)
            
            par_trans = QtGui.QComboBox(self)
            par_trans.addItems(["Fixed", "None", "Log", "Tied"])
                       
            
            val= QtGui.QLineEdit(self)
            print "After val" 
            print count
            #self.para_rows[count].append(val)
            print "After append"
            
            
            
            l_val = QtGui.QLineEdit(self)
            #self.para_rows[count].append(l_val)
            
            h_val = QtGui.QLineEdit(self)
            #self.para_rows[count].append(h_val)
            
            self.para_rows.append([par_trans, val, l_val, h_val])
            
            
            self.par_grid.addWidget(par_trans, x, y+1, 1, 1)
            
            #Add widget for dropdown
            self.par_grid.addWidget(val, x, y+2, 1, 1)
            
            print "After adding widget"
            self.par_grid.addWidget(l_val, x, y+3, 1, 1)
            self.par_grid.addWidget(h_val, x, y+4, 1, 1)
            
            x += 1
           
            print "Val = " + para.get_value()
            print self.para_rows
            print "2nd line of loop"
            count += 1
        
        count_col = 0
        count = 0
        for row in self.para_rows:
            for col in row:
                self.para_rows[count][count_col].editingFinished.connect(self.pp)
                count_col += 1
            count += 1
        
        
             
    #   Open Model output file             
    def out_btn_click(self):

        self.out_fname = QtGui.QFileDialog.getOpenFileName(self, 'Open Output file', 
                '/home')
        print self.out_fname
        self.out_file_lbl.setText(self.out_fname.split('/')[-1])
        self.out_file_lbl.resize(self.out_file_lbl.sizeHint())
        if self.out_fname[-3:] == "txt":
            self.out_par.addItems(["Surface Runoff","Drain Outflow", 
                                   "Surface Depth", "Storage Depth"])
            
        elif self.out_fname[-3:] == "rpt":
            self.out_par.addItems(["Surface Outflow(LID Summary)", "Drain Outflow(LID Summary)"])
        
        
    #   Open Field data file
    def field_btn_click(self):
        self.field_fname = QtGui.QFileDialog.getOpenFileName(self, 'Open Field data file',
                    '/home')
        self.field_file_lbl.setText(self.field_fname.split('/')[-1])
        self.field_file_lbl.resize(self.field_file_lbl.sizeHint())
        
        
        
    #   Open Model output file 1  
    def out_btn_click1(self):

        self.out_fname1 = QtGui.QFileDialog.getOpenFileName(self, 'Open Output file', 
                '/home')
        print self.out_fname1
        self.out_file_lbl1.setText(self.out_fname1.split('/')[-1])
        self.out_file_lbl1.resize(self.out_file_lbl.sizeHint())
        if self.out_fname1[-3:] == "txt":
            self.out_par1.addItems(["Surface Runoff","Drain Outflow", 
                                   "Surface Depth", "Storage Depth"])
        elif self.out_fname1[-3:] == "rpt":
            self.out_par1.addItems(["Surface Outflow(LID Summary)", "Drain Outflow(LID Summary)"])
        
        
    #   Open Field data file 1
    def field_btn_click1(self):
        self.field_fname1 = QtGui.QFileDialog.getOpenFileName(self, 'Open Field data file',
                    '/home')
        self.field_file_lbl1.setText(self.field_fname1.split('/')[-1])
        self.field_file_lbl1.resize(self.field_file_lbl1.sizeHint())

    #   Control Data Section
    
    
    
    #   Parameter Data Section
    
    
class Output(QtGui.QWidget):
    
    def __init__(self, output):
        super(Output, self).__init__()
        
        print "In Output"
        
        self.scrollArea = QtGui.QScrollArea()
        label = QtGui.QLabel(output)
        self.setWindowTitle('Output')
        self.scrollArea.setWidget(label)
        
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedHeight(600)
        self.scrollArea.setFixedWidth(800)
        
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.scrollArea)
        
        self.setGeometry(200, 200, 250, 200)
        self.setLayout(layout)
        self.show()
        
        
        print "After method  call"
        
  
class GraphOutput(QtGui.QDialog):
    def __init__(self, lines, old_vals, new_vals, x, parent=None):
        super(GraphOutput, self).__init__(parent)
 
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.setGeometry(300, 200, 650, 650)
         
        #self.toolbar = NavigationToolbar(self.canvas, self)
        #self.toolbar.hide()
        self.plot(lines, old_vals, new_vals, x)
 
    
 
        # set the layout
        layout = QtGui.QVBoxLayout()
        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)
 
    
         
    def plot(self, field_vals, old_vals, new_vals, x):
        ''' plot some random stuff '''
        #data = [random.random() for i in range(25)]
        ax1 = self.figure.add_subplot(211)
        #ax1.hold(False)
        ax1.set_title("Before Calibration")
        
        ax2 = self.figure.add_subplot(212)
        #ax2.hold(False)
        ax2.set_title("After Calibration")
        
        self.figure.text(0.5, 0.04, 'Time Series', ha='center', va='center')
        self.figure.text(0.06, 0.5, 'Output Values', ha='center', va='center', 
                         rotation='vertical')
        
        
        print len(field_vals)
        
        print len(old_vals)
        
        print len(new_vals)
        
        ax1.plot(x, field_vals, 'b', label="Field Values")
        ax1.plot(x, old_vals, 'r', label="Simulated Values")
        
        ax2.plot(x, field_vals, 'b', label="Field Values")
        ax2.plot(x, new_vals, 'r', label="Simulated Values")
        
        ax1.legend()
        
        ax2.legend()
        
        self.canvas.draw()
                                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.raise_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()