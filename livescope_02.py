#!/usr/bin/env python
import sys
import time
from PyQt4 import Qwt5, QtCore, QtGui, Qt
from livescope_ui import Ui_MainWindow
from lecroy.scope import LecroyScope

scope_address = 'localhost'

class AcquisitionThread(QtCore.QThread):
    def __init__(self, fun):
        super(AcquisitionThread, self).__init__()
        self.fun = fun
    def run(self):
        self.fun()

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
        # Acquisition thread
        self.acquisition_thread = AcquisitionThread(self.acquire)
        self.acquiring = False

    @QtCore.pyqtSignature("")
    def on_pushButton_Start_clicked(self):
        if not self.acquiring:
            # Start acquisition
            self.acquisition_thread.finished.connect(self.callback)
            self.acquisition_thread.start()
            self.acquiring = True

    @QtCore.pyqtSignature("")
    def on_pushButton_Stop_clicked(self):
        if self.acquiring:
            # Stop acquisition
            self.acquisition_thread.finished.disconnect(self.callback)
            self.acquiring = False

    def acquire(self):
        time.sleep(0.1)
        self.last_trace = self.scope.fetchwaveform(1)

    def callback(self):
        self.plot(*self.last_trace)
        self.acquisition_thread.start()

    def plot(self, x, y):
        self.curve.setData(x, y)
        self.ui.qwtPlot.replot()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
