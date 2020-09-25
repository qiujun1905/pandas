# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogTongji.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_tongji(object):
    def setupUi(self, dialog_tongji):
        dialog_tongji.setObjectName("dialog_tongji")
        dialog_tongji.resize(235, 128)
        dialog_tongji.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dialog_tongji)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(dialog_tongji)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)

        self.retranslateUi(dialog_tongji)
        QtCore.QMetaObject.connectSlotsByName(dialog_tongji)

    def retranslateUi(self, dialog_tongji):
        _translate = QtCore.QCoreApplication.translate
        dialog_tongji.setWindowTitle(_translate("dialog_tongji", "班次产量统计"))
