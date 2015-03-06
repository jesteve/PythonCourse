# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'livescope_ui.ui'
#
# Created: Thu Mar  5 10:56:56 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(570, 384)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.qwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.verticalLayout.addWidget(self.qwtPlot)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Start = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Start.setObjectName(_fromUtf8("pushButton_Start"))
        self.horizontalLayout.addWidget(self.pushButton_Start)
        self.pushButton_Stop = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Stop.setObjectName(_fromUtf8("pushButton_Stop"))
        self.horizontalLayout.addWidget(self.pushButton_Stop)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Save = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Save.setObjectName(_fromUtf8("pushButton_Save"))
        self.horizontalLayout.addWidget(self.pushButton_Save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Livescope", None))
        self.pushButton_Start.setText(_translate("MainWindow", "Start", None))
        self.pushButton_Stop.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_Save.setText(_translate("MainWindow", "Save", None))

from PyQt4 import Qwt5
