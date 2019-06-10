"""
@author: magician
@file: pd_pickle.py
@date: 2019/06/10
"""
import os

import pandas as pd


def read_pickle(file, **kwargs):
    """
    read pickle
    :param file:    pickle
    :param kwargs:
    :return: DataFrame
    """
    pickle_df = pd.read_pickle(file, **kwargs)

    return pickle_df


def write_pickle(df, **kwargs):
    """
    write pickle
    :param df:
    :param kwargs: file_name:     file name
                   file_path:     file path
    :return: {
        'file_name': file_name,
        'output_path': output_path
    }
    """
    file_name = kwargs.get('file_name', '')
    file_path = kwargs.get('file_path', '')
    output_path = os.path.join(file_path, file_name)

    df.to_pickle(output_path, **kwargs)

    return {
        'file_name': file_name,
        'output_path': output_path
    }
