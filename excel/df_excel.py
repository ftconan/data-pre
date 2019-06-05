"""
@file:   df_excel.py
@author: magician
@date:   2019/4/1
"""
import os
import random
import time
import pandas as pd


def df_to_excel(**kwargs):
    """
    dataframe to excel
    :param kwargs:   excel_header:  列名
                     excel_data:    dataframe
                     excel_name:    excel名称
                     is_email:      是否发送邮件
                     sheet_names:   sheet
    :return:
    """
    excel_header = kwargs.get('excel_header')
    excel_data = kwargs.get('excel_data')
    excel_name = kwargs.get('excel_name')
    is_email = kwargs.get('is_email')
    sheet_names = kwargs.get('sheet_names')

    time_str = str(time.time())
    random_str = str(random.randint(1, 10000))
    file_name = time_str + random_str + '.xls'
    pdf_dir = ''
    file_path = os.path.join(pdf_dir, file_name)
    # excel_data.to_excel(excel_writer=file_path, index=False)
    with pd.ExcelWriter(file_path) as writer:
        if sheet_names:
            for index, sheet in enumerate(sheet_names):
                excel_data[index].to_excel(excel_writer=writer, header=excel_header[index], sheet_name=sheet, index=False,
                                           encoding='utf-8')
        else:
            excel_data.to_excel(excel_writer=writer, header=excel_header, index=False, encoding='utf-8')

    response = {
        'file_name': file_name,
        'file_path': file_path
    }

    return response
