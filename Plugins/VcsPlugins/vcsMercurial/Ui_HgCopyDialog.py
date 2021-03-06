# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/HgCopyDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgCopyDialog(object):
    def setupUi(self, HgCopyDialog):
        HgCopyDialog.setObjectName("HgCopyDialog")
        HgCopyDialog.resize(409, 138)
        HgCopyDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgCopyDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtWidgets.QLabel(HgCopyDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.sourceEdit = QtWidgets.QLineEdit(HgCopyDialog)
        self.sourceEdit.setReadOnly(True)
        self.sourceEdit.setObjectName("sourceEdit")
        self.gridlayout.addWidget(self.sourceEdit, 0, 1, 1, 1)
        self.targetEdit = QtWidgets.QLineEdit(HgCopyDialog)
        self.targetEdit.setObjectName("targetEdit")
        self.gridlayout.addWidget(self.targetEdit, 1, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(HgCopyDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.dirButton = QtWidgets.QToolButton(HgCopyDialog)
        self.dirButton.setObjectName("dirButton")
        self.gridlayout.addWidget(self.dirButton, 1, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.forceCheckBox = QtWidgets.QCheckBox(HgCopyDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.vboxlayout.addWidget(self.forceCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgCopyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgCopyDialog)
        self.buttonBox.accepted.connect(HgCopyDialog.accept)
        self.buttonBox.rejected.connect(HgCopyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgCopyDialog)
        HgCopyDialog.setTabOrder(self.targetEdit, self.dirButton)
        HgCopyDialog.setTabOrder(self.dirButton, self.forceCheckBox)
        HgCopyDialog.setTabOrder(self.forceCheckBox, self.buttonBox)
        HgCopyDialog.setTabOrder(self.buttonBox, self.sourceEdit)

    def retranslateUi(self, HgCopyDialog):
        _translate = QtCore.QCoreApplication.translate
        HgCopyDialog.setWindowTitle(_translate("HgCopyDialog", "Mercurial Copy"))
        self.textLabel1.setText(_translate("HgCopyDialog", "Source:"))
        self.sourceEdit.setToolTip(_translate("HgCopyDialog", "Shows the name of the source"))
        self.sourceEdit.setWhatsThis(_translate("HgCopyDialog", "<b>Source name</b>\n"
"<p>This field shows the name of the source.</p>"))
        self.targetEdit.setToolTip(_translate("HgCopyDialog", "Enter the target name"))
        self.targetEdit.setWhatsThis(_translate("HgCopyDialog", "<b>Target name</b>\n"
"<p>Enter the new name in this field. The target must be the new name or an absolute path.</p>"))
        self.textLabel2.setText(_translate("HgCopyDialog", "Target:"))
        self.dirButton.setToolTip(_translate("HgCopyDialog", "Press to open a selection dialog"))
        self.dirButton.setWhatsThis(_translate("HgCopyDialog", "<b>Target directory</b>\n"
"<p>Select the target name for the operation via a selection dialog.</p>"))
        self.forceCheckBox.setToolTip(_translate("HgCopyDialog", "Select to force the operation"))
        self.forceCheckBox.setText(_translate("HgCopyDialog", "Enforce operation"))

