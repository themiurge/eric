# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Debugger/VariablesFilterDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VariablesFilterDialog(object):
    def setupUi(self, VariablesFilterDialog):
        VariablesFilterDialog.setObjectName("VariablesFilterDialog")
        VariablesFilterDialog.resize(386, 338)
        VariablesFilterDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(VariablesFilterDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(VariablesFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.localsLabel = QtWidgets.QLabel(VariablesFilterDialog)
        self.localsLabel.setObjectName("localsLabel")
        self.gridlayout.addWidget(self.localsLabel, 0, 0, 1, 1)
        self.globalsLabel = QtWidgets.QLabel(VariablesFilterDialog)
        self.globalsLabel.setObjectName("globalsLabel")
        self.gridlayout.addWidget(self.globalsLabel, 0, 1, 1, 1)
        self.localsList = QtWidgets.QListWidget(VariablesFilterDialog)
        self.localsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localsList.setObjectName("localsList")
        self.gridlayout.addWidget(self.localsList, 1, 0, 1, 1)
        self.globalsList = QtWidgets.QListWidget(VariablesFilterDialog)
        self.globalsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.globalsList.setObjectName("globalsList")
        self.gridlayout.addWidget(self.globalsList, 1, 1, 1, 1)
        self.localsLabel.setBuddy(self.localsList)
        self.globalsLabel.setBuddy(self.globalsList)

        self.retranslateUi(VariablesFilterDialog)
        self.buttonBox.accepted.connect(VariablesFilterDialog.accept)
        self.buttonBox.rejected.connect(VariablesFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VariablesFilterDialog)
        VariablesFilterDialog.setTabOrder(self.localsList, self.globalsList)

    def retranslateUi(self, VariablesFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        VariablesFilterDialog.setWindowTitle(_translate("VariablesFilterDialog", "Variables Type Filter"))
        VariablesFilterDialog.setWhatsThis(_translate("VariablesFilterDialog", "<b>Filter Dialog</b>\n"
"<p> This dialog gives the user the possibility to select what kind of variables should <b>not</b> be shown during a debugging session.</p>"))
        self.localsLabel.setText(_translate("VariablesFilterDialog", "&Locals Filter"))
        self.globalsLabel.setText(_translate("VariablesFilterDialog", "&Globals Filter"))
        self.localsList.setToolTip(_translate("VariablesFilterDialog", "Locals Filter List"))
        self.localsList.setWhatsThis(_translate("VariablesFilterDialog", "<b>Locals Filter List</b>\n"
"<p>Select the variable types you want to be filtered out of the locals variables list.</p<"))
        self.globalsList.setToolTip(_translate("VariablesFilterDialog", "Globals Filter List"))
        self.globalsList.setWhatsThis(_translate("VariablesFilterDialog", "<b>Globals Filter List</b>\n"
"<p>Select the variable types you want to be filtered out of the globals variables list.</p<"))

