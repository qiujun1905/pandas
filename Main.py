import sys

import pandas
from PyQt5.QtCore import pyqtSignal, Qt, QThread, QAbstractTableModel, QObject
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import *

from DateEditDialog import Ui_Dialog_Date_Edit
from DialogTongji import Ui_dialog_tongji
from MainWindow import Ui_MainWindow
from crawl import Crawl
from dialog_login import Ui_Dialog_Login


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class DialogTongji(QDialog, Ui_dialog_tongji):
    def __init__(self, parent=None):
        super(DialogTongji, self).__init__(parent)
        self.setupUi(self)

        mainUI.pass_tongji_signal.connect(self.get_sum)

    def get_sum(self, df):
        model = pandasModel(df)
        # ****************************************开始

        # ****************************************结束
        # headers = ['班次', '总数量',]
        # item_names = ['classes', 'weight_unit']
        # for i, r in df.iterrows():
        #     print(i, '-->', r)
        #     for j in r:
        #         print("---->",j)
        # model.setHorizontalHeaderLabels(headers)
        # for i, v in enumerate(self.datas):
        #     for index, itemname in enumerate(item_names):
        #         self.model.setItem(i, index, QStandardItem(v[itemname]))
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(model)
        tongji_ui.show()
        # tongji_ui.tableView.setModel()

# 时间选择框
class DateEdit(QDialog, Ui_Dialog_Date_Edit):
    def __init__(self, parent=None):
        super(DateEdit, self).__init__(parent)
        self.setupUi(self)
        # 点击dialog的ok按钮触发的事件
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.writeback)

        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.writeback)
        mainUI.passControlSignal.connect(self.getEdit)


        # self.move()

    def getEdit(self, edit):
        self.currentEdit = edit


    def writeback(self, edit):
        print("=====================>" + str(edit))
        calendar = self.calendarWidget.selectedDate().toString("yyyy.MM.dd")
        self.currentEdit.setText(calendar)
        print(calendar)
        self.close()

    def closeSelf(self):
        self.close()

# mainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):
    passControlSignal = pyqtSignal(QLineEdit)
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1024, 600)
        self.center()
        self.setFixedSize(self.width(), self.height())
        self.lineEdit_time_cr_before.clicked.connect(self.timeEidtClicked)
        self.lineEdit_time_cr_after.clicked.connect(self.timeEidtClicked)
        self.btn_search.clicked.connect(self.seacth)

        self.btn_tongji.clicked.connect(self.sum)
        self.actiontuichu.triggered.connect(app.quit)
        self.model = QSqlQueryModel()
        self.datas = []

        # self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.setWindowOpacity(0.8)

    def setText(self):
        self.lineEdit_page.setText("0")

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def timeEidtClicked(self, edit):
        print("========>" + str(edit))
        dateEditDialog.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(dateEditDialog.writeback)
        dateEditDialog.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(dateEditDialog.closeSelf)
        self.passControlSignal.emit(edit)
        dateEditDialog.move(dateEditDialog.currentEdit.x()+mainUI.x(), mainUI.y()
                            +dateEditDialog.currentEdit.y()+dateEditDialog.currentEdit.height()+54)
        dateEditDialog.show()

    pass_tongji_signal = pyqtSignal(pandas.DataFrame)

    def sum(self):
        df = pandas.DataFrame(self.datas)
        df['weight_unit'] = df['weight_unit'].str[0:-1].str.replace(',', '')
        df['weight_unit'] = df['weight_unit'].astype(float)
        df = df.groupby(['classes'])['weight_unit'].sum().reset_index()
        print(df)
        self.pass_tongji_signal.emit(df)


    def seacth(self):
        search = Search_Data({})
        search.start()
        self.statusbar.showMessage("正在查询中...")
        search.display_signal.connect(self.fill_grid)

    def fill_grid(self, json):
        self.statusBar().showMessage("完成", 2000)
        self.datas = json['data']
        self.data_count = json['records']
        if len(self.datas) == 0:
            self.statusBar().showMessage('没有数据', 2000)
            return

        df = pandas.DataFrame(json['data'])
        model = pandasModel(df)
        self.tableView.setModel(model)


# 爬取数据的线程
class Search_Data(QThread):
    display_signal = pyqtSignal(dict) ##此处定义了一个信号，可以用来与主程序交互
    # 通知表格刷新
    # notify_form_refresh_signal = pyqtSignal(str)
    def __init__(self, count):
        super().__init__()  ## 继承QThread
        self.count = count ## 取出主程序传过来的参数name

    def run(self):
        qrcode_id = mainUI.lineEdit_qrcode_id.text()
        index = mainUI.comboBox_process.currentIndex()
        process = (index + 1) * 10
        time_range = mainUI.lineEdit_time_cr_before.text() + \
                      "~" + mainUI.lineEdit_time_cr_after.text()

        json = loginUI.crawl.search(time_range, process=process, qrcode_id=qrcode_id)
        self.display_signal.emit(json)
        mainUI.btn_tongji.setEnabled(True)

# 登录窗口
class LoginUI(QDialog, Ui_Dialog_Login):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.crawl = Crawl()
        self.setupUi(self)
        self.center()
        self.setCapcha()
        self.btn_login.clicked.connect(self.login)  # 按钮事件绑定
        self.pushButton_shuaxin.clicked.connect(self.setCapcha)


    def setCapcha(self):
        captchaBytes = self.crawl.get_captcha()

        print(self.crawl.session)
        pixmap = QPixmap()
        pixmap.loadFromData(captchaBytes)
        self.label_captcha.setPixmap(pixmap)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


    # 登录
    def login(self):
        name = self.lineEdit_name.text()
        password = self.lineEdit_password.text()
        captcha = self.lineEdit_capcha.text()
        loginTitle = self.crawl.login(name, password, captcha)
        print(self.crawl.session)
        if loginTitle == '登录成功':
            self.close()
            mainUI.show()
            print("mainUI..x()--------->" + str(mainUI.lineEdit_time_cr_before.geometry().x()))
            print("mainUI.y()--------->" + str(mainUI.lineEdit_time_cr_before.geometry().y()))
            print("mainUI.horizontalLayout.x()--------->" + str(mainUI.horizontalLayout.geometry().x()))
            print("mainUI.horizontalLayout.y()--------->" + str(mainUI.horizontalLayout.geometry().y()))
        else:
            self.lineEdit_capcha.clear()
            QMessageBox.information(self, '提示', loginTitle)
            self.setCapcha()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginUI = LoginUI()

    mainUI = MyMainWindow()

    dateEditDialog = DateEdit(mainUI)

    tongji_ui = DialogTongji()

    loginUI.show()
    sys.exit(app.exec_())


