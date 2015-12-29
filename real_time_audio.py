import time
import ui_plot
import sys
import numpy
from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from recorder import *

gBigValue = 1000

def plotSomething():
    if SR.newAudio==False: 
        return
    xs,ys=SR.fft()
    c.setData(xs,ys)
    uiplot.qwtPlot.replot()
    SR.newAudio=False
    if len(ys) > 0 and ys[0] > gBigValue: 
        print time.strftime("%I:%M:%S %p  %B %d"), "    ", int(ys[0])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if isinstance(int(sys.argv[1]), int):
            gBigValue = int(sys.argv[1])
        else:
            print "Not an integer value...\nTerminated."
            sys.exit()
    print "Disturbances greater than ", gBigValue, "at time..."
    print "\n           Time               Value"
    print "------------------------      -----" 
    app = QtGui.QApplication(sys.argv)
    
    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_win_plot()
    uiplot.setupUi(win_plot)
    uiplot.btnA.clicked.connect(plotSomething)
    #uiplot.btnB.clicked.connect(lambda: uiplot.timer.setInterval(100.0))
    #uiplot.btnC.clicked.connect(lambda: uiplot.timer.setInterval(10.0))
    #uiplot.btnD.clicked.connect(lambda: uiplot.timer.setInterval(1.0))
    c=Qwt.QwtPlotCurve()  
    c.attach(uiplot.qwtPlot)
    
    uiplot.qwtPlot.setAxisScale(uiplot.qwtPlot.yLeft, 0, 10000)
    
    uiplot.timer = QtCore.QTimer()
    uiplot.timer.start(1.0)
    
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething) 
    
    SR=SwhRecorder()
    SR.setup()
    SR.continuousStart()

    ### DISPLAY WINDOWS
    win_plot.show()
    code=app.exec_()
    SR.close()
    sys.exit(code)
