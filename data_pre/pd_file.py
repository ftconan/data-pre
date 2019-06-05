"""
@author: magician
@file: pd_file.py
@date: 2019/06/05
"""


class PdFile(object):
    """
    PdFile
    """
    def __init__(self, file, file_type, **kwargs):
        """
        init file,file_type
        :param file:
        :param file_type:
        :param kwargs:
        """
        self.file = file
        self.file_type = file_type
        self.kwargs = kwargs

    def df_pre(self, data):
        """
        pre data
        :param data:
        :return:
        """
        pass
