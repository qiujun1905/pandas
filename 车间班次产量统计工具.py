import os
import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDesktopWidget, QLineEdit, \
    QLabel, QFileDialog, QComboBox, QMessageBox

pd.set_option('display.max_columns', None)   #显示完整的列
pd.set_option('display.max_rows', None)  #显示完整的行


class ProductionProcesses(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 创建控件
        self.fileEdit = QLineEdit()
        button = QPushButton("浏览...")
        button.clicked.connect(self.spunlaceClicked)

        sumButton = QPushButton("统计")
        sumButton.clicked.connect(self.sumClicked)

        self.lable = QLabel()
        self.combox = QComboBox()
        self.items = ['水刺按班统计', '拖漂烘干按班统计', '验布按班统计', '分切按班统计', '覆膜按班统计', ]
        self.combox.addItems(self.items)


        #创建布局管理器并添加控件
        fileChoiceLayout = QHBoxLayout()
        fileChoiceLayout.addWidget(self.fileEdit)
        fileChoiceLayout.addWidget(button)
        fileChoiceLayout.addWidget(self.combox)
        fileChoiceLayout.addWidget(sumButton)



        layout = QVBoxLayout()

        layout.addLayout(fileChoiceLayout)
        layout.addWidget(self.lable)


        self.setLayout(layout)



        self.resize(600, 300)
        self.setWindowTitle('车间班次产量统计工具')
        self.center()
        self.show()

    def spunlaceClicked(self):
        fileName, fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.txt)")
        self.fileEdit.setText(fileName)


    def sumClicked(self):
        # '水刺按班统计', '拖漂烘干按班统计', '验布按班统计', '分切按班统计', '覆膜按班统计',
        gongxu = self.combox.currentText()
        file = self.fileEdit.text()
        index = -5
        if(gongxu == self.items[1]):
            index = -8
        if(gongxu == self.items[2]):
            index = -4
        if(gongxu == self.items[3]):
            index = -5
        if(gongxu == self.items[4]):
            index = -5
        df = None
        try:
            df = sum_by_excel(file, index)
        except :
            msg_box = QMessageBox(QMessageBox.Warning, '提示', '读取excel文件出现异常，请删除excel第一行保存再次尝试！')
            msg_box.exec_()
        if df is not None:
            sum = df.to_string()
            self.lable.setText(sum)


    def center(self):
        # 得到主体框架的信息
        qr = self.frameGeometry()
        # 得到桌面的中心
        cp = QDesktopWidget().availableGeometry().center()
        # 框架的中心与桌面的中心对齐
        qr.moveCenter(cp)
        # 自身窗体的左上角与框架的左上角对齐
        self.move(qr.topLeft())


def sum_by_excel(excel, index):
    df2 = pd.read_excel(excel,)
    df2['班次'] = df2['产品批号(一物一码)'].str[index]
    df2['数量'] = df2['数量'].str[0:-1].str.replace(',', '')
    print(df2)
    df2['数量'] = df2['数量'].astype(float)
    df2 = df2.groupby(['班次'])['数量'].sum().reset_index()
    df2.set_index(['班次'], inplace=True)

    print(df2)
    return df2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pp = ProductionProcesses()
    sys.exit(app.exec_())
