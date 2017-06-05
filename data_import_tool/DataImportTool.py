# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DBOperator import *
from UIDataImportTool import *
import xlrd

reload(sys)
sys.setdefaultencoding('utf-8')


class DataImportTool(QDialog):
    def __init__(self):
        super(DataImportTool, self).__init__()
        self.ui = Ui_DataImportTool()
        self.ui.setupUi(self)

        self.ui.user_path_button.clicked.connect(self.select_user_path)
        self.ui.import_button.clicked.connect(self.import_data)

        self.db_operator = DBOperator()

    def select_user_path(self):
        path, file_filter = QFileDialog().getOpenFileName(self, '导入用户数据Excel', '')
        if path:
            self.ui.user_path_edit.setText(path)

    def import_data(self):
        self.import_user_data()
        self.import_bank_data()

    def import_user_data(self):
        excel_path = self.ui.user_path_edit.text()
        excel_data = xlrd.open_workbook(excel_path)
        user_table = excel_data.sheets()[1]
        for row_index in range(1, user_table.nrows):
            # 户主姓名 家庭成员姓名 与户主关系 身份证号码 户主身份证号码
            data_array = user_table.row_values(row_index)
            single_user = User()
            single_user.name = data_array[1]
            single_user.relationship = data_array[2]
            single_user.identifier = data_array[3]
            single_user.head_identifier = data_array[4]
            self.db_operator.add_user(single_user)
        QMessageBox().information(self, '提示', '导入用户数据成功。')

    def import_bank_data(self):
        excel_path = self.ui.user_path_edit.text()
        excel_data = xlrd.open_workbook(excel_path)
        bank_table = excel_data.sheets()[2]
        for row_index in range(1, bank_table.nrows):
            # 证件号码 客户名称 存款日均余额 贷款余额 信用卡额度 是否签约短信银行 是否签约手机银行 客户星级 联系电话
            data_array = bank_table.row_values(row_index)
            single_bank_data = BankData()
            single_bank_data.customer = data_array[0]
            if data_array[2]:
                single_bank_data.daily_deposit = data_array[2]
            else:
                single_bank_data = 0
            if data_array[3]:
                single_bank_data.loan_balance = int(data_array[3])
            else:
                single_bank_data.loan_balance = 0
            if data_array[4]:
                single_bank_data.credit_card_limit = data_array[4]
            else:
                single_bank_data.credit_card_limit = 0
            single_bank_data.is_sms = (data_array[5] == '是')
            single_bank_data.is_phone = (data_array[6] == '是')
            single_bank_data.stars = data_array[7]
            single_bank_data.phone_number = data_array[8]
            self.db_operator.add_bank_data(single_bank_data)
        QMessageBox().information(self, '提示', '导入银行账户数据成功。')

if __name__ == '__main__':
    QApplication.addLibraryPath('qt5_plugins')
    app = QApplication(sys.argv)
    w = DataImportTool()
    w.show()
    sys.exit(app.exec_())
