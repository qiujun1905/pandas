# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZhuisuoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZhuisuoDialog(object):
    def setupUi(self, ZhuisuoDialog):
        ZhuisuoDialog.setObjectName("ZhuisuoDialog")
        ZhuisuoDialog.resize(881, 576)
        self.verticalLayout = QtWidgets.QVBoxLayout(ZhuisuoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(ZhuisuoDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableView = QtWidgets.QTableView(self.frame_2)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_3.addWidget(self.tableView)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(ZhuisuoDialog)
        QtCore.QMetaObject.connectSlotsByName(ZhuisuoDialog)

    def retranslateUi(self, ZhuisuoDialog):
        _translate = QtCore.QCoreApplication.translate
        ZhuisuoDialog.setWindowTitle(_translate("ZhuisuoDialog", "追溯"))
        self.label.setText(_translate("ZhuisuoDialog", "一物一码"))
        self.pushButton.setText(_translate("ZhuisuoDialog", "追溯"))
