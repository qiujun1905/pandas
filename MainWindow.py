# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1004, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_process = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_process.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_process.setObjectName("comboBox_process")
        self.comboBox_process.addItem("")
        self.comboBox_process.addItem("")
        self.comboBox_process.addItem("")
        self.comboBox_process.addItem("")
        self.comboBox_process.addItem("")
        self.comboBox_process.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_process)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_time_cr = MyLineEdit(self.centralwidget)
        self.lineEdit_time_cr.setObjectName("lineEdit_time_cr")
        self.horizontalLayout.addWidget(self.lineEdit_time_cr)
        self.pushButton_class = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_class.setEnabled(False)
        self.pushButton_class.setObjectName("pushButton_class")
        self.horizontalLayout.addWidget(self.pushButton_class)
        self.btn_tongji = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tongji.setEnabled(False)
        self.btn_tongji.setObjectName("btn_tongji")
        self.horizontalLayout.addWidget(self.btn_tongji)
        self.pushButton_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export.setEnabled(False)
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout.addWidget(self.pushButton_export)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setToolTip("")
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_show_count = QtWidgets.QLabel(self.centralwidget)
        self.label_show_count.setText("")
        self.label_show_count.setObjectName("label_show_count")
        self.horizontalLayout_2.addWidget(self.label_show_count)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_rows = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_rows.setEnabled(True)
        self.comboBox_rows.setMinimumSize(QtCore.QSize(50, 0))
        self.comboBox_rows.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_rows.setObjectName("comboBox_rows")
        self.comboBox_rows.addItem("")
        self.comboBox_rows.addItem("")
        self.comboBox_rows.addItem("")
        self.comboBox_rows.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_rows)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.pushButton_shang = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shang.setEnabled(False)
        self.pushButton_shang.setObjectName("pushButton_shang")
        self.horizontalLayout_2.addWidget(self.pushButton_shang)
        self.label_current_page = QtWidgets.QLabel(self.centralwidget)
        self.label_current_page.setMinimumSize(QtCore.QSize(30, 0))
        self.label_current_page.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_current_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_page.setObjectName("label_current_page")
        self.horizontalLayout_2.addWidget(self.label_current_page)
        self.pushButton_xia = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_xia.setEnabled(False)
        self.pushButton_xia.setObjectName("pushButton_xia")
        self.horizontalLayout_2.addWidget(self.pushButton_xia)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.actionzhuisuo = QtWidgets.QAction(MainWindow)
        self.actionzhuisuo.setObjectName("actionzhuisuo")
        self.menu.addAction(self.actionzhuisuo)
        self.menu.addAction(self.actiontuichu)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "车间生产统计工具"))
        self.label.setText(_translate("MainWindow", "选择工序"))
        self.comboBox_process.setItemText(0, _translate("MainWindow", "工序：全部工序"))
        self.comboBox_process.setItemText(1, _translate("MainWindow", "工序：水刺 | 编码：10"))
        self.comboBox_process.setItemText(2, _translate("MainWindow", "工序：脱漂烘干 | 编码：20"))
        self.comboBox_process.setItemText(3, _translate("MainWindow", "工序：检布（验布） | 编码：30"))
        self.comboBox_process.setItemText(4, _translate("MainWindow", "工序：分切 | 编码：40"))
        self.comboBox_process.setItemText(5, _translate("MainWindow", "工序：分切覆膜 | 编码：50"))
        self.label_3.setText(_translate("MainWindow", "赋码时间范围"))
        self.pushButton_class.setText(_translate("MainWindow", "班次统计"))
        self.btn_tongji.setText(_translate("MainWindow", "订单号统计"))
        self.pushButton_export.setText(_translate("MainWindow", "导出"))
        self.label_5.setText(_translate("MainWindow", "每页"))
        self.comboBox_rows.setItemText(0, _translate("MainWindow", "20"))
        self.comboBox_rows.setItemText(1, _translate("MainWindow", "50"))
        self.comboBox_rows.setItemText(2, _translate("MainWindow", "100"))
        self.comboBox_rows.setItemText(3, _translate("MainWindow", "1000"))
        self.label_6.setText(_translate("MainWindow", "条"))
        self.pushButton_shang.setText(_translate("MainWindow", "上一页"))
        self.label_current_page.setText(_translate("MainWindow", "1"))
        self.pushButton_xia.setText(_translate("MainWindow", "下一页"))
        self.menu.setTitle(_translate("MainWindow", "操作"))
        self.actiontuichu.setText(_translate("MainWindow", "退出"))
        self.actionzhuisuo.setText(_translate("MainWindow", "&z追溯"))
from Custom import MyLineEdit
