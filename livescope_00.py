#!/usr/bin/env python
import sys
from PyQt4 import Qwt5, QtCore, QtGui, Qt
from livescope_ui import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        # Create the main window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @QtCore.pyqtSignature("")
    def on_pushButton_Start_clicked(self):
        print 'Clic !'

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
