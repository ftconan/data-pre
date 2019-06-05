# coding=utf-8
"""
@author: magician
@file: excel.py
@date: 2018/12/17
"""
import copy
import os
import random
import time
import pandas as pd

from data_pre.pd_check import check_data_type
from data_pre.pd_error import checker


class PdExcel:
    """
    pandas excel
    """
    def __init__(self, excel_path, excel_name, excel_type, **kwargs):
        """
        :param excel_path: excel路径
        :param excel_name: excel名称
        :param excel_type: excel类型

        checker            excel checker
        sheet_name         excel sheet
        header             忽略excel前几行(标题)
        excel_data         excel数据
        export_data        导出数据
        error_list         错误列表
        columns            excel列
        rows               excel行
        pre_row            预览行数
        pre_type           预览类型(all head tail)
        """
        self.excel_path = excel_path
        self.excel_name = excel_name
        self.excel_type = excel_type
        self.checker = checker.get('hc_po')
        self.sheet_name = kwargs.get('sheet_name', '')
        self.header = kwargs.get('header')
        self.excel_data = pd.DataFrame()
        self.export_excel = pd.DataFrame()
        self.error_list = []
        self.columns = []
        self.rows = []
        self.pre_row = kwargs.get('pre_row')
        self.pre_type = kwargs.get('pre_type', 'head')
        pd.set_option('display.max_columns', 100)

    def read_excel(self):
        """
        读取excel  excel to DataFrame
        :return:
        """
        import_dir = os.path.join(self.excel_path, self.excel_name)
        # self.excel_data = pd.read_excel(pd.ExcelFile(import_dir), self.sheet_name, header=self.header, index_col=None,
        #                                 na_values=['NA'])
        self.excel_data = pd.read_excel(pd.ExcelFile(import_dir), self.sheet_name, header=self.header)
        # 筛选其中的列
        if self.checker:
            self.excel_data = self.excel_data[list(self.checker.keys())]
        # 查看是否含有异常值。
        # self.excel_data.describe()
        # 检查是否包含重复值
        excel_flag = self.excel_data.duplicated().any()
        if excel_flag:
            self.excel_data.drop_duplicates(inplace=True)

        self.columns = self.excel_data.columns
        self.rows = self.excel_data.index

        return self.excel_data

    def write_excel(self):
        """
        写excel   DataFrame to excel
        :return:
        """
        # excel 随机名称
        name, suffix = self.excel_name.split(',')
        time_str = str(time.time())
        random_str = str(random.randint(1, 10000))
        export_name = time_str + random_str + suffix

        export_dir = os.path.join(self.excel_path, export_name)
        self.export_excel.to_excel(export_dir, sheet_name=self.sheet_name)

    def check_data(self):
        """
        excel数据检查
        1.获得预览数据
        2.添加错误信息
        :return:
        """
        # 获得预览数据
        if self.pre_type == 'all':
            pre_df = self.excel_data
        elif self.pre_type == 'head':
            pre_df = self.excel_data.head(self.pre_row)
        elif self.pre_type == 'tail':
            pre_df = self.excel_data.tail(self.pre_row)
        else:
            pre_df = pd.DataFrame()

        # 添加错误信息
        if self.pre_row and self.pre_type != 'all':
            self.error_list = ['']*self.pre_row
        else:
            self.error_list = [''] * len(self.rows)

        new_pre_df = copy.deepcopy(pre_df)
        for col in self.columns:
            for index, value in enumerate(pre_df[col]):
                self.error_list[index] += check_data_type(col, value, self.checker[col])

        # print(self.error_list, len(self.error_list))
        new_pre_df['error'] = self.error_list

        return new_pre_df

    @staticmethod
    def df_to_json(df):
        """
        DataFrame to json
        :return:
        """
        df_json = df.to_json(orient='index')
        return df_json

    def preview_excel(self):
        """
        预览excel
        :return:
        """
        pre_df = pd_excel.check_data()
        pre_data = self.df_to_json(pre_df)

        print(pre_data)
        return pre_data


if __name__ == '__main__':
    time1 = time.time()
    pd_kw = {
        'header': 1,
        'sheet_name': 'Sheet1',
        # 'pre_row': 5
        'pre_type': 'all'
    }
    pd_excel = PdExcel('/home/magician/Documents', '17229N006B（1） PO.xls', 'hc_po', **pd_kw)
    pd_excel.read_excel()
    pd_excel.preview_excel()
    time2 = time.time()
    print(time2 - time1)
