import sys

import pandas
from PyQt5.QtCore import pyqtSignal, Qt, QThread, QAbstractTableModel, QUrl, pyqtSlot, QPoint, QPropertyAnimation
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import *

from DateEditDialog import Ui_Dialog_Date_Edit
from DialogTongji import Ui_dialog_tongji
from MainWindow import Ui_MainWindow
from crawl import Crawl
from dialog_login import Ui_Dialog_Login

def df_adjustment(df):
    df.loc[df['process'] == '10', 'process'] = '水刺'
    df.loc[df['process'] == '20', 'process'] = '脱漂烘干'
    df.loc[df['process'] == '30', 'process'] = '验布'
    df.loc[df['process'] == '40', 'process'] = '分切'
    df.loc[df['process'] == '50', 'process'] = '分切覆膜'
    # ********************调整列位置********************开始
    df.drop(labels=['id'], axis=1, inplace=True)

    time_cr = df['time_cr']
    df.drop(labels=['time_cr'], axis=1, inplace=True)
    df.insert(0, 'time_cr', time_cr)

    weight_unit = df['weight_unit']
    df.drop(labels=['weight_unit'], axis=1, inplace=True)
    df.insert(0, 'weight_unit', weight_unit)

    classes = df['classes']
    df.drop(labels=['classes'], axis=1, inplace=True)
    df.insert(0, 'classes', classes)

    producer = df['producer']
    df.drop(labels=['producer'], axis=1, inplace=True)
    df.insert(0, 'producer', producer)

    producer = df['producer']
    df.drop(labels=['producer'], axis=1, inplace=True)
    df.insert(0, 'producer', producer)

    process = df['process']
    df.drop(labels=['process'], axis=1, inplace=True)
    df.insert(0, 'process', process)

    front_qr_code = df['front_qr_code']
    df.drop(labels=['front_qr_code'], axis=1, inplace=True)
    df.insert(0, 'front_qr_code', front_qr_code)

    qrcode_id = df['qrcode_id']
    df.drop(labels=['qrcode_id'], axis=1, inplace=True)
    df.insert(0, 'qrcode_id', qrcode_id)

    production_order = df['production_order']
    df.drop(labels=['production_order'], axis=1, inplace=True)
    df.insert(0, 'production_order', production_order)

    # ********************调整列位置********************结束
    df.rename(columns={'qrcode_id': '一物一码'}, inplace=True)
    df.rename(columns={'gds_id': 'gds_id'}, inplace=True)
    df.rename(columns={'front_qr_code': '上工序一物一码'}, inplace=True)
    df.rename(columns={'classes': '班次'}, inplace=True)
    df.rename(columns={'process': '工序'}, inplace=True)
    df.rename(columns={'roll_length': '卷长'}, inplace=True)
    df.rename(columns={'roll_diameter': '卷径'}, inplace=True)
    df.rename(columns={'gross_weight': '总重量'}, inplace=True)
    df.rename(columns={'inspectionStatus': '检验状态'}, inplace=True)
    df.rename(columns={'shift_classes': '上一班次'}, inplace=True)
    df.rename(columns={'shift_roll_length': '上班次产量'}, inplace=True)
    df.rename(columns={'net_weight': '净重'}, inplace=True)
    df.rename(columns={'shift_classes_producer': '上班次生产者'}, inplace=True)
    df.rename(columns={'inspector': '检查员'}, inplace=True)
    df.rename(columns={'producer': '生产者'}, inplace=True)
    df.rename(columns={'package_no': '包号'}, inplace=True)
    df.rename(columns={'machine_number': '机器编号'}, inplace=True)
    df.rename(columns={'cotton_blending_ratio': '配棉比例'}, inplace=True)
    df.rename(columns={'width_cloth': '幅宽'}, inplace=True)
    df.rename(columns={'remark': '生产备注'}, inplace=True)
    df.rename(columns={'time_into': '导入时间'}, inplace=True)
    df.rename(columns={'batch_id': '批次编号'}, inplace=True)
    df.rename(columns={'bs_id': 'bs_id'}, inplace=True)
    df.rename(columns={'operator_id': '操作员编号'}, inplace=True)
    df.rename(columns={'syn': 'syn'}, inplace=True)
    df.rename(columns={'time_cr': '赋码时间'}, inplace=True)
    df.rename(columns={'time_into': 'time_into'}, inplace=True)
    df.rename(columns={'product_name': '产品名称'}, inplace=True)
    df.rename(columns={'machName': '单位'}, inplace=True)
    df.rename(columns={'material_code': '物料编号'}, inplace=True)
    df.rename(columns={'weight_unit': '数量'}, inplace=True)
    df.rename(columns={'username': 'PDA USER'}, inplace=True)
    df.rename(columns={'batch_type': '批次类型'}, inplace=True)
    df.rename(columns={'production_order': '订单号'}, inplace=True)
# ********************DataFrame数据源********************开始
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
# ********************DataFrame数据源********************结束

class DialogTongji(QDialog, Ui_dialog_tongji):
    def __init__(self, parent=None):
        super(DialogTongji, self).__init__(parent)
        self.setupUi(self)

        mainUI.pass_tongji_signal.connect(self.get_sum)

    def get_sum(self, df):
        # mainUI.statusBar().showMessage("统计完成", 2000)
        mainUI.label_show_count.setText(
            "共有{}条数据，页数{},当前页{}".format(mainUI.data_count, mainUI.data_pages, mainUI.current_page))
        # mainUI.statusBar().showMessage("共有{}条数据，页数{},当前页{}".format(mainUI.data_count, mainUI.data_pages, mainUI.current_page))
        model = pandasModel(df)
        self.tableView.setModel(model)
        tongji_ui.show()
        self.setWindowOpacity(0.8)

# 时间选择框
class DateEdit(QDialog, Ui_Dialog_Date_Edit):
    def __init__(self, parent=None):
        super(DateEdit, self).__init__(parent)
        self.setupUi(self)
        # 点击dialog的ok按钮触发的事件
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.writeback)

        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.closeSelf)
        self.setWindowOpacity(0.8)
        mainUI.passControlSignal.connect(self.getEdit)


        # self.move()

    def getEdit(self, edit):
        self.currentEdit = edit


    def writeback(self, edit):
        # print("=====================>" + str(edit))
        calendar_b = self.calendarWidget_b.selectedDate().toString("yyyy.MM.dd")
        calendar_a = self.calendarWidget_a.selectedDate().toString("yyyy.MM.dd")
        calendar = calendar_b + "~" + calendar_a
        print(calendar)
        self.currentEdit.setText(calendar)
        self.close()

    def closeSelf(self):
        mainUI.lineEdit_time_cr.clear()
        self.close()
from ZhuisuoDialog import Ui_ZhuisuoDialog
class ZhuisuoDialog(Ui_ZhuisuoDialog, QDialog):
    def __init__(self, parent=None):
        super(ZhuisuoDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.zhuisuoClick)
        self.datas = []
        self.setWindowOpacity(0.8)

    def zhuisuoClick(self):
        qrcode_id = self.lineEdit.text()
        self.search_thread = ZhuisuoThread(qrcode_id)
        self.search_thread.start()
        self.search_thread.zhuisuo_signal.connect(self.get_datas)

    def get_datas(self, datas):
        if len(datas) > 0:
            df = pandas.DataFrame(datas)
            df_adjustment(df)
            model = pandasModel(df)
        else:
            mainUI.statusBar().showMessage("没有数据", 2000)
            return
        self.tableView.setModel(model)

class ZhuisuoThread(QThread):
    zhuisuo_signal = pyqtSignal(list)
    def __init__(self, qrcode_id):
        super(ZhuisuoThread, self).__init__()
        self.qrcode_id = qrcode_id
        self.datas = []

    def zhuisuo(self, qrcode_id):
        datas = loginUI.crawl.search(process=0, qrcode_id=qrcode_id)['data']
        if len(datas) > 0:
            data = datas[0]
            if data['front_qr_code'] != '':
                self.datas.append(data)
                self.zhuisuo(data['front_qr_code'])
            else:
                self.datas.append(data)
    def run(self):
        self.zhuisuo(self.qrcode_id)
        self.zhuisuo_signal.emit(self.datas)
        mainUI.statusBar().clearMessage()

# mainWindow
class MyMainWindow(QMainWindow, Ui_MainWindow):
    passControlSignal = pyqtSignal(QLineEdit)
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.setGeometry(0, 0, 1024, 600)
        self.center()
        # self.setFixedSize(self.width(), self.height())
        self.lineEdit_time_cr.clicked.connect(self.timeEidtClicked)
        self.lineEdit_time_cr.textChanged.connect(self.seacth)
        self.pushButton_export.clicked.connect(self.exportExcel)
        self.pushButton_shang.clicked.connect(self.shangyiye)
        self.pushButton_xia.clicked.connect(self.xiayiye)
        self.comboBox_process.currentIndexChanged.connect(self.qiehuangongxu)
        self.btn_tongji.clicked.connect(self.actionSum)
        self.pushButton_class.clicked.connect(self.actionClassSum)
        self.comboBox_rows.currentIndexChanged.connect(self.comboBox_rows_currentIndexChangeEvent)

        print(self.menu.hasMouseTracking(), "------------->鼠标跟踪")
        self.menu.triggered.connect(lambda: print("------------>focusChanged"))
        self.actiontuichu.triggered.connect(app.quit)
        self.actionzhuisuo.triggered.connect(self.zhuisuoSearch)
        self.datas = []
        self.current_page = int(self.label_current_page.text())


        # self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.setWindowOpacity(0.8)


    def zhuisuoSearch(self):
        zhuisuoDialog = ZhuisuoDialog(mainUI)
        zhuisuoDialog.show()


    def comboBox_rows_currentIndexChangeEvent(self):
        self.current_page = 1
        self.label_current_page.setText("1")
        self.seacth()

    def qiehuangongxu(self):
        self.current_page = 1
        self.label_current_page.setText("1")
        self.seacth()

    def shangyiye(self):
        current_page = int(self.label_current_page.text())
        if int(current_page) <= 1:
            QMessageBox.information(self, "提示", "已经是第一页了，请稍后...")
            return
        self.current_page -= 1
        self.label_current_page.setText(str(current_page - 1))
        self.seacth()

    def xiayiye(self):
        current_page = int(self.current_page)
        if int(current_page >= self.data_pages):
            QMessageBox.information(self, "提示", "已经是最后一页了，请稍后...")
            return
        self.current_page += 1
        self.label_current_page.setText(str(current_page + 1))
        self.seacth()
    def exportExcel(self):
        if self.check_time_range():
            self.statusBar().showMessage("正在获取数据中，请稍后...")

            self.search = Search_Data({'rows':self.data_count,
                                       'page': 1,
                                       'qrcode_id': '',
                                       'process': self.comboBox_process.currentIndex()*10})
            self.search.start()
            self.search.display_signal.connect(self.export)

    def export(self, datas):
        json_data = datas['data']
        mainUI.label_show_count.setText("共有{}条数据，页数{},当前页{}".format(self.data_count, self.data_pages, self.current_page))
        # self.statusBar().showMessage("共有{}条数据，页数{},当前页{}".format(self.data_count, self.data_pages, self.current_page))
        fileName, file = QFileDialog.getSaveFileName(self, "导出Excel",
                                               "untitled.xls",
                                               "Excel (*.xls *.xlsx)")
        print(file)
        if fileName == "" or fileName is None:
            return False
        df = pandas.DataFrame(json_data)
        df_adjustment(df)
        df.to_excel(fileName, index=False)
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

    def sum(self, datas):
        df = pandas.DataFrame(datas['data'])
        if len(datas['data']) > 0:
            df['roll_length'] = df['roll_length'].astype(float)
            df = df.groupby(['production_order','classes',])['roll_length'].sum().reset_index()
            df.rename(columns={'roll_length': '总产量'}, inplace=True)
            df.rename(columns={'classes': '班次'}, inplace=True)
            df.rename(columns={'production_order': '订单号'}, inplace=True)
            print(df)
        self.pass_tongji_signal.emit(df)


    def actionClassSum(self):
        if self.check_time_range():
            self.statusBar().showMessage("正在计算中，请稍后...")
            self.searchThread = Search_Data({'rows':self.data_count,
                                       'page': 1,
                                       'qrcode_id': '',
                                       'process': self.comboBox_process.currentIndex()*10})
            self.searchThread.start()
            self.searchThread.display_signal.connect(self.classSum)

    def classSum(self, datas):
        df = pandas.DataFrame(datas['data'])
        if len(datas['data']) > 0:
            df['roll_length'] = df['roll_length'].astype(float)
            df = df.groupby(['classes'])['roll_length'].sum().reset_index()
            df.rename(columns={'roll_length': '总产量'}, inplace=True)
            df.rename(columns={'classes': '班次'}, inplace=True)
            # df.rename(columns={'production_order': '订单号'}, inplace=True)
            print(df)
        self.pass_tongji_signal.emit(df)

    def actionSum(self):
        if self.check_time_range():
            self.statusBar().showMessage("正在计算中，请稍后...")
            self.searchThread = Search_Data({'rows':self.data_count,
                                       'page': 1,
                                       'qrcode_id': '',
                                       'process': self.comboBox_process.currentIndex()*10})
            self.searchThread.start()
            self.searchThread.display_signal.connect(self.sum)

    def check_time_range(self):
        time_range = mainUI.lineEdit_time_cr.text()
        if self.comboBox_process.currentIndex() == 0:
            QMessageBox.information(self, '提示', "请选择工序")
            return False
        elif time_range.strip() == "":
            QMessageBox.information(self, '提示', "请输入赋码范围")
            return False
        else:
            return True

    def seacth(self):
        self.statusBar().showMessage("正在查询中，请稍后...")
        #time_range=time_range, process=self.params['process'],
        # qrcode_id=self.params['qrcode_id'],rows=self.params['rows'], page=self.params['page']
        self.search = Search_Data({'process': (int(self.comboBox_process.currentIndex())) * 10,
                                   'rows': self.comboBox_rows.currentText(),
                                   'page': self.label_current_page.text()})
        self.search.display_signal.connect(self.fill_grid)
        self.search.start()
        # search.wait()


    def fill_grid(self, json):

        self.datas = json['data']
        self.data_count = json['records']

        if self.data_count % int(self.comboBox_rows.currentText()) == 0 and self.data_count < int(self.comboBox_rows.currentText()):
            self.data_pages = self.data_count // int(self.comboBox_rows.currentText())
        else:
            self.data_pages = self.data_count // int(self.comboBox_rows.currentText()) + 1

        mainUI.label_show_count.setText(
            "共有{}条数据，页数{},当前页{}".format(self.data_count, self.data_pages, self.current_page))
        # self.statusBar().showMessage("共有{}条数据，页数{},当前页{}".format(self.data_count, self.data_pages, self.current_page))

        if len(self.datas) == 0:
            self.statusBar().showMessage('没有数据', 2000)
            return

        df = pandas.DataFrame(json['data'])
        df_adjustment(df)

        model = pandasModel(df)
        self.tableView.setModel(model)


# 爬取数据的线程
class Search_Data(QThread):
    display_signal = pyqtSignal(dict) ##此处定义了一个信号，可以用来与主程序交互
    def __init__(self, params):
        super().__init__()  ## 继承QThread
        self.params = params
    def run(self):
        time_range = mainUI.lineEdit_time_cr.text()

        mainUI.pushButton_xia.setEnabled(False)
        mainUI.pushButton_shang.setEnabled(False)
        mainUI.btn_tongji.setEnabled(False)
        mainUI.pushButton_export.setEnabled(False)
        mainUI.pushButton_class.setEnabled(False)

        try:
            json = loginUI.crawl.search(time_range=time_range,
                                        process=self.params['process'],
                                        rows=self.params['rows'],
                                        page=self.params['page'])
        except Exception:
            mainUI.statusBar().showMessage("服务器错误...", 2000)
            return
        finally:
            mainUI.btn_tongji.setEnabled(True)
            mainUI.pushButton_xia.setEnabled(True)
            mainUI.pushButton_shang.setEnabled(True)
            mainUI.pushButton_export.setEnabled(True)
            mainUI.btn_tongji.setEnabled(True)
            mainUI.pushButton_export.setEnabled(True)
            mainUI.pushButton_class.setEnabled(True)
            mainUI.statusBar().clearMessage()
        self.display_signal.emit(json)

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
        self.setWindowOpacity(0.8)

    def keyPressSlot(self, keyEvent):
        if keyEvent.key() == Qt.Key_Enter:
            self.btn_login.click()

    # 爬取验证码并显示
    def setCapcha(self):
        captchaBytes = self.crawl.get_captcha()
        pixmap = QPixmap()
        pixmap.loadFromData(captchaBytes)
        self.label_captcha.setPixmap(pixmap)

    # 窗口居中
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


    def keyPressEvent(self, keyEvent):
        print(keyEvent.key())
        if keyEvent.key() == Qt.Key_Return:
            self.btn_login.click()


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
            mainUI.seacth()
        else:
            self.lineEdit_capcha.clear()
            QMessageBox.information(self, '提示', loginTitle)
            self.setCapcha()
if __name__ == '__main__':
    app = QApplication(sys.argv)

    loginUI = LoginUI()

    mainUI = MyMainWindow()

    dateEditDialog = DateEdit(mainUI)

    tongji_ui = DialogTongji(mainUI)

    loginUI.show()
    sys.exit(app.exec_())


