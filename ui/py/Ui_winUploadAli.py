# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winUploadAli.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winUploadAli(object):
    def setupUi(self, winUploadAli):
        winUploadAli.setObjectName("winUploadAli")
        winUploadAli.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(winUploadAli)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSearchFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearchFile.setGeometry(QtCore.QRect(320, 420, 93, 28))
        self.btnSearchFile.setObjectName("btnSearchFile")
        winUploadAli.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(winUploadAli)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        winUploadAli.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(winUploadAli)
        self.statusbar.setObjectName("statusbar")
        winUploadAli.setStatusBar(self.statusbar)

        self.retranslateUi(winUploadAli)
        QtCore.QMetaObject.connectSlotsByName(winUploadAli)

    def retranslateUi(self, winUploadAli):
        _translate = QtCore.QCoreApplication.translate
        winUploadAli.setWindowTitle(_translate("winUploadAli", "MainWindow"))
        self.btnSearchFile.setText(_translate("winUploadAli", "查找目录"))
