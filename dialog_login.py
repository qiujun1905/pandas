# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Login(object):
    def setupUi(self, Dialog_Login):
        Dialog_Login.setObjectName("Dialog_Login")
        Dialog_Login.resize(400, 250)
        Dialog_Login.setMinimumSize(QtCore.QSize(400, 250))
        Dialog_Login.setMaximumSize(QtCore.QSize(400, 250))
        self.layoutWidget = QtWidgets.QWidget(Dialog_Login)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 10, 281, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_login = QtWidgets.QLabel(self.layoutWidget)
        self.label_login.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(43)
        self.label_login.setFont(font)
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.verticalLayout.addWidget(self.label_login)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(30, 32))
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit_name.setMaximumSize(QtCore.QSize(300, 32))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 32))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(200, 32))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(300, 32))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 32))
        self.label_3.setMaximumSize(QtCore.QSize(40, 32))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_capcha = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_capcha.setMinimumSize(QtCore.QSize(70, 32))
        self.lineEdit_capcha.setMaximumSize(QtCore.QSize(100, 32))
        self.lineEdit_capcha.setText("")
        self.lineEdit_capcha.setObjectName("lineEdit_capcha")
        self.horizontalLayout.addWidget(self.lineEdit_capcha)
        self.label_captcha = QtWidgets.QLabel(self.layoutWidget)
        self.label_captcha.setMinimumSize(QtCore.QSize(75, 32))
        self.label_captcha.setMaximumSize(QtCore.QSize(75, 32))
        self.label_captcha.setText("")
        self.label_captcha.setObjectName("label_captcha")
        self.horizontalLayout.addWidget(self.label_captcha)
        self.pushButton_shuaxin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_shuaxin.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_shuaxin.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_shuaxin.setObjectName("pushButton_shuaxin")
        self.horizontalLayout.addWidget(self.pushButton_shuaxin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_login = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_login.setMinimumSize(QtCore.QSize(242, 30))
        self.btn_login.setMaximumSize(QtCore.QSize(400, 30))
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)

        self.retranslateUi(Dialog_Login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Login)

    def retranslateUi(self, Dialog_Login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Login.setWindowTitle(_translate("Dialog_Login", "车间生产数据统计工具"))
        self.label_login.setText(_translate("Dialog_Login", "登录"))
        self.label.setText(_translate("Dialog_Login", "用户名"))
        self.lineEdit_name.setText(_translate("Dialog_Login", "hbwj@zhedao.net"))
        self.lineEdit_name.setPlaceholderText(_translate("Dialog_Login", "请输用户名"))
        self.label_2.setText(_translate("Dialog_Login", "密  码"))
        self.lineEdit_password.setText(_translate("Dialog_Login", "hbwj@2020"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog_Login", "请输入密码"))
        self.label_3.setText(_translate("Dialog_Login", "验证码"))
        self.lineEdit_capcha.setPlaceholderText(_translate("Dialog_Login", "验证码"))
        self.pushButton_shuaxin.setText(_translate("Dialog_Login", "刷新"))
        self.btn_login.setText(_translate("Dialog_Login", "登录"))
