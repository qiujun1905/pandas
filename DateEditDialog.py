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
        Dialog_Date_Edit.resize(266, 244)
        Dialog_Date_Edit.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Date_Edit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog_Date_Edit)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Date_Edit)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_Date_Edit)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Date_Edit)

    def retranslateUi(self, Dialog_Date_Edit):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Date_Edit.setWindowTitle(_translate("Dialog_Date_Edit", "Calendar"))
