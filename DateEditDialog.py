# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DateEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Date_Edit(object):
    def setupUi(self, Dialog_Date_Edit):
        Dialog_Date_Edit.setObjectName("Dialog_Date_Edit")
        Dialog_Date_Edit.resize(526, 244)
        Dialog_Date_Edit.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Date_Edit)
        self.buttonBox.setGeometry(QtCore.QRect(360, 220, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog_Date_Edit)
        self.widget.setGeometry(QtCore.QRect(10, 10, 504, 199))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget_b = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget_b.setObjectName("calendarWidget_b")
        self.horizontalLayout.addWidget(self.calendarWidget_b)
        self.calendarWidget_a = QtWidgets.QCalendarWidget(self.widget)
        self.calendarWidget_a.setObjectName("calendarWidget_a")
        self.horizontalLayout.addWidget(self.calendarWidget_a)

        self.retranslateUi(Dialog_Date_Edit)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Date_Edit)

    def retranslateUi(self, Dialog_Date_Edit):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Date_Edit.setWindowTitle(_translate("Dialog_Date_Edit", "时间范围选择"))
