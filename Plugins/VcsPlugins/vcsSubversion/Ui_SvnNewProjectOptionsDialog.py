# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsSubversion/SvnNewProjectOptionsDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnNewProjectOptionsDialog(object):
    def setupUi(self, SvnNewProjectOptionsDialog):
        SvnNewProjectOptionsDialog.setObjectName("SvnNewProjectOptionsDialog")
        SvnNewProjectOptionsDialog.resize(562, 201)
        SvnNewProjectOptionsDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnNewProjectOptionsDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.vcsTagEdit = QtWidgets.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsTagEdit.setObjectName("vcsTagEdit")
        self.gridlayout.addWidget(self.vcsTagEdit, 2, 1, 1, 1)
        self.protocolCombo = QtWidgets.QComboBox(SvnNewProjectOptionsDialog)
        self.protocolCombo.setObjectName("protocolCombo")
        self.gridlayout.addWidget(self.protocolCombo, 0, 1, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vcsUrlEdit = QtWidgets.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsUrlEdit.setObjectName("vcsUrlEdit")
        self.gridlayout.addWidget(self.vcsUrlEdit, 1, 1, 1, 1)
        self.vcsUrlLabel = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.vcsUrlLabel.setObjectName("vcsUrlLabel")
        self.gridlayout.addWidget(self.vcsUrlLabel, 1, 0, 1, 1)
        self.vcsProjectDirEdit = QtWidgets.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsProjectDirEdit.setObjectName("vcsProjectDirEdit")
        self.gridlayout.addWidget(self.vcsProjectDirEdit, 3, 1, 1, 1)
        self.layoutCheckBox = QtWidgets.QCheckBox(SvnNewProjectOptionsDialog)
        self.layoutCheckBox.setChecked(True)
        self.layoutCheckBox.setObjectName("layoutCheckBox")
        self.gridlayout.addWidget(self.layoutCheckBox, 4, 0, 1, 2)
        self.TextLabel4 = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.TextLabel4.setObjectName("TextLabel4")
        self.gridlayout.addWidget(self.TextLabel4, 3, 0, 1, 1)
        self.vcsTagLabel = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.vcsTagLabel.setObjectName("vcsTagLabel")
        self.gridlayout.addWidget(self.vcsTagLabel, 2, 0, 1, 1)
        self.vcsUrlButton = QtWidgets.QToolButton(SvnNewProjectOptionsDialog)
        self.vcsUrlButton.setObjectName("vcsUrlButton")
        self.gridlayout.addWidget(self.vcsUrlButton, 1, 2, 1, 1)
        self.projectDirButton = QtWidgets.QToolButton(SvnNewProjectOptionsDialog)
        self.projectDirButton.setObjectName("projectDirButton")
        self.gridlayout.addWidget(self.projectDirButton, 3, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnNewProjectOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.protocolCombo)
        self.vcsUrlLabel.setBuddy(self.vcsUrlEdit)
        self.TextLabel4.setBuddy(self.vcsProjectDirEdit)
        self.vcsTagLabel.setBuddy(self.vcsTagEdit)

        self.retranslateUi(SvnNewProjectOptionsDialog)
        self.buttonBox.accepted.connect(SvnNewProjectOptionsDialog.accept)
        self.buttonBox.rejected.connect(SvnNewProjectOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnNewProjectOptionsDialog)
        SvnNewProjectOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsUrlEdit, self.vcsUrlButton)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsUrlButton, self.vcsTagEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsTagEdit, self.vcsProjectDirEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsProjectDirEdit, self.projectDirButton)
        SvnNewProjectOptionsDialog.setTabOrder(self.projectDirButton, self.layoutCheckBox)

    def retranslateUi(self, SvnNewProjectOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnNewProjectOptionsDialog.setWindowTitle(_translate("SvnNewProjectOptionsDialog", "New Project from Repository"))
        SvnNewProjectOptionsDialog.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>New Project from Repository Dialog</b>\n"
"<p>Enter the various repository infos into the entry fields. These values are used, when the new project is retrieved from the repository. If the checkbox is selected, the URL must end in the project name. A repository layout with project/tags, project/branches and project/trunk will be assumed. In this case, you may enter a tag or branch, which must look like tags/tagname or branches/branchname. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>"))
        self.vcsTagEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the tag the new project should be generated from"))
        self.vcsTagEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>Tag in VCS</b>\n"
"<p>Enter the tag name the new project shall be generated from. Leave empty to retrieve the latest data from the repository.</p>"))
        self.protocolCombo.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select the protocol to access the repository"))
        self.textLabel1.setText(_translate("SvnNewProjectOptionsDialog", "&Protocol:"))
        self.vcsUrlEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the url path of the module in the repository (without protocol part)"))
        self.vcsUrlEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>URL</b><p>Enter the URL to the module. For a repository with standard layout, this must not contain the trunk, tags or branches part.</p>"))
        self.vcsUrlLabel.setText(_translate("SvnNewProjectOptionsDialog", "&URL:"))
        self.vcsProjectDirEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the directory of the new project."))
        self.vcsProjectDirEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>Project Directory</b>\n"
"<p>Enter the directory of the new project. It will be retrieved from \n"
"the repository and be placed in this directory.</p>"))
        self.layoutCheckBox.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select to indicate, that the repository has a standard layout (projectdir/trunk, projectdir/tags, projectdir/branches)"))
        self.layoutCheckBox.setText(_translate("SvnNewProjectOptionsDialog", "Repository has standard &layout"))
        self.layoutCheckBox.setShortcut(_translate("SvnNewProjectOptionsDialog", "Alt+L"))
        self.TextLabel4.setText(_translate("SvnNewProjectOptionsDialog", "Project &Directory:"))
        self.vcsTagLabel.setText(_translate("SvnNewProjectOptionsDialog", "&Tag:"))
        self.vcsUrlButton.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select the repository url via a directory selection dialog or the repository browser"))

