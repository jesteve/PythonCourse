#!/usr/bin/env python
import sys
import time
from PyQt4 import Qwt5, QtCore, QtGui, Qt
from livescope_ui import Ui_MainWindow
from lecroy.scope import LecroyScope

scope_address = 'localhost'

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # Create the main window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Setup the plot
        self.curve = Qwt5.QwtPlotCurve()
        self.curve.attach(self.ui.qwtPlot)
        # Connects to the scope
        self.scope = LecroyScope(scope_address)

    @QtCore.pyqtSignature("")
    def on_pushButton_Start_clicked(self):
        self.last_trace = self.scope.fetchwaveform(1)
        self.plot(*self.last_trace)

    def plot(self, x, y):
        self.curve.setData(x, y)
        self.ui.qwtPlot.replot()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
