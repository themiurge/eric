# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/CorbaPage.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CorbaPage(object):
    def setupUi(self, CorbaPage):
        CorbaPage.setObjectName("CorbaPage")
        CorbaPage.resize(589, 490)
        self.vboxlayout = QtWidgets.QVBoxLayout(CorbaPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(CorbaPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line13 = QtWidgets.QFrame(CorbaPage)
        self.line13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line13.setObjectName("line13")
        self.vboxlayout.addWidget(self.line13)
        self.groupBox = QtWidgets.QGroupBox(CorbaPage)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.idlEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idlEdit.setObjectName("idlEdit")
        self.gridlayout.addWidget(self.idlEdit, 0, 0, 1, 1)
        self.textLabel1_4 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridlayout.addWidget(self.textLabel1_4, 1, 0, 1, 2)
        self.idlButton = QtWidgets.QToolButton(self.groupBox)
        self.idlButton.setObjectName("idlButton")
        self.gridlayout.addWidget(self.idlButton, 0, 1, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(CorbaPage)
        QtCore.QMetaObject.connectSlotsByName(CorbaPage)
        CorbaPage.setTabOrder(self.idlEdit, self.idlButton)

    def retranslateUi(self, CorbaPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("CorbaPage", "<b>Configure CORBA support</b>"))
        self.groupBox.setTitle(_translate("CorbaPage", "IDL Compiler"))
        self.idlEdit.setToolTip(_translate("CorbaPage", "Enter the path to the IDL compiler."))
        self.textLabel1_4.setText(_translate("CorbaPage", "<b>Note:</b> Leave this entry empty to use the default value (omniidl or omniidl.exe)."))
        self.idlButton.setToolTip(_translate("CorbaPage", "Press to select the IDL compiler via a file selection dialog."))

