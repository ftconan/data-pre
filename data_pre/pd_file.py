"""
@author: magician
@file: pd_file.py
@date: 2019/06/05
"""
import importlib

import pandas as pd

from data_pre.pd_params import READ_FILE, WRITE_FILE
from data_pre.pd_utils import check_type


class PdFile(object):
    """
    PdFile
    """
    def __init__(self, file, file_type, **kwargs):
        """
        init file,file_type
        :param file:
        :param file_type:  file type
        :param kwargs:
        """
        self.file = file
        self.file_type = file_type
        self.df = pd.DataFrame()
        self.kwargs = kwargs

    def read_file(self):
        """
        read excel, csv, pickle(at this time)
        :param:  drop_flag   True or False
        :return: DataFrame
        """
        drop_flag = self.kwargs.get('drop_flag')
        if self.file_type not in list(READ_FILE.keys()):
            return '{0} file type is not supported at this time!'.format(self.file_type)

        reader = importlib.import_module(READ_FILE[self.file_type])
        self.df = reader(self.file, **self.kwargs)
        # drop duplicates data
        self.df.drop_duplicates(inplace=bool(drop_flag))

        return self.df

    def write_file(self):
        """
        write excel, csv, pickle(at this time)
        :return: File
        """
        if self.file_type not in list(WRITE_FILE.keys()):
            return '{0} file type is not supported at this time!'.format(self.file_type)

        writer = importlib.import_module(WRITE_FILE[self.file_type])
        new_file = writer(self.df, **self.kwargs)

        return new_file

    def df_preview(self):
        """
        preview DataFrame
        :param: pre_list      index or label
        :param: data_index    row or column
        :param: dtype         int or string
        :return: DataFrame
        """
        pre_list = self.kwargs.get('pre_list', [])
        data_index = self.kwargs.get('data_index', 'row')
        dtype = self.kwargs.get('dtype', 'int')
        error = ''
        df = pd.DataFrame()
        if pre_list < 1 or not isinstance(pre_list, list):
            error = 'pre_list data is error!'
        elif len(pre_list) == 2:
            if dtype == 'int':
                error = check_type(pre_list, dtype)
                if not error:
                    if pre_list[-1] == 0:
                        df = self.df.head(pre_list[0])
                    elif pre_list[0] == 0:
                        df = self.df.tail(pre_list[0])
                    else:
                        df = self.df.iloc[pre_list[0]:pre_list[-1]]
            elif dtype == 'string':
                error = check_type(pre_list, dtype)
                df = self.df.loc[pre_list, :] if data_index == 'row' else self.df.loc[:, pre_list]
            else:
                error = 'dtype error!'
        else:
            if dtype == 'string':
                df = self.df.loc[pre_list, :] if data_index == 'row' else self.df.loc[:, pre_list]
            else:
                error = 'dtype error!'

        if error:
            return error

        return df

    def df_remove(self):
        """
        DataFrame remove
        :param:         rows     list
        :param:         columns  list
        :return: DataFrame
        """
        rows = self.kwargs.get('rows', [])
        columns = self.kwargs.get('columns', [])
        self.df = self.df.drop(index=rows, columns=columns, inplace=True)

        return self.df

    def df_select(self):
        """
        DataFrame select
        :param: rows     list
        :param: columns  list
        :param: dtype    int or string
        :return: DataFrame
        """
        rows = self.kwargs.get('rows', [])
        columns = self.kwargs.get('columns', [])
        dtype = self.kwargs.get('dtype')
        data = []
        df = pd.DataFrame()
        data.extend(rows)
        data.extend(columns)
        error = check_type(data, dtype)
        if not error:
            if dtype == 'int':
                if len(rows) == 2 and len(columns) == 2:
                    df = self.df.iloc[rows[0]:rows[-1], columns[0]:columns[-1]]
                else:
                    error = 'rows or columns error!'
            else:
                df = self.df.loc[rows, columns]

        if error:
            return error

        return df

    def df_style(self):
        """
        DataFrame style
        :param:         is_style_func True or False
        :param:         background_color:   background color
        :param:         color:              font color
        :param:         border_color:       border color
        :param:         style_map_func      style map function
        :param:         style_func          style function
        :param:         precision
        :return: DataFrame
        """
        is_style_func = self.kwargs.get('is_style_func', False)
        if is_style_func:
            background_color = self.kwargs.get('background_color')
            color = self.kwargs.get('color')
            border_color = self.kwargs.get('border_color')
            df = self.df.style.set_properties(
                **{
                    'background-color': background_color,
                    'color': color,
                    'border-color': border_color
                })
        else:
            style_map_func = self.kwargs.get('style_map_func')
            style_func = self.kwargs.get('style_func')
            precision = self.kwargs.get('precision', 2)
            df = self.df.style.applymap(style_map_func).apply(style_func).set_precision(precision)

        return df

    def df_pre(self):
        """
        DataFrame preprocessing
        :return:  DataFrame
        """
        pass

    def df_statistics(self):
        """
        DataFrame statistics
        :return: DataFrame
        """
        pass
