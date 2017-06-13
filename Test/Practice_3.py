import pyqtgraph as pg
### for white background #####
pg.setConfigOption('background', 'w')  # first set background to white
pg.setConfigOption('foreground', 'k')
### create data to plot ######
from numpy import *
pi=3.1415
X=linspace(-10,10,100)
X1=linspace(-1,1,10);X11=linspace(-1,1,11)
Y=2+sin(X1);Y1=2+sin(X);
Y2=(cos(10*Y)/(X1+0.0131415))**2
Y3=cos(10*Y1)/(X+0.0131415)
Y4=4+sin(X)*cos(2*X)
###############################

##### plot two graphs in two windows ########
pg.plot(X,Y1)
# another graph
pg.plot(X,Y1,pen=(255,0,255),symbol='+')
# show
pg.QtGui.QApplication.exec_()

### plot two graphs on the same window ####
H=pg.plot(X,Y1)
# H.plot(X,Y1, pen='g')
H.plot(1.1*X,sqrt(Y1), pen='r')
# show
pg.QtGui.QApplication.exec_()

##### make a window with multiple graphs ####
win= pg.GraphicsWindow(title="subplot window") # make the window
p=win.addPlot(title="fig 1")
p.plot(X,Y1, pen='b')
p.plot(1.1*X, sqrt(Y1), pen='r')

p=win.addPlot(title="fig 2")
p.plot(X,Y4, pen='b')
p.plot(1.1*X, sqrt(Y1), pen='g')
'''

# add axis labels
p.setLabel('left','Y axis text',labelStyle = {'font-size': '48pt'})
p.setLabel('bottom','X axis text',labelStyle = {'font-size': '48pt'})
win.nextRow() # go down one row in the window
p=win.addPlot(title="fig 3");p.plot(X,Y3)
curve=pg.PlotCurveItem(X11,Y2,stepMode=True,fillLevel=0, brush=(0, 0, 255, 80))
p=win.addPlot(title="fig 4");p.addItem(curve)
'''
# show
pg.QtGui.QApplication.exec_()

