# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectMiscSettingsDialog.ui'
#
# Created: Wed Oct 25 13:21:06 2017
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_ProjectMiscSettingsDialog(object):
    def setupUi(self, ProjectMiscSettingsDialog):
        ProjectMiscSettingsDialog.setObjectName(_fromUtf8("ProjectMiscSettingsDialog"))
        ProjectMiscSettingsDialog.resize(802, 416)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProjectMiscSettingsDialog.sizePolicy().hasHeightForWidth())
        ProjectMiscSettingsDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectMiscSettingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(ProjectMiscSettingsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditControllerLoopCycleTime = QtGui.QLineEdit(ProjectMiscSettingsDialog)
        self.lineEditControllerLoopCycleTime.setObjectName(_fromUtf8("lineEditControllerLoopCycleTime"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditControllerLoopCycleTime)
        self.label_3 = QtGui.QLabel(ProjectMiscSettingsDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditPathToControllerCodeFolder = QtGui.QLineEdit(ProjectMiscSettingsDialog)
        self.lineEditPathToControllerCodeFolder.setObjectName(_fromUtf8("lineEditPathToControllerCodeFolder"))
        self.horizontalLayout_3.addWidget(self.lineEditPathToControllerCodeFolder)
        self.toolButtonSelectControllerCodeFolder = QtGui.QToolButton(ProjectMiscSettingsDialog)
        self.toolButtonSelectControllerCodeFolder.setObjectName(_fromUtf8("toolButtonSelectControllerCodeFolder"))
        self.horizontalLayout_3.addWidget(self.toolButtonSelectControllerCodeFolder)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_4 = QtGui.QLabel(ProjectMiscSettingsDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBoxFrameworkAndInterface = QtGui.QComboBox(ProjectMiscSettingsDialog)
        self.comboBoxFrameworkAndInterface.setObjectName(_fromUtf8("comboBoxFrameworkAndInterface"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxFrameworkAndInterface)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.portChangedLabel = QtGui.QLabel(ProjectMiscSettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portChangedLabel.setFont(font)
        self.portChangedLabel.setObjectName(_fromUtf8("portChangedLabel"))
        self.verticalLayout.addWidget(self.portChangedLabel)
        self.groupBoxUdp = QtGui.QGroupBox(ProjectMiscSettingsDialog)
        self.groupBoxUdp.setObjectName(_fromUtf8("groupBoxUdp"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBoxUdp)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBoxUdp)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditComputerIP = QtGui.QLineEdit(self.groupBoxUdp)
        self.lineEditComputerIP.setReadOnly(True)
        self.lineEditComputerIP.setObjectName(_fromUtf8("lineEditComputerIP"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditComputerIP)
        self.label_6 = QtGui.QLabel(self.groupBoxUdp)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditControllerIP = QtGui.QLineEdit(self.groupBoxUdp)
        self.lineEditControllerIP.setReadOnly(True)
        self.lineEditControllerIP.setObjectName(_fromUtf8("lineEditControllerIP"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditControllerIP)
        self.label_7 = QtGui.QLabel(self.groupBoxUdp)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditUDPPort = QtGui.QLineEdit(self.groupBoxUdp)
        self.lineEditUDPPort.setReadOnly(True)
        self.lineEditUDPPort.setObjectName(_fromUtf8("lineEditUDPPort"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditUDPPort)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBoxUdp)
        self.groupBoxSerial = QtGui.QGroupBox(ProjectMiscSettingsDialog)
        self.groupBoxSerial.setObjectName(_fromUtf8("groupBoxSerial"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBoxSerial)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.groupBoxSerial)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.comboBoxComPort = QtGui.QComboBox(self.groupBoxSerial)
        self.comboBoxComPort.setObjectName(_fromUtf8("comboBoxComPort"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxComPort)
        self.label = QtGui.QLabel(self.groupBoxSerial)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBoxBaudRate = QtGui.QComboBox(self.groupBoxSerial)
        self.comboBoxBaudRate.setObjectName(_fromUtf8("comboBoxBaudRate"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxBaudRate)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.verticalLayout.addWidget(self.groupBoxSerial)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(ProjectMiscSettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProjectMiscSettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(ProjectMiscSettingsDialog)

    def retranslateUi(self, ProjectMiscSettingsDialog):
        ProjectMiscSettingsDialog.setWindowTitle(_translate("ProjectMiscSettingsDialog", "Projekteinstellungen", None))
        self.label_2.setText(_translate("ProjectMiscSettingsDialog", "Controller loop cycle time in us", None))
        self.label_3.setText(_translate("ProjectMiscSettingsDialog", "path to controller code folder", None))
        self.toolButtonSelectControllerCodeFolder.setText(_translate("ProjectMiscSettingsDialog", "...", None))
        self.label_4.setText(_translate("ProjectMiscSettingsDialog", "Framework and interface", None))
        self.portChangedLabel.setText(_translate("ProjectMiscSettingsDialog", "original port lost, alternatives are available", None))
        self.groupBoxUdp.setTitle(_translate("ProjectMiscSettingsDialog", "Framework and interface settings", None))
        self.label_5.setText(_translate("ProjectMiscSettingsDialog", "computer IP", None))
        self.label_6.setText(_translate("ProjectMiscSettingsDialog", "controller IP", None))
        self.label_7.setText(_translate("ProjectMiscSettingsDialog", "UDP Port", None))
        self.groupBoxSerial.setTitle(_translate("ProjectMiscSettingsDialog", "Framework and interface settings", None))
        self.label_8.setText(_translate("ProjectMiscSettingsDialog", "Com Port", None))
        self.label.setText(_translate("ProjectMiscSettingsDialog", "BaudRate", None))

