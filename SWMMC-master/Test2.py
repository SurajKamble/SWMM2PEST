# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:47:15 2016

@author: SKamble
"""

import sys
from PyQt4 import QtGui
 
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
 
import random
 
class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
 
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.setGeometry(300, 200, 650, 650)
         
       # self.toolbar = NavigationToolbar(self.canvas, self)
        #self.toolbar.hide()
        self.plot()
 
        '''
        # Just some button 
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)
 
        self.button1 = QtGui.QPushButton('Zoom')
        self.button1.clicked.connect(self.zoom)
         
        self.button2 = QtGui.QPushButton('Pan')
        self.button2.clicked.connect(self.pan)
         
        self.button3 = QtGui.QPushButton('Home')
        self.button3.clicked.connect(self.home)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        def home(self):
        self.toolbar.home()
    def zoom(self):
        self.toolbar.zoom()
    def pan(self):
        self.toolbar.pan()
        '''
 
        # set the layout
        layout = QtGui.QVBoxLayout()
        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)
 
    
         
    def plot(self):
        ''' plot some random stuff '''
        data = [1,2,3]
        data1 = [2,4,6]
        data2 = [3, 5, 7]
        
        ax1 = self.figure.add_subplot(211)
        #ax1.hold(False)
        ax1.set_title("Field values vs Model o/p (Before Calibration)")
       # ax1.set_xlabel("Time Series")
        #ax1.set_ylabel("Output Values")
        #ax1.legend(bbox_to_anchor=(1.05, 0), loc='upper right', borderaxespad=0.)
        
        ax2 = self.figure.add_subplot(212)
        #ax2.hold(False)
        ax2.set_title("Field values vs Model o/p (After Calibration)")
        #ax2.set_xlabel("Time Series")
        #ax2.set_ylabel("Output Values")
        
        self.figure.text(0.5, 0.04, 'Time Series', ha='center', va='center')
        self.figure.text(0.06, 0.5, 'Output Values', ha='center', va='center', rotation='vertical')
        
        ax1.plot(data, data1, 'b',  label="SSS sfd")
        ax1.plot(data, data2, 'r', label='AAA')
        
        ax2.plot(data, data1, 'b', label = "SSS")
        ax2.plot(data, data2, 'r', label='AAA')
        
        #plt.figlegend([l1, l2, l3, l4], ['label1', 'label2', 'label1', 'label2'],
                           #'upper right')
        
        ax1.legend()
        
        ax2.legend()

        self.canvas.draw()
 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
 
    main = Window()
    main.setWindowTitle('Simple QTpy and MatplotLib example with Zoom/Pan')
    main.show()
 
    sys.exit(app.exec_())