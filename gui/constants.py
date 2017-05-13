# -*- encoding: utf-8 -*-
from PyQt4 import QtGui

AVAILABLE_FRAMEWORKS = [
    {"macroName": "MBED_2_UDP", "displayName": u"Mbed 2 UDP"},
    {"macroName": "MBED_2_SERIAL", "displayName": u"Mbed 2 Serial"},
    {"macroName": "MBED_OS_UDP", "displayName": u"Mbed OS UDP"},
    {"macroName": "MBED_OS_SERIAL", "displayName": u"Mbed OS Serial"},
    {"macroName": "ARDUINO_UDP", "displayName": u"Arduino UDP"},
    {"macroName": "ARDUINO_SERIAL", "displayName": u"Arduino Serial"}
]

PATH_TO_APPLICATION_SETTINGS = "applicationSettings.json"

CHECK_BOX_FONT = QtGui.QFont()
CHECK_BOX_FONT.setPointSize(8)

USER_INPUT_WARNING_COLOR = QtGui.QColor(255, 165, 0)
CONFIRMATION_TIMEOUT_WARNING_COLOR = QtGui.QColor(210, 0, 0)
# NEGATIVE_CONFIRMATION_WARNING_COLOR = QtGui.QColor(50, 200, 50)
NEGATIVE_CONFIRMATION_WARNING_COLOR = QtGui.QColor(210, 30, 0)

HOVER_COLOR = QtGui.QColor(200, 200, 200)
MOUSE_DOWN_COLOR = QtGui.QColor(150, 150, 150)

PENDING_VALUE_COLOR = QtGui.QColor(210, 0, 0)

CABLE_PEN = QtGui.QPen()
CABLE_PEN.setColor(QtGui.QColor(0, 0, 0))
CABLE_PEN.setCosmetic(True)
CABLE_PEN.setWidth(2)